from django.shortcuts import render
# AGREGADAS By JuanK
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import *
from .forms import MovieFormulario

# Create your views here.

def inicio(req):
    return render(req, "inicio.html")
    #return HttpResponse("Inicio")

def buscar(req):
    return render(req, "buscar.html")
    #return HttpResponse("Movies")

def movies(req):
    return render(req, "movies.html")
    #return HttpResponse("Movies")
    
def cuentas(req):
    return render(req, "cuentas.html")
    #return HttpResponse("Movies")

def contactanos(req):
    return render(req, "contactanos.html")
    #return HttpResponse("Movies")

def acerca(req):
    return render(req, "acerca.html")
    #return HttpResponse("Movies")

def movieForm(req):
    if req.method == 'POST':
        #movie = Movie(nombre=req.POST["nombre"], nombre_tr=req.POST["nombre_tr"], descrip=req.POST["descrip"], fecha_est=req.POST["fecha_est"])
        miForm = MovieFormulario(req.POST)
        if miForm.is_valid():
            data = miForm.cleaned_data
            movie = Movie(nombre=data["nombre"], nombre_tr=data["nombre_tr"], descrip=data["descrip"], fecha_est=data["fecha_est"])
            movie.save()
            return render(req, "inicio.html")
    else:
        # Genera form vacio si viene como GET
        miForm = MovieFormulario()
        return render(req, "movieForm.html", {"miForm": miForm})

def busquedaMovie(req):
    return render(req, "busquedaMovie.html")

def busquedaMovieRes(req: HttpRequest):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        movies = Movie.objects.filter(nombre__icontains=nombre)
        return render(req, "resultadosMovie.html", {"movies": movies})
    else:
        return HttpResponse(f"Debe indicar algo para buscar")
        
def listaMovies(req):
    movies = Movie.objects.all()
    return render(req, "listaMovies.html", {"movies": movies})

def creaMovie(req):
    if req.method == 'POST':
        #movie = Movie(nombre=req.POST["nombre"], nombre_tr=req.POST["nombre_tr"], descrip=req.POST["descrip"], fecha_est=req.POST["fecha_est"])
        miForm = MovieFormulario(req.POST)
        if miForm.is_valid():
            data = miForm.cleaned_data
            movie = Movie(nombre=data["nombre"], nombre_tr=data["nombre_tr"], descrip=data["descrip"], fecha_est=data["fecha_est"])
            movie.save()
            return render(req, "inicio.html")
    else:
        # Genera form vacio si viene como GET
        miForm = MovieFormulario()
        return render(req, "creaMovie.html", {"miForm": miForm})

def borraMovie(req, id):
    if req.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        
        movies = Movie.objects.all() # Busca todos despues de borrar
        return render(req, "listaMovies.html", {"movies": movies})

def editaMovie(req, id):
    movie = Movie.objects.get(id=id)
    if req.method == 'POST':
        miForm = MovieFormulario(req.POST)
        if miForm.is_valid():
            data = miForm.cleaned_data
            movie.nombre=data["nombre"]
            movie.nombre_tr=data["nombre_tr"]
            movie.descrip=data["descrip"]
            movie.fecha_est=data["fecha_est"]
            movie.save()
            
            return render(req, "inicio.html")
    else:
        # Genera form con datos si viene como GET
        miForm = MovieFormulario(initial={
        "nombre": movie.nombre,
        "nombre_tr": movie.nombre_tr,
        "descrip": movie.descrip,
        "fecha_est": movie.fecha_est,
        })
        return render(req, "editaMovie.html", {"miForm": miForm, "id": movie.id})

class movieList(ListView):
    model = Movie
    template_name = "movie_list.html"
    context_object_name = "movies"

class movieDetail(DetailView):
    model = Movie
    template_name = "movie_detail.html"
    context_object_name = "movie"

class movieCreate(CreateView):
    model = Movie
    template_name = "movie_create.html"
    fields = ('__all__')
    success_url = '/AppF/'

class movieUpdate(UpdateView):
    model = Movie
    template_name = "movie_update.html"
    fields = ('__all__')
    success_url = '/AppF/movie-list'
    context_object_name = "movie"

class movieDelete(DeleteView):
    model = Movie
    template_name = "movie_delete.html"
    fields = ('__all__')
    success_url = '/AppF/movie-list'
    context_object_name = "movie"
