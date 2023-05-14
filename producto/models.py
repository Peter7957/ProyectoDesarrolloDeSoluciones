from django.db import models

# Create your models here.

class Producto(models.Model):
    NomProducto = models.CharField(max_length=30)
