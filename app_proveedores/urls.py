from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_proveedores, name="lista_proveedores"),
    path("nuevo/", views.nuevo_proveedor, name="nuevo_proveedor"),
    path("eliminar/<int:pk>/", views.eliminar_proveedor, name="eliminar_proveedor"),
    path("modificar/<int:pk>/", views.modificar_proveedor, name="modificar_proveedor"),
]