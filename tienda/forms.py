from django import forms
from .models import Producto, Marca, Modelo, Genero, Aro
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

UserMod = get_user_model()

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'

class AroForm(forms.ModelForm):
    class Meta:
        model = Aro
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    perfil = forms.ChoiceField(choices=(
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
        ('bodeguero', 'Bodeguero'),
    ), initial='cliente', widget=forms.HiddenInput())

    #staff = forms.BooleanField(label='Staff', required=False)


    class Meta:
        model = CustomUser
        fields = ["username",
        # "first_name", "last_name", "email"
        "password1", "password2", "perfil"]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['perfil'].initial = 'cliente'

class CustomUserAdminForm(UserChangeForm):
    perfil = forms.ChoiceField(choices=CustomUser.Perfiles)

    class Meta:
        model = CustomUser
        fields = '__all__'