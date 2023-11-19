"""
URL configuration for Gallery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# main/urls.py

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
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
