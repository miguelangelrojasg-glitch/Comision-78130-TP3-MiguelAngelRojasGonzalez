from django.contrib import admin
from app_coder_cai.models import *

# Register your models here.

#admin.site.register
...

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "fecha_de_nacimiento")
    list_display_links = ("nombre", "apellido", "email", "fecha_de_nacimiento")
    search_fields = ("fecha_de_nacimiento",)
    list_filter = ("nombre", "apellido", "email", "fecha_de_nacimiento")
    ordering = ("apellido", "nombre")
    readonly_fields = ("fecha_de_creacion",)
