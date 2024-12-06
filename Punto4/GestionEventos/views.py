from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Participante
from .forms import ParticipanteForm
# Create your views here.

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/listar_eventos.html', {'eventos': eventos})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    participantes = evento.participantes.all()
    
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            participante = form.save(commit=False)
            participante.evento = evento
            participante.save()
            return redirect('detalle_evento', evento_id=evento.id)
    else:
        form = ParticipanteForm()
    
    return render(request, 'eventos/detalle_evento.html', {
        'evento': evento,
        'participantes': participantes,
        'form': form,
    })