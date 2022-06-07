
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from entrega_final.models import Cliente, Contacto, Equipo
from entrega_final.forms import ClienteForm, ContactoForm, EquipoForm
from django.template import loader

# Create your views here.

def inicio(request):
    return render(request, 'plantillas_final/inicio.html/')

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

            nombre = form.cleaned_data['razon_social']
            email = form.cleaned_data['id_cliente']
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


