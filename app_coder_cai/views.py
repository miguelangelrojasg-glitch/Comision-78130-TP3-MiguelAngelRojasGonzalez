from django.shortcuts import render, redirect
from app_coder_cai.forms import ClienteForm, ProductoForm, CompraForm
from app_coder_cai.models import Cliente, Producto, Compra


def index(request):
    return render(request, "app_coder_cai/index.html")


def test(request):
    return render(request, "app_coder_cai/test.html")


# -----------------------
# CLIENTES
# -----------------------
def nuevo_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ClienteForm()
    return render(request, "app_coder_cai/nuevo_cliente_form.html", {"form": form})


def lista_cliente(request):
    query = request.GET.get("q", "")
    if query:
        cliente = Cliente.objects.filter(nombre__icontains=query).order_by("-fecha_de_creacion")
    else:
        cliente = Cliente.objects.all().order_by("-fecha_de_creacion")
    return render(request, "app_coder_cai/cliente_list.html", {"cliente": cliente, "query": query})


# -----------------------
# PRODUCTOS
# -----------------------
def lista_producto(request):
    query = request.GET.get("q", "")
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    return render(request, "app_coder_cai/producto_list.html", {"productos": productos, "query": query})


def nuevo_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_producto")
    else:
        form = ProductoForm()
    return render(request, "app_coder_cai/nuevo_producto_form.html", {"form": form})


# -----------------------
# COMPRAS
# -----------------------
def lista_compra(request):
    compras = Compra.objects.select_related("cliente", "producto").order_by("-fecha")
    return render(request, "app_coder_cai/compra_list.html", {"compras": compras})


def nueva_compra(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_compra")
    else:
        form = CompraForm()
    return render(request, "app_coder_cai/nueva_compra_form.html", {"form": form})
