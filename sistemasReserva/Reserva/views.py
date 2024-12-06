from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mesa, Reserva
from .forms import ReservaForm

def crear_reserva(request):
    mesas = Mesa.objects.filter(disponibilidad=True)  
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            mesa_id = form.cleaned_data['mesa']  
            if not Mesa.objects.filter(id=mesa_id, disponibilidad=True).exists():
                return HttpResponse('Mesa no disponible', status=400)
            reserva = form.save(commit=False)  
            reserva.mesa = Mesa.objects.get(id=mesa_id) 
            reserva.save()  
            return redirect('listar_reservas')
    else:
        form = ReservaForm()
    return render(request, 'crear_reserva.html', {'form': form, 'mesas': mesas})

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'listar_reservas.html', {'reservas': reservas})

def cancelar_reserva(request, pk):
    reserva = Reserva.objects.get(pk=pk)
    reserva.delete()
    return redirect('listar_reservas')
from django.shortcuts import render
from .models import Reserva

def calendario_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'calendario_reservas.html', {'reservas': reservas})    