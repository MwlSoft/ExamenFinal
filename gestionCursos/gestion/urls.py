
from django.urls import path
from .views import listar_cursos, detalle_curso

urlpatterns = [
    path('cursos/', listar_cursos, name='listar_cursos'),
    path('cursos/<int:curso_id>/', detalle_curso, name='detalle_curso'),
]