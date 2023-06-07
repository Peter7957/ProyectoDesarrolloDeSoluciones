from django.shortcuts import render,redirect, get_object_or_404
from .models import Producto, CustomUser
from .forms import ProductoForm , CustomUserCreationForm
from django.contrib import messages


from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import CustomUser

# Create your views here.

def home(request):
    return render(request, "Home/Home.html")

def bodega(request):
    return render(request, "Bodega/Bodega.html")

def cliente(request):
    return render(request, "Cliente/Cliente.html")

def producto(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, "Producto/Producto.html", data)


def detalles(request, producto_id):
    #INVESTIGAR ACERCA DE ESTA OPCION
    #producto = get_object_or_404(Producto, id=producto_id)
    producto = Producto.objects.get(id=producto_id)
    data = {'producto' : producto}
    
    return render(request, "Producto/Detalles.html", data)

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
    return render(request, "Admin/Agregar.html", data)

def listar_productos(request):
    producto = Producto.objects.all()
    data = {
        "producto" : producto
    }
    return render(request, "Admin/Listar.html", data)

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
    return render(request, "Admin/Modificar.html", data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id) 
    producto.delete()
    return redirect(to="listar_productos")

def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro Completo")
            return redirect(to="Home")
        data["form"] =formulario
    return render(request, 'registration/Registro.html', data)

class LoginCustom(LoginView):
    template_name = 'registration/login.html'


    def get_success_url(self):
        custom_user = CustomUser.objects.get(username=self.request.user.username)
        custom_user = self.request.user
        if hasattr(custom_user, 'perfil'): 
            if custom_user.perfil == 'administrador':
                return '/admin/'
            elif custom_user.perfil == 'cliente':
                return '/Cliente/'
            elif custom_user.perfil == 'bodeguero':
                return '/Bodeguero/'
        return '/Bodeguero'
        
    
    #def form_valid(self, form):
    #    if not self.request.user.is_active:
    #        return redirect('inactive-account')
    #    return super().form_valid(form)

#class CustomUserCreationView(CreateView):
#    template_name = 'registration/Registro.html'
#    model = CustomUser
#    form_class = CustomUserCreationForm
#    
#
#    def get_success_url(self):
#        success_url = super().get_success_url()
#        print(success_url)
#        return success_url
#    
#    def form_valid(self, form):
#        response = super().form_valid(form)
#        messages.success(self.request, 'Conexión exitosa. ¡Bienvenido!')
#        return response