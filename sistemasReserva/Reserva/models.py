from django.db import models

class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    capacidad = models.IntegerField()
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return f'Mesa {self.numero} - Capacidad: {self.capacidad}'
class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)

    def __str__(self):
        return f'Reserva de {self.nombre_cliente} en {self.mesa} para {self.fecha_hora}'        