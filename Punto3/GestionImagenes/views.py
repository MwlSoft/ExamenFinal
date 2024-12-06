from django.shortcuts import render, redirect, get_object_or_404
from .models import Imagen

# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        archivo = request.FILES['archivo']
        Imagen.objects.create(titulo=titulo, descripcion=descripcion, archivo=archivo)
        return redirect('gallery')
    return render(request, 'upload.html')

def gallery(request):
    imagenes = Imagen.objects.all()
    return render(request, 'gallery.html', {'imagenes': imagenes})

def delete_image(request, id):
    imagen = get_object_or_404(Imagen, id=id)
    imagen.delete()
    return redirect('gallery')