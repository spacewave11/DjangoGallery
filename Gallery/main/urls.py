from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  path('', views.index, name='home'),
                  path('image/<int:image_number>/', views.image_detail, name='image_detail'),
                  path('categories/', views.categories, name='categories'),
                  path('categories/<slug:category_slug>/', views.category_images, name='category_images'),
                  path('account/', views.account, name='account'),
                  path('top_authors/', views.top_authors, name='top_authors'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)