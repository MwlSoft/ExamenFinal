from django.contrib import admin
from .models import Mesa, Reserva

# Registra el modelo Mesa
@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'capacidad', 'disponibilidad')  # Campos a mostrar en la lista
    search_fields = ('numero',)  # Campo por el que se puede buscar

# Registra el modelo Reserva
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'fecha_hora', 'mesa')  # Campos a mostrar en la lista
    list_filter = ('fecha_hora',)  # Filtros disponibles en la lista
    search_fields = ('nombre_cliente',)  # Campo por el que se puede buscar