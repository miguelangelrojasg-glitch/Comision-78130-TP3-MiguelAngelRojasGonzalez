from django.urls import path
from app_coder_cai.views import index, test, nuevo_cliente, lista_cliente

urlpatterns = [
    path("", index, name="index"),
    path("test/", test, name="test"),
    path("nuevo/cliente/", nuevo_cliente, name="nuevo_cliente"),
    path("lista/", lista_cliente, name="cliente_list"),
]
