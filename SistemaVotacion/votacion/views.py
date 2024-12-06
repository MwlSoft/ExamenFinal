from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Encuesta, Opcion
from .serializers import EncuestaSerializer, OpcionSerializer

class EncuestaViewSet(viewsets.ModelViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer

    @action(detail=True, methods=['post'])
    def votar(self, request, pk=None):
        encuesta = self.get_object()
        opcion_id = request.data.get('opcion_id')
        try:
            opcion = Opcion.objects.get(id=opcion_id, encuesta=encuesta)
            opcion.votos += 1
            opcion.save()
            return Response({'message': 'Voto registrado', 'opcion': OpcionSerializer(opcion).data})
        except Opcion.DoesNotExist:
            return Response({'error': 'Opción no válida'}, status=400)

def lista_encuestas(request):
    encuestas = Encuesta.objects.all()
    return render(request, 'votacion/lista_encuestas.html', {'encuestas': encuestas})