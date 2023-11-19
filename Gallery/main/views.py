# main/views.py
from django.shortcuts import render
from .models import Image

images1 = [
    {'id': 1, 'user_avatar': 'main/avatars/ava1.jpg', 'user_nickname': 'John', 'image': 'main/img/picture1.jpg',
     'timestamp': '18 ноября в 22:00'},
    {'id': 2, 'user_avatar': 'main/avatars/ava2.jpg', 'user_nickname': 'Jack', 'image': 'main/img/picture2.jpg',
     'timestamp': '17 ноября в 20:30'},
    {'id': 3, 'user_avatar': 'main/avatars/ava3.jpg', 'user_nickname': 'Daniel', 'image': 'main/img/picture3.jpg',
     'timestamp': '10 ноября в 15:00'},
    {'id': 4, 'user_avatar': 'main/avatars/ava4.jpg', 'user_nickname': 'Иван', 'image': 'main/img/picture4.jpg',
     'timestamp': '15 ноября в 00:00'},
    {'id': 5, 'user_avatar': 'main/avatars/ava5.jpg', 'user_nickname': 'Veritasium', 'image': 'main/img/picture5.jpg',
     'timestamp': '11 ноября в 02:00'},
    {'id': 6, 'user_avatar': 'main/avatars/ava6.jpg', 'user_nickname': 'Сергей', 'image': 'main/img/picture6.jpg',
     'timestamp': '14 октября в 23:00'},
    {'id': 7, 'user_avatar': 'main/avatars/ava7.jpg', 'user_nickname': 'Елена', 'image': 'main/img/picture7.jpg',
     'timestamp': '07 ноября в 17:00'},
    {'id': 8, 'user_avatar': 'main/avatars/ava8.jpg', 'user_nickname': 'Катя', 'image': 'main/img/picture8.jpg',
     'timestamp': '16 февраля в 04:00'},
    {'id': 9, 'user_avatar': 'main/avatars/ava9.jpg', 'user_nickname': 'Magnus', 'image': 'main/img/picture9.jpg',
     'timestamp': '25 мая в 01:00'},
    {'id': 10, 'user_avatar': 'main/avatars/ava10.jpg', 'user_nickname': 'Carlsen', 'image': 'main/img/picture10.jpg',
     'timestamp': '20 ноября в 11:00'},
    {'id': 11, 'user_avatar': 'main/avatars/ava11.jpg', 'user_nickname': 'Ян', 'image': 'main/img/picture11.jpg',
     'timestamp': '29 апреля в 10:00'},
    {'id': 12, 'user_avatar': 'main/avatars/ava12.jpg', 'user_nickname': 'Spacex', 'image': 'main/img/picture12.jpg',
     'timestamp': '11 апреля в 04:00'},
    {'id': 13, 'user_avatar': 'main/avatars/ava13.jpg', 'user_nickname': 'Nakamura', 'image': 'main/img/picture13.jpg',
     'timestamp': '03 июня в 16:00'},
    {'id': 14, 'user_avatar': 'main/avatars/ava14.jpg', 'user_nickname': 'Caruana', 'image': 'main/img/picture14.jpg',
     'timestamp': '04 июля в 22:00'},
    {'id': 15, 'user_avatar': 'main/avatars/ava15.jpg', 'user_nickname': 'Olga', 'image': 'main/img/picture15.jpg',
     'timestamp': '18 ноября в 22:00'},
    {'id': 16, 'user_avatar': 'main/avatars/ava16.jpg', 'user_nickname': 'Натали', 'image': 'main/img/picture16.jpg',
     'timestamp': '18 ноября в 22:00'},
    {'id': 17, 'user_avatar': 'main/avatars/ava17.jpg', 'user_nickname': 'Юля', 'image': 'main/img/picture17.jpg',
     'timestamp': '18 ноября в 22:00'},
    {'id': 18, 'user_avatar': 'main/avatars/ava18.jpg', 'user_nickname': 'Sam Altman',
     'image': 'main/img/picture18.jpg',
     'timestamp': '19 июля в 17:20'},
]


def index(request):
    images = images1
    return render(request, 'main/index.html', {'images': images})


def image_detail(request, image_number):
    images = images1

    image = next((img for img in images if img['id'] == image_number), None)

    if image:
        return render(request, 'main/image_detail.html', {'image': image})
    else:
        return render(request, 'main/image_detail.html', {'image_number': image_number})
