# SOLO en url.py del proyecto... from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    # SOLO en url.py del proyecto... path('admin/', admin.site.urls),
    path('', inicio),
    path('movies/', movies),
]
