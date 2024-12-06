from django import forms
from .models import Reserva, Mesa

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'fecha_hora', 'mesa'] 
    
    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)
        self.fields['mesa'].queryset = Mesa.objects.filter(disponibilidad=True)  