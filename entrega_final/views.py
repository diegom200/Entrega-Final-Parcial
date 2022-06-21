
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from entrega_final.models import Cliente, Contacto, Equipo
from entrega_final.forms import ClienteForm, ContactoForm, EquipoForm, UserRegisterForm
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

def inicio(request):
    return render(request, 'plantillas_final/bienvenida.html/')

def agregar(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():

            razon_social = form.cleaned_data['razon_social']
            id_cliente = form.cleaned_data['id_cliente']
            Cliente(razon_social=razon_social, id_cliente=id_cliente).save()

            return HttpResponseRedirect('/entrega_final/')
    elif request.method == "GET":
        form = ClienteForm()
    else:
        return HttpResponseBadRequest("Error no conozco metodo")

    return render(request, 'plantillas_final/formulario.html', {'form':form})


def borrar(request, identificador):
   
    if request.method == "GET":
        cliente = Cliente.objects.filter(id=int(identificador)).first()
        if cliente:
            cliente.delete()
        return HttpResponseRedirect("/entrega_final/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")



def cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():

            razon_social = form.cleaned_data['razon_social']
            id_cliente = form.cleaned_data['id_cliente']
            Cliente(razon_social=razon_social, id_cliente=id_cliente).save()

            return HttpResponseRedirect('/entrega_final/')
    elif request.method == "GET":
        form = ClienteForm()
    else:
        return HttpResponseBadRequest("Error no conozco metodo")

    return render(request, 'plantillas_final/cliente.html', {'form':form})

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            Contacto(nombre=nombre, email=email).save()

            return HttpResponseRedirect('/entrega_final/')
    elif request.method == "GET":
        form = ContactoForm()
    else:
        return HttpResponseBadRequest("Error no conozco metodo")

    return render(request, 'plantillas_final/contacto.html', {'form':form})

def equipo(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():

            equipo = form.cleaned_data['equipo']
            serie = form.cleaned_data['serie']
            Equipo(equipo=equipo, serie=serie).save()

            return HttpResponseRedirect('/entrega_final/')
    elif request.method == "GET":
        form = EquipoForm()
    else:
        return HttpResponseBadRequest("Error no conozco metodo")

    return render(request, 'plantillas_final/equipo.html', {'form':form})

def formulario(request):
    return render(request,'plantillas_final/formulario.html')

def actualizar(request, identificador):
    pass

def busquedacliente(request):
    return render(request, 'plantillas_final/busquedacliente.html')

def buscar(request):
    if request.GET["id_client"]: 
        id_cliente = request.GET['id_cliente']
        cliente = cliente.objetcs.filter(id_cliente_icontains=id_cliente)

        return render(request, 'plantillas_final/resultadobusqueda.html', {"cliente":cliente, "id_cliente":id_cliente})

    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "plantillas_final/bienvenida.html", {"mensaje":f"Bienvenide{usuario}"})
            else:
                return render(request, "plantillas_final/bienvenida.html", {"mensaje":"Error, datos incorrectos"})
        else:
                return render(request, "plantillas_final/bienvenida.html", {"mensaje":"Error, formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "plantillas_final/login.html", {'form':form})


def register(request):
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render (request, "plantillas_final/inicio.html", {'mensaje':'Usuario Creado'})

    else:
       
        form = UserRegisterForm()

    return render(request, "plantillas_final/registro.html", {'form': form})

class Login(LoginView):
    template_name = 'plantillas_final/login.html'
    next_page = reverse_lazy('bienvenida')

class Logout(LogoutView):
    template_name = 'plantillas_final/logout.html'