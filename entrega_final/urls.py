from django.urls import path
from entrega_final import views


urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('borrar_cliente/<identificador>', views.borrar_cliente, name='borrar_cliente'),
    path('borrar_contacto/<identificador>', views.borrar_contacto, name='borrar_contacto'),
    path('borrar_equipo/<identificador>', views.borrar_equipo, name='borrar_equipo'),
    path('buscar_cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('buscar_contacto/', views.buscar_contacto, name='buscar_contacto'),
    path('buscar_equipo/', views.buscar_equipo, name='buscar_equipo'),
    path('actualizar_cliente/<identificador>', views.actualizar_cliente, name='actualizar_cliente'),
    path('actualizar_contacto/<identificador>', views.actualizar_contacto, name='actualizar_contacto'),
    path('actualizar_equipo/<identificador>', views.actualizar_equipo, name='actualizar_equipo'),
    path('cliente/', views.cliente, name='cliente'),
    path('contacto/', views.contacto, name='contacto'),
    path('equipo/', views.equipo, name='equipo'),
    path('index_cliente/', views.index_cliente, name='index_cliente'),
    path('index_contacto/', views.index_contacto, name='index_contacto'),
    path('index_equipo/', views.index_equipo, name='index_equipo'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('lista_contactos/', views.lista_contactos, name='lista_contactos'),
    path('lista_equipos/', views.lista_equipos, name='lista_equipos')

]


  

