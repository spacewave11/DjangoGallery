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
# users/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views
from .views import *

urlpatterns = [
                  path('', views.index, name='user_index'),
                  path('register/', register, name='register'),
                  path('login/', login, name='login'),
                  path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
                  path('upload_image/', upload_image, name='upload_image'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
