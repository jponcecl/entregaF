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
    
    path('movie-list/', movieList.as_view(), name='movieList'),
    path('movie-detail/<pk>', movieDetail.as_view(), name='movieDetail'),
    path('movie-create/', movieCreate.as_view(), name='movieCreate'),
    path('movie-update/<pk>', movieUpdate.as_view(), name='movieUpdate'),
    path('movie-delete/<pk>', movieDelete.as_view(), name='movieDelete'),
    
    path('cuentas/', cuentas, name='Cuentas'),
    path('contactanos/', contactanos, name='Contactanos'),
    path('acerca/', acerca, name='Acerca'),
]
