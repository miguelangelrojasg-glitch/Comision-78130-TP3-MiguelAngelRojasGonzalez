from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_nacimiento = models.DateField(null=True)

    class Meta:
        ordering = ["-fecha_de_creacion"]
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"Cliente: {self.nombre} - {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    sku = models.CharField("Código/SKU", max_length=50, unique=True)
    precio = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))]
    )
    stock = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.nombre} (SKU: {self.sku})"

    def hay_stock(self, cantidad: int) -> bool:
        return self.stock >= cantidad

class Compra(models.Model):
    ESTADOS = [
        ("CREADA", "Creada"),
        ("PAGADA", "Pagada"),
        ("CANCELADA", "Cancelada"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="compras")
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, related_name="compras")
    cantidad = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    precio_unitario = models.DecimalField(
        "Precio unitario al momento",
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
        help_text="Se guarda el precio histórico al realizar la compra."
    )
    estado = models.CharField(max_length=10, choices=ESTADOS, default="CREADA")
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha"]
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return f"Compra #{self.id} - {self.cliente} - {self.producto} x{self.cantidad}"

    @property
    def subtotal(self) -> Decimal:
        return self.precio_unitario * self.cantidad
