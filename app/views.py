from django.http import HttpResponse
from datetime import datetime
from django.template import Context,Template

def hola(request):
    return HttpResponse("<h1>Hola</h1>")

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f"La fecha actual es {fecha_actual}")

def calcular_fecha(request,edad):

    fecha = datetime.now().year - edad
    return HttpResponse(f"tu fecha de nacimiento para tus {edad} es {fecha}")

def mi_template(request):
    cargar_archivo = open(r"D:\Develop\python-projects\prj-django-coder\templates\template.html","r")
    template = Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)