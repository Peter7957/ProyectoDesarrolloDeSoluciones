from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "marca"]
    search_fields   = ["nombre"]
    list_filter     = ["marca"]
    list_per_page   = 5

admin.site.register(Marca)
admin.site.register(Aro)
admin.site.register(Genero)
admin.site.register(Producto,ProductoAdmin)