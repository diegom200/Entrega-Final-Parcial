from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class ClienteForm(forms.Form):
    razon_social = forms.CharField(label="Razon social", max_length=100)
    id_cliente = forms.CharField(label="Id_cliente", max_length=100)
    #widget=forms.TextInput(attrs={'placeholder': '1234'})
    #widget es para poder agrega
    # \
    #   1``123456
    # / un tip para que el usuario sepa como ingresar el valor

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField()
    fecha_creacion = models.DateField(auto_now_add=True)

class EquipoForm(forms.Form):
    equipo = forms.CharField(label="Equipo", max_length=100)
    serie = forms.CharField(label="Serie", max_length=100)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasena')
    password2 = forms.CharField(label='Repetir a contrasena', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:''for k in fields}

