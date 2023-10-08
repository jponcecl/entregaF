from django.shortcuts import render
# AGREGADAS By JuanK
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import *
from .forms import MovieFormulario, UserEditForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def buscar_url_avatar(user):
    avatar = Avatar.objects.filter(user=user)
    if avatar.exists():
        # Se usa first() para obtener el primer objeto
        return avatar.first().imagen.url
    # Si no existe el avatar regresar un None
    return None
    
def inicio(req):
    #print(buscar_url_avatar(req.user))
    #global ava=buscar_url_avatar(req.user)
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        global ava
        ava = avatar.imagen.url
        return render(req, "inicio.html", {"url_avatar": avatar.imagen.url})
    except:
        return render(req, "inicio.html")

def buscar(req):
    return render(req, "buscar.html")
    #return HttpResponse("Movies")

def movies(req):
    return render(req, "movies.html")
    #return HttpResponse("Movies")
    
def cuentas(req):
    return render(req, "cuentas.html")
    #return HttpResponse("Movies")

@login_required(login_url='/AppF/do-login')
def contactanos(req):
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "contactanos.html", {"url_avatar": avatar.imagen.url})
    except:
        return render(req, "contactanos.html")
    #return HttpResponse("Movies")

def acerca(req):
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "acerca.html", {"url_avatar": avatar.imagen.url})
    except:
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
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "busquedaMovie.html", {"url_avatar": avatar.imagen.url})
    except:
        return render(req, "busquedaMovie.html")

def busquedaMovieRes(req: HttpRequest):
    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        movies = Movie.objects.filter(nombre__icontains=nombre)
        try:
            avatar = Avatar.objects.get(user=req.user.id)
            return render(req, "resultadosMovie.html", {"movies": movies, "url_avatar": avatar.imagen.url})
        except:
            return render(req, "resultadosMovie.html", {"movies": movies})
    else:
        return HttpResponse(f"Debe indicar algo para buscar")
    
#@staff_member_required(login_url='/AppF/do-login')       
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

class movieList(LoginRequiredMixin, ListView):
    model = Movie
    template_name = "movie_list.html"
    context_object_name = "movies"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'ava' in globals():
            context['url_avatar'] = ava
        return context

class movieDetail(DetailView):
    model = Movie
    template_name = "movie_detail.html"
    context_object_name = "movie"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'ava' in globals():
            context['url_avatar'] = ava
        return context

class movieCreate(CreateView):
    model = Movie
    template_name = "movie_create.html"
    fields = ('__all__')
    success_url = '/AppF/'
    context_object_name = "movie"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'ava' in globals():
            context['url_avatar'] = ava
        return context

class movieUpdate(UpdateView):
    model = Movie
    template_name = "movie_update.html"
    fields = ('__all__')
    success_url = '/AppF/movie-list'
    context_object_name = "movie"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'ava' in globals():
            context['url_avatar'] = ava
        return context

class movieDelete(DeleteView):
    model = Movie
    template_name = "movie_delete.html"
    fields = ('__all__')
    success_url = '/AppF/movie-list'
    context_object_name = "movie"
    
def doLogin(req):
    if req.method == 'POST':
        miForm = AuthenticationForm(req, data=req.POST)
        if miForm.is_valid():
            data = miForm.cleaned_data
            usr = data["username"]
            pwd = data["password"]
            
            user = authenticate(username=usr, password=pwd)
            if user:
                login(req, user)
                global ava
                ava = buscar_url_avatar(req.user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usr}!", "url_avatar": ava})
        return render(req, "inicio.html", {"mensaje": f"Usuario o contraseña incorrecta!"})
    else:
        # Genera form con datos si viene como GET
        miForm = AuthenticationForm()
        return render(req, "login.html", {"miForm": miForm})

def doRegister(req):
    if req.method == 'POST':
        miForm = UserCreationForm(req.POST)
        if miForm.is_valid():
            data = miForm.cleaned_data
            usr = data["username"]
            miForm.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {usr} creado exitosamente!"})
            
        return render(req, "inicio.html", {"mensaje": f"Ocurrió un error"})
    else:
        # Genera form con datos si viene como GET
        miForm = UserCreationForm()
        return render(req, "register.html", {"miForm": miForm})

def editarPerfil(req):
    usuario = req.user
    if req.method == 'POST':
        miForm = UserEditForm(req.POST, instance=req.user)
        if miForm.is_valid():
            data = miForm.cleaned_data
            usuario.first_name=data["first_name"]
            usuario.last_name=data["last_name"]
            usuario.email=data["email"]
            usuario.set_password(data["passw1"])
            usuario.save()
            
            ava = buscar_url_avatar(req.user)
            #return render(req, "inicio.html", {"mensaje": f"Bienvenido {usr}!", "url_avatar": ava})
            return render(req, "inicio.html", {"mensaje": "Perfil actualizado exitosamente!", "url_avatar": ava})
        else:
            return render(req, "editarPerfil.html", {"miForm": miForm})
    else:
        # Genera form con datos del usuario logeado
        if usuario.id != None:
            miForm = UserEditForm(instance=usuario)
            ava = buscar_url_avatar(req.user)
            return render(req, "editarPerfil.html", {"miForm": miForm, "url_avatar": ava})
        else:
            #LogoutView.as_view(template_name="logout.html")
            return render(req, "logout.html", {"mensaje": "Por seguridad debe ingresar nuevamente!"})

def editarAvatar(req):
    usuario = req.user
    if (usuario.id != None):
        if req.method == 'POST':
            miForm = AvatarForm(req.POST, req.FILES)
            if miForm.is_valid():
                try:
                    borra = Avatar.objects.get(user=req.user)
                    borra.delete()
                except:
                    pass
                
                data = miForm.cleaned_data
                avatar = Avatar(user=req.user, imagen=data["imagen"])
                avatar.save()
                avatar = Avatar.objects.filter(user=req.user)
                global ava
                ava = buscar_url_avatar(req.user)
                return render(req, "inicio.html", {"mensaje": "Avatar actualizado exitosamente!", "url_avatar": ava})
        else:
            # Genera form con datos del usuario logeado
            miForm = AvatarForm()
            ava = buscar_url_avatar(req.user)
            return render(req, "editarAvatar.html", {"miForm": miForm, "url_avatar": ava})
    else:
        return render(req, "editarAvatar.html", {"mensaje": "Debe estar logeado para esta operación"})