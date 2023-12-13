from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
    tipo_Usuario = models.CharField(max_length=100)

    class Meta:
        db_table = 'TipoUsuario'

    def __str__(self):
        return self.tipo_Usuario