# SOLO en url.py del proyecto... from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    # SOLO en url.py del proyecto... path('admin/', admin.site.urls),
    path('', inicio, name='Inicio'),
    path('buscar/', buscar, name='Buscar'),
    path('movies/', movies, name='Movies'),
    
    path('movie-form/', movieForm, name='movieForm'),
    path('busqueda-movie/', busquedaMovie, name='busquedaMovie'),
    path('busqueda-movie-res/', busquedaMovieRes, name='busquedaMovieRes'),
    
    path('lista-movies/', listaMovies, name='listaMovies'),
    path('crea-movie/', creaMovie, name='creaMovie'),
    path('borra-movie/<int:id>', borraMovie, name='borraMovie'),
    path('edita-movie/<int:id>', editaMovie, name='editaMovie'),
    
    path('cuentas/', cuentas, name='Cuentas'),
    path('contactanos/', contactanos, name='Contactanos'),
    path('acerca/', acerca, name='Acerca'),
]
