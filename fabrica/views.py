from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from .forms import TareaForm, FabricaForm, EstadoForm, CostureraForm, Costureras, CustomAuthenticationForm
from .models import Tareas
from .forms import CustomLoginForm


def contactanos(request):
    # Puedes agregar lógica adicional aquí si es necesario
    return render(request, 'contactanos.html')
  
def enviar_correo(request):
    if request.method == 'POST':
        # Procesar el formulario y enviar el correo electrónico
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')

        # Lógica para enviar el correo electrónico
        send_mail(
            'Mensaje de contacto',
            f'Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}',
            'tu_correo@example.com',
            ['destinatario@example.com'],
            fail_silently=False,
        )

        # Redirigir o mostrar un mensaje de éxito
        return render(request, 'exito.html')

    # Si el método de la solicitud no es POST, redirigir o manejarlo de otra manera
    return render(request, 'error.html')

def index(request):
    # Aquí puedes incluir cualquier lógica necesaria para la página de inicio
    # Por ejemplo, recuperar datos de la base de datos, procesar formularios, etc.
    return render(request, 'index.html')  # Renderiza la plantilla index.html

def crear_costurera(request):
    if request.method == 'POST':
        form = CostureraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_costurera')
    else:
        form = CostureraForm()

    return render(request, 'crear_costurera.html', {'form': form})

def modificar_costurera(request, identificacion):
    costurera = get_object_or_404(Costureras, identificacion=identificacion)

    if request.method == 'POST':
        form = CostureraForm(request.POST, instance=costurera)
        if form.is_valid():
            form.save()
            return redirect('listar_costureras')
    else:
        form = CostureraForm(instance=costurera)

    return render(request, 'modificar_costurera.html', {'form': form, 'costurera': costurera})

def listar_costureras(request):
    costureras = Costureras.objects.all()
    return render(request, 'listar_costureras.html', {'costureras': costureras})
  
def eliminar_costurera(request, identificacion):
    costurera = get_object_or_404(Costureras, identificacion=identificacion)
    if request.method == 'POST':
        costurera.delete()
    return render(request, 'eliminar_costurera.html', {'costurera': costurera})

def crear_fabrica(request):
    if request.method == 'POST':
        form = FabricaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Se creó la fábrica")
    else:
        form = FabricaForm()
    return render(request, 'crear_fabrica.html', {'form': form})

def crear_estado(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EstadoForm()
    return render(request, 'crear_estado.html', {'form': form})

def lista_tareas(request):
    tareas = Tareas.objects.all()
    return render(request, 'lista_tareas.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'crear_tarea.html', {'form': form})

def detalle_tarea(request, id):
    tarea = get_object_or_404(Tareas, id=id)
    return render(request, 'detalle_tarea.html', {'tarea': tarea})

def modificar_tarea(request, id):
    tarea = get_object_or_404(Tareas, id=id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'modificar_tarea.html', {'form': form})  

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tareas, id=id)
    tarea.delete()
    return redirect('lista_tareas')

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Nombre de la plantilla de inicio de sesión personalizada

    def form_valid(self, form):
        # Llama al método form_valid() de la clase base para realizar la autenticación
        super().form_valid(form)
        # Redirige al index.html después de la autenticación exitosa
        return redirect('index')


