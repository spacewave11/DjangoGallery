from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  path('', views.index, name='cards_index'),
                  path('image/<int:image_id>/', views.image_detail, name='cards_image_detail'),
                  path('image/<int:image_id>/download/', views.download_image, name='download_image'),
                  path('image/<int:image_id>/delete_image/', views.delete_image, name='delete_image'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
