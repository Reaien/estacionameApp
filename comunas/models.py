from django.db import models

# Create your models here.

class Comuna(models.Model):
    nombreComuna = models.CharField(max_length=80)
    imagenComuna = models.ImageField(upload_to= "images", null=True)

    class Meta:
        db_table = 'Comuna'

    def __str__(self):
        return self.nombreComuna    