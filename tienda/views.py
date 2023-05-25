from django.shortcuts import render,redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


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


def detalles(request, producto_id):
    #INVESTIGAR ACERCA DE ESTA OPCION
    #producto = get_object_or_404(Producto, id=producto_id)
    producto = Producto.objects.get(id=producto_id)
    data = {'producto' : producto}
    
    return render(request, "templateHTML/Producto/Detalles.html", data)

def agregar_producto(request):
    
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
            data["mensaje"] = "Error"
    return render(request, "templateHTML/Admin/Agregar.html", data)

def listar_productos(request):
    producto = Producto.objects.all()
    data = {
        "producto" : producto
    }
    return render(request, "templateHTML/Admin/Listar.html", data)

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario
            data["mensaje"] = "Error"
    return render(request, "templateHTML/Admin/Modificar.html", data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_productos")
