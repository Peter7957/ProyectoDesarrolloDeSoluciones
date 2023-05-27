"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tienda import views


#metodo para guardar imagenes, solo sirve en DEBUG
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Ruta para ingresar al administrador de django
    path('admin/', admin.site.urls),

    #Rutas generales vinculadas al navbar
    path('', views.home, name="Home"),
    path('Producto/', views.producto, name="Producto"),
    path('Detalles/<int:producto_id>/', views.detalles, name='detalles'),
    path('Bodega/', views.bodega),

    #Rutas para el Crud que tendra django (Actualemente pueden tener cambios segun se requiera)
    path('Agregar-Producto/', views.agregar_producto, name='agregar_producto'),
    path('Listar-Producto/', views.listar_productos, name='listar_productos'),
    path('Modificar-Producto/<id>/', views.modificar_producto, name='modificar_producto'),
    path('Eliminar-Producto/<id>/', views.eliminar_producto, name='eliminar_producto'),

    #Ruta para el Login (este esta conectado con la ruta templates/login.html) y no require de views.py 
    #se importa directamente de 'django.contrib.auth.urls' 
    path('accounts/', include('django.contrib.auth.urls')),
    path('Registro/', views.registro, name='registro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)