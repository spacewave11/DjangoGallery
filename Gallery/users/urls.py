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
                  path('logout/', auth_views.LogoutView.as_view(next_page='cards_index'), name='logout'),
                  path('upload_image/', upload_image, name='upload_image'),
                  path('profile/', views.profile, name='profile'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
