from django.urls import path
from . import views

urlpatterns = [
    path('crear_reserva/', views.crear_reserva, name='crear_reserva'),
    path('listar_reservas/', views.listar_reservas, name='listar_reservas'),
    path('cancelar_reserva/<pk>/', views.cancelar_reserva, name='cancelar_reserva'),
    path('calendario_reservas/', views.calendario_reservas, name='calendario_reservas'),
]