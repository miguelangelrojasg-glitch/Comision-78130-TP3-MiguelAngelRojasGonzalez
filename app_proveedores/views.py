from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Proveedor
from .forms import ProveedorForm

@login_required
def lista_proveedores(request):
    query = request.GET.get("q", "")
    if query:
        proveedores = Proveedor.objects.filter(nombre__icontains=query).order_by("-fecha_de_creacion")
    else:
        proveedores = Proveedor.objects.all().order_by("-fecha_de_creacion")
    return render(request, "app_proveedores/lista_proveedores.html", {"proveedores": proveedores, "query": query})

@login_required
def nuevo_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor creado correctamente")
            return redirect("lista_proveedores")
    else:
        form = ProveedorForm()
    return render(request, "app_proveedores/nuevo_proveedor_form.html", {"form": form})

@login_required
def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.delete()
    messages.success(request, "Proveedor eliminado correctamente")
    return redirect("lista_proveedores")

@login_required
def modificar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor modificado correctamente.")
            return redirect("lista_proveedores")
    else:
        form = ProveedorForm(instance=proveedor)
    
    return render(request, "app_proveedores/nuevo_proveedor_form.html", {"form": form, "edicion": True})
