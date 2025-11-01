from django.shortcuts import render, redirect, get_object_or_404
from app_coder_cai.forms import ClienteForm, ProductoForm, CompraForm
from app_coder_cai.models import Cliente, Producto, Compra
from django.contrib import messages

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


def eliminar_cliente(request, pk): # pk = ID en la base de datos
    #cliente = Cliente.objects.get(nombre=pk)
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    messages.success(request, "Cliente eliminado correctamente")
    return redirect("lista_cliente")


def modificar_cliente(request, pk):  # ← agrega pk
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente modificado correctamente.")
            return redirect("lista_cliente")
    else:
        form = ClienteForm(instance=cliente)  # ← usar ClienteForm, no Cliente
    
    return render(request, "app_coder_cai/nuevo_cliente_form.html", {"form": form, "edicion": True})

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

def eliminar_producto(request, pk): # pk = ID en la base de datos
    #cliente = Cliente.objects.get(nombre=pk)
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente")
    return redirect("lista_producto")


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

def eliminar_compra(request, pk): # pk = ID en la base de datos
    #cliente = Cliente.objects.get(nombre=pk)
    compra = get_object_or_404(Compra, pk=pk)
    compra.delete()
    messages.success(request, "Compra eliminada correctamente")
    return redirect("lista_compra")

def modificar_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == "POST":
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, "Compra modificada correctamente.")
            return redirect("lista_compra")
    else:
        form = CompraForm(instance=compra)

    return render(request, "app_coder_cai/nueva_compra_form.html", {"form": form, "compra": compra, "modo": "editar"})
