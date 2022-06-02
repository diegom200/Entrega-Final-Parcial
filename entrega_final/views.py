
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from entrega_final.models import Cliente
from entrega_final.forms import ClienteForm
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


def actualizar(request, identificador):
    pass



def cliente(request):
    return render(request, 'plantillas_final/cliente.html')

def contacto(request):
    return render(request, 'plantillas_final/contacto.html')

def equipo(request):
    return render(request, 'plantillas_final/equipo.html')

def formulario(request):
    return render(request,'plantillas_final/formulario.html')



