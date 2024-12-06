from django.db import models
from django.db import models

class Encuesta(models.Model):
    pregunta = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pregunta
class Opcion(models.Model):
    texto = models.CharField(max_length=255)
    votos = models.IntegerField(default=0)
    encuesta = models.ForeignKey(Encuesta, related_name='opciones', on_delete=models.CASCADE)

    def __str__(self):
        return self.texto     
        
           