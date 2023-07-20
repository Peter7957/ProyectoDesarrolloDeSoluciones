from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=350, null=True)
    imagen = models.ImageField(upload_to="Marca", null=True)
    ##Me permite ver el nombre cuando registre algo en el admin de django
    def __str__(self):
        return self.nombre
    
class Aro(models.Model):    
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=350, null=True)
    imagen = models.ImageField(upload_to="Aro", null=True)
    
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=350, null=True)
    imagen = models.ImageField(upload_to="Genero", null=True)
    
    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=340, null=True)
    imagen = models.ImageField(upload_to="Modelo", null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca,null=True, on_delete=models.SET_NULL)
    aro = models.ForeignKey(Aro,null=True,on_delete=models.SET_NULL)
    genero = models.ForeignKey(Genero,null=True,on_delete=models.SET_NULL)
    cantidad = models.IntegerField()
    modelo = models.ForeignKey(Modelo, null=True, on_delete=models.SET_NULL)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="Producto", null=True)
    
    def __str__(self):
        return self.nombre

class CustomUser(AbstractUser):
    Perfiles =(
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
        ('bodeguero', 'Bodeguero'),
    )

    perfil = models.CharField(max_length=15, choices=Perfiles,default='cliente')
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',  # Agregar related_name único
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',  # Agregar related_name único
        related_query_name='customuser'
    )

class Carrito(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ItemCarrito')

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

class Factura(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class ListaFacturas(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    facturas = models.ManyToManyField(Factura)