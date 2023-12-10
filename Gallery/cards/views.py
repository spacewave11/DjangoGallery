from django.shortcuts import render
from .models import Picture
from .forms import PictureFilterForm
from django.db.models.functions import Random


def index(request):
    form = PictureFilterForm(request.GET)
    pictures = Picture.objects.all()

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





# def image_detail(request, image_id):
#     image = Picture.objects.get(pk=image_id)
#     # images = Picture.objects.all()
#     # a = images.first()
#     return render(request, 'cards/image_detail.html', {'image': image})
#
#
# def card_list(request):
#     images = Image.objects.all()
#     return render(request, 'cards/card_list.html', {'images': images})



# def index(request):
# print(pictures.tags.first())
# tag = Tag.objects.filter(title='Snow')[0]
# tagged_pics = Picture.objects.filter(tags=tag)
# print(tagged_pics)

# picture = Picture.objects.all().first()
# pictures = Picture.objects.filter(author_id=1)
# print(pictures[1].category)

# picture = Picture.objects.filter(author_id=1).first()
# print(picture.author.account.account_image.url)

# user_list = User.objects.all()
# for user in user_list:
#     print(Picture.objects.filter(author=user))
# print(user_list)

# form = PictureFilterForm(request.GET)
# pictures = Picture.objects.all()
#
# if form.is_valid() and form.cleaned_data['category']:
#     pictures = pictures.filter(category=form.cleaned_data['category'])
#
# context = {'pictures': pictures, 'form': form}
# return render(request, 'cards/index.html', context)

# return render(request, 'cards/index.html', {'images': images})


# def image_detail(request, image_number):
#     images = images1
#
#     image = next((img for img in images if img['id'] == image_number), None)
#
#     if image:
#         return render(request, 'cards/image_detail.html', {'image': image})
#     else:
#         return render(request, 'cards/image_detail.html', {'image_number': image_number})
