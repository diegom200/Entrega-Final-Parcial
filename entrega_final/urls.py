from django.urls import path
from entrega_final import views
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('agregar/', views.agregar, name='agregar'),
    path('borrar/<identificador>', views.borrar, name='borrar'),
    path('cliente/', views.cliente, name='cliente'),
    path('contacto/', views.contacto, name='contacto'),
    path('equipo/', views.equipo, name='equipo'),
    path('formulario/', views.formulario, name='formulario'),
    path('busquedaCliente', views.busquedacliente, name="busquedacliente"),
    path('buscar/', views.buscar),
    path('login', views.login_request, name='login'),
    path('register', views.register, name = 'register'),
    path('logout', LogoutView.as_view(template_name='plantillas_final/logout.html'), name='logout'),

    
]


  


