# proyecto_coder_cai/urls.py
from django.urls import path
from app_coder_cai import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test, name="test"),

    path("clientes/", views.lista_cliente, name="lista_cliente"),
    path("clientes/nuevo/", views.nuevo_cliente, name="nuevo_cliente"),

    path("productos/", views.lista_producto, name="lista_producto"),
    path("productos/nuevo/", views.nuevo_producto, name="nuevo_producto"),

    path("compras/", views.lista_compra, name="lista_compra"),
    path("compras/nuevo/", views.nueva_compra, name="nueva_compra"),
]