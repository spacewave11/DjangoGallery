from django.shortcuts import render, get_object_or_404
from .models import Picture
from .forms import PictureFilterForm
from django.db.models.functions import Random
from django.http import HttpResponse
from django.conf import settings
from django.db.models import F
import os


def index(request):
    form = PictureFilterForm(request.GET)
    pictures = Picture.objects.filter(author__isnull=False)

    if form.is_valid():
        if form.cleaned_data['category']:
            pictures = pictures.filter(category=form.cleaned_data['category'])
        if form.cleaned_data['authors']:
            pictures = pictures.filter(author=form.cleaned_data['authors'])
        if form.cleaned_data['tag_search']:
            pictures = pictures.filter(tags__title__icontains=form.cleaned_data['tag_search'])

        sorting = form.cleaned_data['sorting']
        if sorting == 'date':
            pictures = pictures.order_by('-date')
        elif sorting == 'downloads':
            pictures = pictures.order_by('-downloads')
        elif sorting == 'rating':
            pictures = pictures.order_by('-rating')
        elif sorting == 'random':
            pictures = pictures.annotate(random_order=Random()).order_by('random_order')

    context = {'pictures': pictures, 'form': form}
    return render(request, 'cards/index.html', context)


def image_detail(request, image_id):
    picture = get_object_or_404(Picture, pk=image_id)
    return render(request, 'cards/image_detail.html', {'picture': picture})


def download_image(request, image_id):
    picture = get_object_or_404(Picture, pk=image_id)

    Picture.objects.filter(pk=image_id).update(downloads=F('downloads') + 1)

    image_path = os.path.join(settings.MEDIA_ROOT, str(picture.image))
    with open(image_path, 'rb') as image_file:
        response = HttpResponse(image_file.read(), content_type='image/jpeg')
        response['Content-Disposition'] = f'attachment; filename="{picture.image.name}"'

    return response
