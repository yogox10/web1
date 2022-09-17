#from xml.dom.minidom import Document
#from django.template import Template, Context
#import pathlib

from django.http import HttpResponse
from django.template import loader

from AppCoder.models import Curso

def home(self,name):
    return HttpResponse(f"Hola soy {name}")

def homePage(self):
    lista = [1,2,3,4,5,6,7,8,9]
    data = {"nombre":"Diego","apellido":"Matta","lista":lista}
    planilla = loader.get_template("home.html")
    documento = planilla.render(data)
    return HttpResponse(documento)

def cursos(self):
    #planilla = loader.get_template('cursos.html')
    curso = Curso(nombre="UX/UI", camada="12345")
    curso.save()
    documento = f'Curso: {curso.nombre} camada: {curso.camada}'
    return HttpResponse(documento)


#path = pathlib.Path(__file__).parent.resolve()

#def saludo(request):
#    return HttpResponse("Hola Mundo")

#def segunda_vista(request):
#    return HttpResponse('<div style="background-color: blue; width: 100%; height: 100%; position: absolute; color: white; border : 0px; margin: 0px">Hola equipo coder</div>')

#def miNombre(self,nombre):
#    documentoTexto = f"Mi nombre es {nombre}"
#    return HttpResponse(documentoTexto)

#def template(self):
#    Mihtml = open (f"{path}/template/index.html")
#    planilla = Template(Mihtml.read())
#   Mihtml.close()
#    miContexto = Context()
#    documento = planilla.render(miContexto)
#    return HttpResponse(documento)


