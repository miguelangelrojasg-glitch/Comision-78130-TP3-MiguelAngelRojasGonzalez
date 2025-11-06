from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from accounts.forms import PerfilChangeForm, PerfilCreationForm


def register(request):
    if request.method == "POST":
        form = PerfilCreationForm(request.POST, request.FILES)  # ← AGREGAR request.FILES para el avatar
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_detail")
    else:
        form = PerfilCreationForm()
    return render(request, "accounts/register.html", {"form": form})

@login_required
def profile_detail(request):
    return render(request, "accounts/profile_detail.html", {"user": request.user})

@login_required  # ← AGREGAR login_required A ESTA VISTA TAMBIÉN
def profile_edit(request):
    if request.method == "POST":
        form = PerfilChangeForm(request.POST, request.FILES, instance=request.user)  # ← CORREGIDO: request.user
        if form.is_valid():
            form.save()
            return redirect("profile_detail")
        else:
            # Debug temporal
            print("🔥 ERRORES DEL FORMULARIO:")
            for field, errors in form.errors.items():
                print(f"Campo {field}: {errors}")
    else:
        form = PerfilChangeForm(instance=request.user)  # ← CORREGIDO: request.user
    
    return render(request, "accounts/profile_edit.html", {"form": form})