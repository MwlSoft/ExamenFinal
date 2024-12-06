from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from .views import upload_image, gallery, delete_image

urlpatterns = [
    path("admin/", admin.site.urls),
    path("upload/", upload_image, name='upload_image'),
    path("gallery/", gallery, name='gallery'),
    path("delete/<int:id>/", delete_image, name='delete_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)