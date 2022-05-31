from django.urls import path
from entrega_final import views


urlpatterns = [

    path('', views.inicio, name='Inicio'),
    path('agregar/', views.agregar, name='Agregar'),
    path('borrar/<identificador>', views.borrar, name='Borrar'),
    path('cliente', views.cliente, name='Cliente'),
    path('contacto', views.contacto, name='Contacto'),
    path('equipo', views.equipo, name='Equipo'),
    path('formulario', views.formulario, name='Formulario'),

]


  


