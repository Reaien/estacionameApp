from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    password = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    edad = models.CharField(max_length=3)
    tipo_usuario = models.CharField(max_length=15, null=True)
    auto = models.CharField(max_length=100)
    estacionamiento = models.CharField(max_length=20)
    comuna = models.CharField(max_length=100)


    class Meta:
        db_table = 'Usuario'

    def __str__(self):
        return self.nombre
    

