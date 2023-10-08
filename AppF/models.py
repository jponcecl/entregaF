from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.

class Movie(models.Model):
    nombre    = models.CharField(max_length=100, verbose_name='Titulo de la pelicula')          
    nombre_tr = models.CharField(max_length=100, verbose_name='Titulo (Traduccion)')
    descrip   = models.TextField(verbose_name='Descripción / Resumen')
    fecha_est = models.DateField(verbose_name='Fecha de estreno')
    imagen    = models.ImageField(verbose_name='Portada', upload_to='images', blank=True, null=True)
    #imagen    = models.ImageField(upload_to='images')
    def __str__(self):
        return f'{self.nombre} - {self.nombre_tr}'
    class Meta():
        ordering = ('nombre','nombre_tr')
        unique_together = ('nombre',)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(verbose_name='Imagen de avatar', upload_to='avatares', blank=True, null=True)