from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"Cliente: {self.nombre} - {self.apellido}"