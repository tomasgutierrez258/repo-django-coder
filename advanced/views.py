from django.shortcuts import render,redirect
from advanced.models import Mascota
from advanced.forms import MascotaFormulario
from django.contrib.auth.mixins import LoginRequiredMixin #limita al usuario a acceder a ciertas paginas
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.
def ver_mascotas(request):
    
    mascotas = Mascota.objects.all()
    return render(request, 'advanced/ver_mascotas.html', {'mascotas':mascotas})

@login_required
def crear_mascota(request):
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            mascota = Mascota(nombre=data['nombre'],
                              tipo=data['tipo'],
                              edad=data['edad'],
                              fecha_nacimiento=data['fecha_nacimiento'])
            mascota.save()
            return redirect('ver_mascotas')
        else:
            return render(request, 'advanced/crear_mascota.html', {'formulario':formulario})
    formulario = MascotaFormulario()
    return render(request, 'advanced/crear_mascota.html', {'formulario':formulario})

def editar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            mascota.nombre = data['nombre']
            mascota.tipo = data['tipo']
            mascota.edad = data['edad']
            mascota.fecha_nacimiento = data['fecha_nacimiento']
            mascota.save()
            
            return redirect('ver_mascotas')
        else:
            return render(request, 'advanced/editar_mascota.html', {'formulario':formulario})
        
    formulario = MascotaFormulario(
        initial = {
            'nombre' : mascota.nombre,
            'tipo' : mascota.tipo,
            'edad' : mascota.edad,
            'fecha_nacimiento' : mascota.fecha_nacimiento})
    return render(request, 'advanced/editar_mascota.html', {'formulario':formulario, 'mascota':mascota})

def eliminar_mascota(request,id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('ver_mascotas')

class ListaMascotas(ListView):
    model = Mascota
    template_name = 'advanced/ver_mascotas_cbv.html'

class CrearMascotas(CreateView):
    #createview por defecto crea un formulario
    model = Mascota
    success_url = '/advanced/mascotas/'
    template_name = 'advanced/crear_mascota_cbv.html'
    fields = ['nombre','tipo','edad','fecha_nacimiento']
    
class EditarMascotas(LoginRequiredMixin,UpdateView):
    model = Mascota
    success_url = '/advanced/mascotas/'
    template_name = 'advanced/editar_mascota_cbv.html'
    fields = ['nombre','tipo','edad','fecha_nacimiento']
    

class EliminarMascotas(LoginRequiredMixin,DeleteView):
    model = Mascota
    success_url = '/advanced/mascotas/'
    template_name = 'advanced/eliminar_mascota_cbv.html'

# class VerMascotas():