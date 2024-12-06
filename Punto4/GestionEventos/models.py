from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Participante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    evento = models.ForeignKey(Evento, related_name='participantes', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    