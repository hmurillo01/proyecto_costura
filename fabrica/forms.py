from django import forms
from .models import Tareas,Fabrica,Costureras

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ['descripcion', 'cant_prendas', 'fecha_ini', 'fecha_fin', 'id_estado', 'id_fabrica', 'id_costurera']
        

class FabricaForm(forms.ModelForm):
    class Meta:
        model = Fabrica
        fields = ['nit', 'nombre', 'direccion', 'id_costura']
        
        
class CostureraForm(forms.ModelForm):
    class Meta:
        model = Costureras
        fields = ['identificacion', 'nombre', 'apellido', 'fecha_nacimiento', 'direccion']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }

def clean_identificacion(self):
        identificacion = self.cleaned_data['identificacion']
        if Costureras.objects.filter(identificacion=identificacion).exists():
            raise forms.ValidationError('Ya existe una costurera con este número de identificación.')
        return identificacion
        
