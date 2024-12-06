from django.contrib import admin

from .models import Evento, Participante
# Register your models here.
admin.site.register(Evento)
admin.site.register(Participante)