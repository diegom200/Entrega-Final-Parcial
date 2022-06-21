from atexit import register
from django.apps import AppConfig
from django.contrib import admin

#from entrega_final.models import Cliente, Contacto, Equipo

#admin.site.register(Cliente)
#admin.site.register(Contacto)
#admin.site.register(Equipo)


class EntregaFinalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'entrega_final'




