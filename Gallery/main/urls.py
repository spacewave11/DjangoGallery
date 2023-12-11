from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  path('', views.index, name='home'),
                  path('image/<int:image_number>/', views.image_detail, name='main_image_detail'),
                  path('top_authors/', views.top_authors, name='top_authors'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)