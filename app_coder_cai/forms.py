# app_coder_cai/forms.py
from django import forms
from .models import Cliente, Producto, Compra

__all__ = ["ClienteForm", "ProductoForm", "CompraForm"]

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "email", "fecha_de_nacimiento"]
        widgets = {
            "fecha_de_nacimiento": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "sku", "precio", "stock", "activo"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "sku": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "stock": forms.NumberInput(attrs={"class": "form-control", "step": "1", "min": "0"}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ["cliente", "producto", "cantidad", "precio_unitario", "estado"]
        widgets = {
            "cliente": forms.Select(attrs={"class": "form-select"}),
            "producto": forms.Select(attrs={"class": "form-select"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control", "min": "1", "step": "1"}),
            "precio_unitario": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
        }
