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
    path('Filtro/<str:filtro>', views.filtro, name="filtro"),
    path('Categoria/<int:id>/', views.categoria, name='categoria'),
    path('Buscar/', views.buscar_productos, name="buscar_productos"),
    path('Detalles/<int:producto_id>/', views.detalles, name='detalles'),
    path('Bodega/', views.bodega , name='Bodeguero'),
    path('Cliente/', views.cliente, name='Cliente'),
    path('Administrador/', views.administrador, name='Admin'),
    path('Pago/', views.pago, name='Pago'),
    path('Factura/', views.factura, name='factura'),
    path('DetallesFactura/<int:factura_id>', views.detalle_factura, name='detalle_factura'),

    #Rutas para el Crud que tendra django (Actualemente pueden tener cambios segun se requiera)
    path('Agregar-Producto/<str:filtro>/', views.agregar_producto, name='agregar_producto'),
    path('Listar-Producto/<str:filtro>/', views.listar_productos, name='listar_productos'),
    path('Modificar-Producto/<str:filtro>/<id>/', views.modificar_producto, name='modificar_producto'),
    path('Eliminar-Producto/<str:filtro>/<id>/', views.eliminar_producto, name='eliminar_producto'),

    #Rutas para el Crud que tendra django carrito (Actualemente pueden tener cambios segun se requiera)
    #path('Agregar/<int:producto_id>/', views.agregar_producto_carrito, name='agregar_producto_carrito'),
    #path('Restar/<int:producto_id>/', views.restar_producto_carrito, name='restar_producto_carrito'),
    #path('Limpiar/', views.limpiar_producto_carrito, name='limpiar_producto_carrito'),
    #path('Eliminar/<int:producto_id>/', views.eliminar_producto_carrito, name='eliminar_producto_carrito'),

    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_producto_carrito'),
    path('Carrito/', views.mostrar_carrito, name='carrito'),
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('actualizar/<int:item_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),

    #Ruta para el Login (este esta conectado con la ruta templates/login.html) y no require de views.py 
    #se importa directamente de 'django.contrib.auth.urls' 
    path('accounts/', include('django.contrib.auth.urls')),
    path('Registro/', views.registro, name='registro'),
    path('login/', views.LoginCustom.as_view(), name='login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.IMG_URL, document_root=settings.IMG_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)