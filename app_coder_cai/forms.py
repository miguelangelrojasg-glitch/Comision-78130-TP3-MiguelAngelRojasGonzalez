from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "email", "fecha_de_nacimiento"]
        widgets = {
            "fecha_de_nacimiento": forms.DateTimeInput(attrs={"type": "date", "class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"})
        }
