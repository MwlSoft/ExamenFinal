from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EncuestaViewSet, lista_encuestas

router = DefaultRouter()
router.register(r'encuestas', EncuestaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('encuestas/lista/', lista_encuestas, name='lista_encuestas'),
]