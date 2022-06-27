
from curses.ascii import US
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from entrega_final.models import BlogModel, Cliente, Contacto, Equipo
from entrega_final.forms import *
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def inicio(request):
    return render(request, 'plantillas_final/base.html/')

def welcome(request):
    return render(request, 'plantillas_final/inicio.html' )

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


def borrar_cliente(request, identificador):
   
    if request.method == "GET":
        cliente = Cliente.objects.filter(id=int(identificador)).first()
        if cliente:
            cliente.delete()
        return HttpResponseRedirect("plantillas_final/bienvenida.html/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

def borrar_contacto(request, identificador):
   
    if request.method == "GET":
        contacto = Contacto.objects.filter(id=int(identificador)).first()
        if contacto:
            contacto.delete()
        return HttpResponseRedirect("plantillas_final/bienvenida.html/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

def borrar_equipo(request, identificador):
   
    if request.method == "GET":
        equipo = Equipo.objects.filter(id=int(identificador)).first()
        if equipo:
            equipo.delete()
        return HttpResponseRedirect("plantillas_final/bienvenida.html/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

def buscar_cliente(request):
    pass

def buscar_contacto(request):
    pass

def buscar_equipo(request):
    pass

def actualizar_cliente(request, identificador):
    pass

def actualizar_contacto(request, identificador):
    pass

def actualizar_equipo(request, identificador):
    pass

def index_cliente(request):
    return render(request, 'plantillas_final/index_cliente.html')

def index_contacto(request):
    return render(request, 'plantillas_final/index_contacto.html')

def index_equipo(request):
    return render(request, 'plantillas_final/index_equipo.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'plantillas_final/lista_clientes.html', {'clientes': clientes})

def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'plantillas_final/lista_contactos.html', {'contactos': contactos})

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'plantillas_final/lista_equipos.html', {'equipos': equipos})

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

class BlogBase(ListView):

    model = BlogModel
    template_name = "plantillas_final/base.html"


class Login(LoginView):
    template_name = 'plantillas_final/login.html'
    next_page = reverse_lazy('inicio')

class Logout(LogoutView):
    template_name = 'plantillas_final/logout.html'

