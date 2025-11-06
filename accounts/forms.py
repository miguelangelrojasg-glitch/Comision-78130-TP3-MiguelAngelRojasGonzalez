from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Perfil

class PerfilCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fecha_de_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
    
    class Meta:
        model = Perfil
        fields = ("username", "email", "fecha_de_nacimiento", "pais", "direccion", "password1", "password2")

class PerfilChangeForm(forms.ModelForm):  # ← CAMBIAR UserChangeForm por forms.ModelForm
    fecha_de_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
    
    class Meta:
        model = Perfil
        fields = ['username', 'email', 'first_name', 'last_name', 'fecha_de_nacimiento', 'pais', 'direccion', 'avatar']