from django.urls import path
from .views import listar_eventos, detalle_evento

urlpatterns = [
    path('', listar_eventos, name='listar_eventos'),
    path('evento/<int:evento_id>/', detalle_evento, name='detalle_evento'),
]