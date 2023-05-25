from django.shortcuts import render
from .models import Producto
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        Usuario = request.POST['Usuario']
        Contraseña = request.POST['Contraseña']
        user = authenticate(request, Usuario=Usuario, Contraseña=Contraseña)
        if Usuario is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio
        else:
            error_message = 'Usuario o contraseña incorrecta.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        Usuario = request.POST['Usuario']
        Contraseña = request.POST['Contraseña']
        confirme_Contraseña = request.POST['confirme_Contraseña']
        if Contraseña == confirme_Contraseña:
            Usuario = Usuario.objects.create_user(Usuario=Usuario, Contraseña=Contraseña)
            login(request, Usuario)
            return redirect('home')  # Redirige a la página de inicio
        else:
            error_message = 'Contraseña incorrecta.'
            return render(request, 'signup.html', {'error_message': error_message})
    else:
        return render(request, 'signup.html')


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
    print(producto)
    
    return render(request, "templateHTML/Producto/Detalles.html", {'producto' : producto})
