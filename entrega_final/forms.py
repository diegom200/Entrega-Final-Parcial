from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class ClienteForm(forms.Form):
    razon_social = forms.CharField(label="Razon social", max_length=100)
    id_cliente = forms.CharField(label="Id_cliente", max_length=100)
    
class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField()

class EquipoForm(forms.Form):
    equipo = forms.CharField(label="Equipo", max_length=100)
    serie = forms.CharField(label="Serie", max_length=100)

class BuscarClienteForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")
    

class BuscarContactoForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class BuscarEquipoForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class ActualizarClienteForm(ClienteForm):
    id = forms.IntegerField(widget = forms.HiddenInput())

class ActualizarClienteForm(ClienteForm):
    id = forms.IntegerField(widget = forms.HiddenInput())

class ActualizarClienteForm(ClienteForm):
    id = forms.IntegerField(widget = forms.HiddenInput())


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasena')
    password2 = forms.CharField(label='Repetir a contrasena', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:''for k in fields}

