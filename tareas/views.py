from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm


def home(request):
    """Vista principal que lista todas las tareas."""
    tareas = Tarea.objects.all().order_by('-fecha_creacion')
    return render(request, "tareas/home.html", {'tareas': tareas})


def lista_tareas(request):
    """Lista todas las tareas."""
    tareas = Tarea.objects.all().order_by('-fecha_creacion')
    return render(request, "tareas/home.html", {'tareas': tareas})


def detalle_tarea(request, pk):
    """Muestra el detalle de una tarea específica."""
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, "tareas/tarea_detail.html", {'tarea': tarea})


def crear_tarea(request):
    """Crea una nueva tarea."""
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    return render(request, "tareas/tarea_form.html", {'form': form, 'titulo': 'Crear Tarea'})


def editar_tarea(request, pk):
    """Edita una tarea."""
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm(instance=tarea)
    return render(request, "tareas/tarea_form.html", {'form': form, 'titulo': 'Editar Tarea'})


def eliminar_tarea(request, pk):
    """Elimina una tarea."""
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect('home')
    return render(request, "tareas/tarea_confirm_delete.html", {'tarea': tarea})

