from django.http import HttpResponse
from datetime import datetime
from django.template import Context,Template,loader
from django.shortcuts import render,redirect
import random
from home.forms  import PersonaFormularios
from home.forms  import BuequedaPersonaFormularios
from home.models import Persona

def hola(request):
    return HttpResponse("<h1>Hola</h1>")

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f"La fecha actual es {fecha_actual}")

def calcular_fecha(request,edad):

    fecha = datetime.now().year - edad
    return HttpResponse(f"tu fecha de nacimiento para tus {edad} es {fecha}")

def mi_template(request):
    cargar_archivo = open(r"D:\Develop\python-projects\prj-django-coder\templates\home\mi_template.html","r")
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)



def tu_template(request,nombre):
    # cargar_archivo = open(r"D:\Develop\python-projects\prj-django-coder\templates\tu_template.html","r")
    # template = Template(cargar_archivo.read())
    # cargar_archivo.close()
    # contexto = Context({"persona" : nombre}) #se usa para pasar contenido al template
    # template_renderizado = template.render(contexto)

    template = loader.get_template("home/tu_template.html")
    template_renderizado = template.render({"persona" : nombre})

    return HttpResponse(template_renderizado)



def prueba_template(request):
    template = loader.get_template("home/prueba_template.html")
    context = {
        "rango" : list(range(1,11)),
        "random_number" : random.randrange(1,11)
    }

    template_renderizado = template.render(context)
    return HttpResponse(template_renderizado)


def crear_persona(request):
    if request.method == "POST":
        
        formulario = PersonaFormularios(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_nacimiento = data.get('fecha_nacimiento',datetime.now())
            
            persona = Persona(nombre = nombre,apellido = apellido,edad = edad,fecha_nacimiento = fecha_nacimiento)
            persona.save()
            return redirect("ver_personas")
    
    formulario = PersonaFormularios()
    return render(request, "home/crear_persona.html", {"formulario":formulario})

def ver_personas(request):
    nombre = request.GET.get('nombre',None)
    
    if nombre:
        personas = Persona.objects.filter(nombre__icontains=nombre)
    else:
        personas = Persona.objects.all()
    
    formulario = BuequedaPersonaFormularios()
    return render(request, "home/ver_personas.html", {"personas" : personas ,"formulario":formulario})

def index(request):
    return render(request, "home/index.html")