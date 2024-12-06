from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/cursos/', permanent=True)),  # Redirige a /cursos/
    path('cursos/', include('gestion.urls')),
]