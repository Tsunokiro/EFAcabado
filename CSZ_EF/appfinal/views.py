from django.shortcuts import render
from appfinal.models import Producto
from appfinal.forms import ProductoForm

# Create your views here.
def ruta_integrantes(request):
    return render (request, "integrantes.html")

def ruta_inicio (request):
    return render (request, "inicio.html")

def saludo(request):
    
    return render (request, "saludo.html")

def crear_producto(request):
    data={
        'form': ProductoForm()
    }
    if request.method=='POST':
        formulario=ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Producto agregado exitosamente"
        else:
            data["form"]=formulario
    return render(request,'crear_producto.html',data)
