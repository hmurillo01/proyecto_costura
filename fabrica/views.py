from django.shortcuts import render, redirect, get_object_or_404
from .models import Tareas
from django.http import HttpResponse
from django.contrib import messages 
from .forms import TareaForm,FabricaForm,CostureraForm


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

def crear_fabrica(request):
    if request.method == 'POST':
        form = FabricaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fabricas')
    else:
        form = FabricaForm()
    return render(request, 'crear_fabrica.html', {'form': form})

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
            return redirect('detalle_tarea', id=id)
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'modificar_tarea.html', {'form': form})

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tareas, id=id)
    tarea.delete()
    return redirect('lista_tareas')
  


