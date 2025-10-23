from django.shortcuts import render, redirect
from app_coder_cai.forms import ClienteForm
from app_coder_cai.models import Cliente

def index(request):
    return render(request, "app_coder_cai/index.html")

def test(request):
    return render(request, "app_coder_cai/test.html")

def nuevo_cliente(request):
    # GET - Pedir informacion a la base de datos. 
    # POST - Solicitud para crear infromación / manipular información.
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
    if len(query) > 0: # if query:
        cliente = Cliente.objects.filter(
            nombre__icontains=query).order_by("-fecha_de_creacion")
    else:
        cliente = Cliente.objects.all().order_by("-fecha_de_creacion")

    return render(request, "app_coder_cai/cliente_list.html", {"cliente": cliente, "query": query})