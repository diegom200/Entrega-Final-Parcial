from django.urls import path
from entrega_final import views


urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('agregar/', views.agregar, name='agregar'),
    path('borrar/<identificador>', views.borrar, name='borrar'),
    path('cliente/', views.cliente, name='cliente'),
    path('contacto/', views.contacto, name='contacto'),
    path('equipo/', views.equipo, name='equipo'),
    path('formulario/', views.formulario, name='formulario'),

]


  


