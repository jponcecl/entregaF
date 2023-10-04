# SOLO en url.py del proyecto... from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    # SOLO en url.py del proyecto... path('admin/', admin.site.urls),
    path('', inicio, name='Inicio'),
    path('buscar/', buscar, name='Buscar'),
    path('movies/', movies, name='Movies'),
    path('cuentas/', cuentas, name='Cuentas'),
    path('contactanos/', contactanos, name='Contactanos'),
    path('acerca/', acerca, name='Acerca'),
]
