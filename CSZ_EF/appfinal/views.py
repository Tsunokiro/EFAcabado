from django.shortcuts import render

# Create your views here.
def ruta_integrantes(request):
    return render (request, "integrantes.html")

def ruta_inicio (request):
    return render (request, "inicio.html")

def saludo(request):
    
    return render (request, "saludo.html")