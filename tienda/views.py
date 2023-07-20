from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
import json
from .models import Producto, CustomUser, Modelo, Marca, Aro, Genero, Carrito, ItemCarrito
from .forms import ProductoForm, MarcaForm, ModeloForm, GeneroForm, AroForm,  CustomUserCreationForm
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView

from .models import CustomUser

#Rutas 
def home(request):
    producto = Producto.objects.order_by('-id')[:6]
    data ={
        "productos": producto,
    }
    return render(request, "Home/Home.html", data)

def bodega(request):
    return render(request, "Bodega/Bodega.html")

def pago(request):
    return render(request, "Producto/Pago.html")

def cliente(request):
    return render(request, "Cliente/Cliente.html")

def administrador(request):
    return render(request, "Admin/Administrador.html")

def producto(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos,
    }
    return render(request, "Producto/Producto.html", data)

def buscar_productos(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        print(query)

        if query:
            palabras = query.split()
            q_lookup = Q()
            for palabra in palabras:
                q_lookup |= Q(nombre__icontains=palabra.lower())
                print(q_lookup)
            productos = Producto.objects.filter(q_lookup)
        else:
            productos = Producto.objects.all()

    context = {
        'productos': productos,
        'query': query
    }
    return render(request, 'Producto/buscar_productos.html', context)


    

def detalles(request, producto_id):
    #INVESTIGAR ACERCA DE ESTA OPCION
    #producto = get_object_or_404(Producto, id=producto_id)
    producto = Producto.objects.get(id=producto_id)
    data = {'producto' : producto}
    
    return render(request, "Producto/Detalles.html", data)


#CRUD Administrador 
def agregar_producto(request, filtro):
    if(filtro == 'producto'):

        data = {
        'form' : ProductoForm(),
        'title' : filtro 
        }

        if request.method == 'POST':
            formulario = ProductoForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "guardado correctamente"
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"

    elif(filtro == 'marca'):
            
        data = {
        'form' : MarcaForm(),
        'title' : filtro 
        }

        if request.method == 'POST':
            formulario = MarcaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "guardado correctamente"
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"
        
    elif(filtro == 'modelo'):
        
        data = {
        'form' : ModeloForm(),
        'title' : filtro 
        }

        if request.method == 'POST':
            formulario = ModeloForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "guardado correctamente"
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"

    elif(filtro == 'genero'):
            
        data = {
        'form' : GeneroForm(),
        'title' : filtro 

        }

        if request.method == 'POST':
            formulario = GeneroForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "guardado correctamente"
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"

    elif(filtro == 'aro'):
            
        data = {
        'form' : AroForm(),
        'title' : filtro 
        }

        if request.method == 'POST':
            formulario = AroForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "guardado correctamente"
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"
    return render(request, "Admin/Agregar.html", data)

def listar_productos(request, filtro):
    if(filtro == 'producto'):
        producto = Producto.objects.all()
        template = 'Admin/Listar/Listar_Producto.html'
        data = {
            "producto" : producto,
            "title" : filtro
        }
    elif(filtro == 'marca'):
        producto = Marca.objects.all()
        template = 'Admin/Listar/Listar_Marca.html'
        data = {
            "producto" : producto,
            "title" : filtro
        }
    elif(filtro == 'modelo'):
        producto = Modelo.objects.all()
        template = 'Admin/Listar/Listar_Modelo.html'
        data = {
            "producto" : producto,
            "title" : filtro
        }
    elif(filtro == 'genero'):
        producto = Genero.objects.all()
        template = 'Admin/Listar/Listar_Genero.html'
        data = {
            "producto" : producto,
            "title" : filtro
        }
    elif(filtro == 'aro'):
        producto = Aro.objects.all()
        template = 'Admin/Listar/Listar_Aro.html'
        data = {
            "producto" : producto,
            "title" : filtro
        }
    return render(request, template, data)

def modificar_producto(request,filtro, id):
    if(filtro == 'producto'):
        producto = get_object_or_404(Producto, id=id)
        data = {
            'form' : ProductoForm(instance=producto)
        }

        if request.method == 'POST':
            formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect(to="listar_productos", filtro=filtro)
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"
    
    elif(filtro == 'marca'):
        producto = get_object_or_404(Marca, id=id)
        data = {
            'form' : MarcaForm(instance=producto)
        }

        if request.method == 'POST':
            formulario = MarcaForm(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect(to="listar_productos", filtro=filtro)
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"

    elif(filtro == 'modelo'):
        producto = get_object_or_404(Modelo, id=id)
        data = {
            'form' : ModeloForm(instance=producto)
        }

        if request.method == 'POST':
            formulario = ModeloForm(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect(to="listar_productos", filtro=filtro)
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"
    
    elif(filtro == 'genero'):
        producto = get_object_or_404(Genero, id=id)
        data = {
            'form' : GeneroForm(instance=producto)
        }

        if request.method == 'POST':
            formulario = GeneroForm(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect(to="listar_productos", filtro=filtro)
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"
    
    elif(filtro == 'aro'):
        producto = get_object_or_404(Aro, id=id)
        data = {
            'form' : AroForm(instance=producto)
        }

        if request.method == 'POST':
            formulario = AroForm(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect(to="listar_productos", filtro=filtro)
            else:
                data["form"] = formulario
                data["mensaje"] = "Error"
    return render(request, "Admin/Modificar.html", data)

def eliminar_producto(request, filtro, id):
    if(filtro == 'producto'):
        producto = get_object_or_404(Producto, id=id) 
        producto.delete()
        return redirect(to="listar_productos", filtro=filtro)
    
    elif(filtro == 'marca'):
        producto = get_object_or_404(Marca, id=id) 
        producto.delete()
        return redirect(to="listar_productos", filtro=filtro)
    
    elif(filtro == 'modelo'):
        producto = get_object_or_404(Modelo, id=id) 
        producto.delete()
        return redirect(to="listar_productos", filtro=filtro)
    
    elif(filtro == 'genero'):
        producto = get_object_or_404(Genero, id=id) 
        producto.delete()
        return redirect(to="listar_productos", filtro=filtro)
    
    elif(filtro == 'aro'):
        producto = get_object_or_404(Aro, id=id) 
        producto.delete()
        return redirect(to="listar_productos", filtro=filtro)


def carrito(request):
    return render(request, "Producto/Carrito.html")

#Registros e Inicio de sesión
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
                return '/Administrador/'
            elif custom_user.perfil == 'cliente':
                return '/Cliente/'
            elif custom_user.perfil == 'bodeguero':
                return '/Bodega/'
        return '/'
        
def filtro(request, filtro):
    if(filtro == 'marca'):
        filtrar = Marca.objects.all()
    elif(filtro == 'modelo'):
        filtrar = Modelo.objects.all()
    elif(filtro == 'aro'):
        filtrar = Aro.objects.all()
    elif(filtro == 'genero'):
        filtrar = Genero.objects.all()
    
    data = {
        'filtrar': filtrar
    }
    return render(request, "Producto/Filtro.html", data)

def categoria(request, id):
    #producto = Producto.objects.get(id=id_categoria)
    #f = filtro.lower()
    #print(f)
    productos = Producto.objects.filter(marca_id=id)
    data = {'productos' : productos}

    return render(request, "Producto/Categoria.html", data)


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item, _ = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    item.cantidad += 1
    item.save()
    return redirect('carrito')

@login_required
def mostrar_carrito(request):
    try:
        carrito = Carrito.objects.get(usuario=request.user)
    except Carrito.DoesNotExist:
        carrito = None

    if carrito is None:
        carrito = Carrito.objects.create(usuario=request.user)


    items_carrito = carrito.itemcarrito_set.all()

    total = 0
    for item in items_carrito:
        subtotal = item.producto.precio * item.cantidad
        total += subtotal

    context = {
        'items_carrito': items_carrito,
        'total': total,
    }

    return render(request, 'Producto/CarritoLog.html', context)

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    item.delete()
    return redirect('carrito')

@login_required
def actualizar_cantidad(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    nueva_cantidad = int(request.POST.get('cantidad'))
    if nueva_cantidad > 0:
        item.cantidad = nueva_cantidad
        item.save()
    else:
        item.delete()
    return redirect('carrito')
