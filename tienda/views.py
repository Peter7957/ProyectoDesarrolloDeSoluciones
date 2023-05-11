from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
    return render(request, "templateHTML/Home/Home.html")

def bodega(request):
    return render(request, "templateHTML/Bodega/Bodega.html")

def producto(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, "templateHTML/Producto/Producto.html", data)

