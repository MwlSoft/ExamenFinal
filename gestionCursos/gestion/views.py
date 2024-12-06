
from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Estudiante
from .forms import EstudianteForm

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos': cursos})

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    estudiantes = curso.estudiantes.all()

    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = form.save()
            curso.estudiantes.add(estudiante)
            return redirect('detalle_curso', curso_id=curso.id)
    else:
        form = EstudianteForm()

    return render(request, 'detalle_curso.html', {'curso': curso, 'estudiantes': estudiantes, 'form': form})
    