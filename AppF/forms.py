# Forms By JuanK
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import NumberInput
from .models import Movie, Avatar
import datetime

class MovieFormulario(forms.Form):
    nombre    = forms.CharField(max_length=100)          
    nombre_tr = forms.CharField(max_length=100)
    descrip   = forms.CharField(widget=forms.Textarea)
    fecha_est = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

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

    class Meta:
        model = Avatar
        fields = ("imagen",)