from django.shortcuts import render, get_object_or_404, redirect
from .models import Picture
from .forms import PictureFilterForm, PictureStatusForm, SandboxFilterForm
from django.db.models.functions import Random
from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test


def index(request):
    form = PictureFilterForm(request.GET)
    pictures = Picture.objects.filter(author__isnull=False, is_verified=True).order_by('-date')

    if form.is_valid():
        if form.cleaned_data['category']:
            pictures = pictures.filter(category=form.cleaned_data['category'])
        if form.cleaned_data['authors']:
            pictures = pictures.filter(author=form.cleaned_data['authors'])
        if form.cleaned_data['tag_search']:
            pictures = pictures.filter(tags__title__icontains=form.cleaned_data['tag_search'])

        sorting = form.cleaned_data['sorting']
        if sorting == 'date':
            pictures = pictures.order_by('date')
        elif sorting == 'downloads':
            pictures = pictures.order_by('-downloads')
        elif sorting == 'rating':
            pictures = pictures.order_by('-rating')
        elif sorting == 'random':
            pictures = pictures.annotate(random_order=Random()).order_by('random_order')

    paginator = Paginator(pictures, 15)
    page = request.GET.get('page')

    try:
        pictures = paginator.page(page)
    except PageNotAnInteger:
        pictures = paginator.page(1)
    except EmptyPage:
        pictures = paginator.page(paginator.num_pages)

    context = {'pictures': pictures, 'form': form}
    return render(request, 'cards/index.html', context)


def sandbox(request):
    form = SandboxFilterForm(request.GET)
    picture_status_form = PictureStatusForm()
    pictures = Picture.objects.filter(author__isnull=False).order_by('-date')

    if form.is_valid():
        if form.cleaned_data['category']:
            pictures = pictures.filter(category=form.cleaned_data['category'])
        if form.cleaned_data['authors']:
            pictures = pictures.filter(author=form.cleaned_data['authors'])
        if form.cleaned_data['tag_search']:
            pictures = pictures.filter(tags__title__icontains=form.cleaned_data['tag_search'])

        sorting = form.cleaned_data['sorting']
        if sorting == 'date':
            pictures = pictures.order_by('date')
        elif sorting == 'downloads':
            pictures = pictures.order_by('-downloads')
        elif sorting == 'rating':
            pictures = pictures.order_by('-rating')
        elif sorting == 'random':
            pictures = pictures.annotate(random_order=Random()).order_by('random_order')

        status = form.cleaned_data['status']
        if status == 'verified':
            pictures = pictures.filter(is_verified=True)
        elif status == 'unverified':
            pictures = pictures.filter(is_verified=False)

    paginator = Paginator(pictures, 15)
    page = request.GET.get('page')

    try:
        pictures = paginator.page(page)
    except PageNotAnInteger:
        pictures = paginator.page(1)
    except EmptyPage:
        pictures = paginator.page(paginator.num_pages)

    context = {'pictures': pictures, 'form': form, 'picture_status_form': picture_status_form, 'active_page': 'sandbox'}
    return render(request, 'cards/sandbox.html', context)


def image_detail(request, image_id):
    picture = get_object_or_404(Picture, id=image_id)

    is_author = request.user == picture.author

    template_name = 'cards/image_detail_profile.html' if is_author else 'cards/image_detail.html'

    context = {'picture': picture}
    return render(request, template_name, context)


def download_image(request, image_id):
    picture = get_object_or_404(Picture, pk=image_id)

    Picture.objects.filter(pk=image_id).update(downloads=F('downloads') + 1)

    image_path = os.path.join(settings.MEDIA_ROOT, str(picture.image))
    with open(image_path, 'rb') as image_file:
        response = HttpResponse(image_file.read(), content_type='image/jpeg')
        response['Content-Disposition'] = f'attachment; filename="{picture.image.name}"'

    return response


def delete_image(request, image_id):
    picture = get_object_or_404(Picture, id=image_id)

    if request.user == picture.author:
        picture.delete()
        return redirect('profile')
    elif request.user.groups.filter(name='Moderators').exists():
        picture.delete()
        return redirect('sandbox')
    else:
        return HttpResponseForbidden("You don't have permission to delete this image.")


def change_picture_status(request, image_id):
    picture = get_object_or_404(Picture, pk=image_id)

    if request.method == 'POST':
        form = PictureStatusForm(request.POST, instance=picture)
        if form.is_valid():
            picture.is_verified = form.cleaned_data['is_verified']
            picture.save()

    return redirect('sandbox')


@csrf_exempt
@user_passes_test(lambda u: u.groups.filter(name='Moderators').exists())
def toggle_verification(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        picture_id = data.get('picture_id')
        is_verified = data.get('is_verified')

        try:
            picture = Picture.objects.get(id=picture_id)
            picture.is_verified = is_verified
            picture.save()

            return JsonResponse({'success': True, 'is_verified': picture.is_verified})
        except Picture.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Picture not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
