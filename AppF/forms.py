# Forms By JuanK
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import NumberInput, DateInput
from .models import Movie, Avatar
import datetime

forms.DateInput.input_type="date"
forms.DateTimeInput.input_type="datetime-local" 

class MovieFormulario(forms.ModelForm):
    nombre    = forms.CharField(max_length=100)          
    nombre_tr = forms.CharField(max_length=100)
    descrip   = forms.CharField(widget=forms.Textarea)
    fecha_est = forms.DateField()

class UserEditForm(UserChangeForm):
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    
    first_name = forms.CharField(label="Nombres")
    last_name = forms.CharField(label="Apellidos")
    email = forms.CharField(label="Correo")
    passw1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    passw2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields = ("first_name", "last_name", "email", "passw1", "passw2")
    
    #def clean = TODOS ; def clean_X donde X=campo
    def clean_passw2(self):
        print(self.cleaned_data)
        
        pw1 = self.cleaned_data["passw1"]
        pw2 = self.cleaned_data["passw2"]
        
        if pw1 != pw2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return pw2

class AvatarForm(forms.ModelForm):
    imagen = forms.ImageField(required=True)
    class Meta:
        model = Avatar
        fields = ("imagen",)