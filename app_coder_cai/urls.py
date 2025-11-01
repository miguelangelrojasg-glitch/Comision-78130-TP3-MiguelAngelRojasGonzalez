# proyecto_coder_cai/urls.py
from django.urls import path
from app_coder_cai import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test, name="test"),

    path("clientes/", views.lista_cliente, name="lista_cliente"),
    path("clientes/<int:pk>/eliminar", views.eliminar_cliente, name="eliminar_cliente"),
    path("clientes/nuevo/", views.nuevo_cliente, name="nuevo_cliente"),
    path("clientes/modificar/<int:pk>", views.modificar_cliente, name="modificar_cliente"),

    path("productos/", views.lista_producto, name="lista_producto"),
    path("productos/<int:pk>/eliminar", views.eliminar_producto, name="eliminar_producto"),
    path("productos/nuevo/", views.nuevo_producto, name="nuevo_producto"),

    path("compras/", views.lista_compra, name="lista_compra"),
    path("compras/nuevo/", views.nueva_compra, name="nueva_compra"),
    path("compras/modificar/<int:pk>", views.modificar_compra, name="modificar_compra"),
    path("compras/<int:pk>/eliminar", views.eliminar_compra, name="eliminar_compra"),

]