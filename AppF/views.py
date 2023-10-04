from django.shortcuts import render
# AGREGADAS
from django.http import HttpResponse
from .models import *

# Create your views here.

def inicio(req):
    return HttpResponse("Inicio")

def movies(req):
    return HttpResponse("Movies")