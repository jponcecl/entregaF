from django.db import models

# Create your models here.
class Movie(models.Model):
    nombre    = models.CharField(max_length=100)          
    nombre_tr = models.CharField(max_length=100)
    descrip   = models.TextField()
    fecha_est = models.DateField()
    #imagen    = models.ImageField(upload_to='images')
    def __str__(self):
        return self.nombre