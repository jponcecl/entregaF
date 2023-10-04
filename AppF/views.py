from django.shortcuts import render
# AGREGADAS
from django.http import HttpResponse
from .models import *

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