from django.db import models

# Create your models here.
class Estacionamiento(models.Model):
    nombreContacto = models.CharField(max_length=50)
    fonoContacto = models.CharField(max_length=12, null=True)
    nombreComuna = models.CharField(max_length=20)
    direccion = models.CharField(max_length=90)
    imagenEstacionamiento = models.ImageField(upload_to= "images", null=True)

    class Meta:
        db_table = 'Estacionamiento'

    def __str__(self):
        return self.nombreTitular  