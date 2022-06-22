
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from entrega_final.models import Cliente, Contacto, Equipo
from entrega_final.forms import *
from django.template import loader

from entrega_final.models import Cliente, Contacto, Equipo

# Create your views here.

def inicio(request):
    return render(request, 'plantillas_final/bienvenida.html/')


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

def buscar_cliente(request):
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarClienteForm(request.GET)
        if form_busqueda.is_valid():
            personas = Cliente.objects.filter(razon_social__icontains=request.GET.get("palabra_a_buscar"))
            return render(request, 'plantillas_final/lista_clientes.html', {"personas": personas, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarClienteForm()
        return render(request, 'plantillas_final/buscar_cliente.html', {"form_busqueda": form_busqueda})
        

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

