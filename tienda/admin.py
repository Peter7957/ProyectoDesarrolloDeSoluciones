from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import *
from .forms import CustomUserAdminForm

# Register your models here.

#class CustomUserAdmin(admin.ModelAdmin):
#    form = CustomUserAdminForm

class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('perfil',)}),
    )

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "marca"]
    search_fields   = ["nombre"]
    list_filter     = ["marca"]
    list_per_page   = 5

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'perfil']

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Marca)
admin.site.register(Aro)
admin.site.register(Genero)
admin.site.register(Producto,ProductoAdmin)