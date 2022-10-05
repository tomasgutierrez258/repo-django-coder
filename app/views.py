from django.http import HttpResponse
from datetime import datetime
from django.template import Context,Template,loader
import random

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
    cargar_archivo = open(r"D:\Develop\python-projects\prj-django-coder\templates\mi_template.html","r")
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

    template = loader.get_template("tu_template.html")
    template_renderizado = template.render({"persona" : nombre})

    return HttpResponse(template_renderizado)



def prueba_template(request):
    template = loader.get_template("prueba_template.html")
    context = {
        "rango" : list(range(1,11)),
        "random_number" : random.randrange(1,11)
    }

    template_renderizado = template.render(context)
    return HttpResponse(template_renderizado)


def crear_persona(request,nombre,apellido):
    persona = Persona(nombre = nombre,apellido = apellido,edad = random.randrange(1,99),fecha_nacimiento = datetime.now())
    persona.save()
    
    template = loader.get_template("crear_persona.html")
    template_renderizado = template.render({"persona" : persona})

    return HttpResponse(template_renderizado)

def ver_personas(request):
    personas = Persona.objects.all()

    template = loader.get_template("ver_personas.html")
    template_renderizado = template.render({"personas" : personas})
    return HttpResponse(template_renderizado)