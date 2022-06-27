from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    razon_social=models.CharField(max_length=100)
    id_cliente=models.IntegerField()

class Contacto(models.Model):
    nombre=models.CharField(max_length=100)
    email=models.EmailField()

class Equipo(models.Model):
    equipo=models.CharField(max_length=100)
    serie=models.CharField(max_length=100)


class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

