from django.contrib import admin

# Register your models here.
from entrega_final.models import Cliente, Contacto, Equipo

admin.site.register(Cliente)
admin.site.register(Contacto)
admin.site.register(Equipo)
