from django import forms

class ClienteForm(forms.Form):
    razon_social = forms.CharField(label="Razon social", max_length=100)
    id_cliente = forms.CharField(label="Id_cliente", max_length=100)
    #widget=forms.TextInput(attrs={'placeholder': '1234'})
    #widget es para poder agregar un tip para que el usuario sepa como ingresar el valor

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField()

class EquipoForm(forms.Form):
    equipo = forms.CharField(label="Equipo", max_length=100)
    serie = forms.CharField(label="Serie", max_length=100)