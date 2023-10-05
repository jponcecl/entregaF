# Forms By JuanK
from django import forms
from django.forms.widgets import NumberInput
import datetime

class MovieFormulario(forms.Form):
    nombre    = forms.CharField(max_length=100)          
    nombre_tr = forms.CharField(max_length=100)
    descrip   = forms.CharField(widget=forms.Textarea)
    fecha_est = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))