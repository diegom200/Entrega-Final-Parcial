from django.db import models

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

    

