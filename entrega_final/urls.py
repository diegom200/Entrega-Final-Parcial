from django.urls import path
from entrega_final import views, models
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('welcome/', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    path('borrar_cliente/<identificador>', views.borrar_cliente, name='borrar_cliente'),
    path('borrar_contacto/<identificador>', views.borrar_contacto, name='borrar_contacto'),
    path('borrar_equipo/<identificador>', views.borrar_equipo, name='borrar_equipo'),
    path('buscar_cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('buscar_contacto/', views.buscar_contacto, name='buscar_contacto'),
    path('buscar_equipo/', views.buscar_equipo, name='buscar_equipo'),
    path('cliente/', views.cliente, name='cliente'),
    path('contacto/', views.contacto, name='contacto'),
    path('equipo/', views.equipo, name='equipo'),
    path('index_cliente/', views.index_cliente, name='index_cliente'),
    path('index_contacto/', views.index_contacto, name='index_contacto'),
    path('index_equipo/', views.index_equipo, name='index_equipo'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('lista_contactos/', views.lista_contactos, name='lista_contactos'),
    path('lista_equipos/', views.lista_equipos, name='lista_equipos'),
    path("entrar/", views.Login.as_view(), name="login"),
    path('register', views.register, name = 'register'),
    path('logout', LogoutView.as_view(template_name='plantillas_final/logout.html'), name='logout'),
    path('base', views.BlogBase.as_view(), name='base')

    
]


  


