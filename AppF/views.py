from django.shortcuts import render
# AGREGADAS
from django.http import HttpResponse
from .models import *

# Create your views here.

def inicio(req):
    return render(req, "inicio.html")
    #return HttpResponse("Inicio")

def movies(req):
    return render(req, "movies.html")
    #return HttpResponse("Movies")