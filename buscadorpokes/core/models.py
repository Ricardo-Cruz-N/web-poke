from django.db import models

# Create your models here.

class Pokemon(models.Model):
    nombre = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15)
    imagen = models.URLField()