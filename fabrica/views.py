from django.shortcuts import render, redirect, get_object_or_404
from .models import Tareas
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.views import LoginView
from .forms import TareaForm,FabricaForm,EstadoForm,CostureraForm, Costureras


class CustomLoginView(LoginView):
    template_name = 'login.html'  # Nombre de la plantilla de inicio de sesión personalizada

def crear_costurera(request):
    if request.method == 'POST':
        form = CostureraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Costurera creada con éxito!') 
            #return redirect('lista_costureras')
    else:
        form = CostureraForm()

    # Si el formulario se ha enviado con éxito o es una solicitud GET, 
    # renderiza un nuevo formulario limpio
    return render(request, 'crear_costurera.html', {'form': form})
  
def eliminar_costurera(request, identificacion):
    costurera = get_object_or_404(Costureras, identificacion=identificacion)
    if request.method == 'POST':
        costurera.delete()
      ## return redirect('lista_costureras')  # Redirige a la lista de costureras después de eliminar
    return render(request, 'eliminar_costurera.html', {'costurera': costurera})

def crear_fabrica(request):
    if request.method == 'POST':
        form = FabricaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fabricas')
    else:
        form = FabricaForm()
    return render(request, 'crear_fabrica.html', {'form': form})

def crear_estado(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página de éxito o a la lista de estados
           # return redirect('lista_estados')  # Ajusta 'lista_estados' a la URL de tu lista de estados
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
            return redirect('lista_tareas')  # Redireccionar a la lista de tareas
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'modificar_tarea.html', {'form': form})

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tareas, id=id)
    tarea.delete()
    return redirect('lista_tareas')


  


