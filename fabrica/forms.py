from django import forms
from .models import Tareas,Fabrica,Costureras,Estado
from django.contrib.auth.forms import AuthenticationForm

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = [ 'cant_prendas', 'fecha_ini', 'fecha_fin', 'estado', 'fabrica', 'costurera','descripcion']
        widgets =  {
        'cant_prendas': forms.NumberInput(attrs={'class': 'form-control bg-color', 'placeholder': 'Ingrese cantidad de prendas','autocomplete': 'off'}),
        'fecha_ini': forms.DateInput(attrs={'class': 'form-control bg-color', 'type': 'date'}),
        'fecha_fin': forms.DateInput(attrs={'class': 'form-control bg-color', 'type': 'date'}),
        'estado': forms.Select(attrs={'class': 'form-control bg-color'}),
        'fabrica': forms.Select(attrs={'class': 'form-control bg-color'}),
        'costurera': forms.Select(attrs={'class': 'form-control bg-color'}),
        'descripcion': forms.Textarea(attrs={'class': 'form-control bg-color','placeholder': 'Ingrese descripción bien detallada','autocomplete': 'off'})
        }
        
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_ini'].label = 'Fecha de inicio'
        self.fields['fecha_fin'].label = 'Fecha de finalización'
        self.fields['costurera'].label = 'Nombre de  costurera'
        self.fields['fabrica'].label = 'Nombre de la fábrica'
        

        

class FabricaForm(forms.ModelForm):
    class Meta:
        model = Fabrica
        fields = ['nit', 'nombre', 'direccion','costura']
        widgets = {
            'nit': forms.TextInput(attrs={'class': 'form-control','autocomplete': 'off', 'placeholder': 'Ingrese el NIT'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control','autocomplete': 'off', 'placeholder': 'Ingrese el nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control','autocomplete': 'off', 'placeholder': 'Ingrese la dirección'}),
            'costura': forms.Select(attrs={'class': 'form-control'}),
        
        }
    

        #En este código, estamos obteniendo el queryset con los nombres y apellidos de las costureras y 
        #luego formateando cada tupla como una cadena de "nombre apellido". 
        #Luego, establecemos estas cadenas formateadas como las opciones del campo "costura".
'''     def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      queryset = Costureras.objects.all().values_list('nombre', 'apellido')
      formatted_choices = [(f"{nombre} {apellido}", f"{nombre} {apellido}") for nombre, apellido in queryset]
      self.fields['costura'].choices = formatted_choices
 '''
class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nombre']
        widgets =  {
          'nombre':forms.TextInput(attrs={'autocomplete': 'off'})
        }

        
class CostureraForm(forms.ModelForm):
    class Meta:
        model = Costureras
        fields = ['identificacion', 'nombre', 'apellido','genero', 'fecha_nacimiento', 'direccion']
        widgets = {
            'identificacion': forms.TextInput(attrs={'class': 'form-control bg-color','autocomplete': 'off'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-color','autocomplete': 'off'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control bg-color','autocomplete': 'off'}),
            'genero': forms.Select(attrs={'class': 'form-control bg-color'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control bg-color', 'type': 'date'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control bg-color','autocomplete': 'off'}),
        }

# Agregamos un id al formulario
        attrs = {'id': 'costurera-form'}

    def clean_identificacion(self):
        identificacion = self.cleaned_data['identificacion']
        if Costureras.objects.filter(identificacion=identificacion).exists():
            raise forms.ValidationError('Ya existe una costurera con este número de identificación.')
        return identificacion 
    


class CustomAuthenticationForm(AuthenticationForm):
    identificacion = forms.CharField(label="Número de Identificación")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()  # Oculta el campo de nombre de usuario

    def clean(self):
        cleaned_data = super().clean()
        identificacion = cleaned_data.get('identificacion')
        if identificacion:
            try:
                costurera = Costureras.objects.get(identificacion=identificacion)
                cleaned_data['username'] = costurera.pk  # Utiliza el ID de la costurera como nombre de usuario
            except Costureras.DoesNotExist:
                raise forms.ValidationError("Número de identificación incorrecto.")
        return cleaned_data


class CustomLoginForm(forms.Form):
    identificacion = forms.CharField(label="Número de Identificación")

    def clean_identificacion(self):
        identificacion = self.cleaned_data.get('identificacion')
        if identificacion:
            try:
                costurera = Costureras.objects.get(identificacion=identificacion)
                return str(costurera.identificacion)  # Devuelve la identificación como cadena
            except Costureras.DoesNotExist:
                raise forms.ValidationError("Número de identificación incorrecto.")
        else:
            raise forms.ValidationError("Ingrese un número de identificación.")

