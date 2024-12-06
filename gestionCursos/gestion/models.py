
from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()

    def __str__(self):
        return self.nombre
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cursos = models.ManyToManyField(Curso, related_name='estudiantes')

    def __str__(self):
        return self.nombre        