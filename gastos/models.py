from django.db import models
from datetime import datetime

# Create your models here.
class Gastos(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    gasto_fecha = models.DateTimeField(default=datetime.now, blank=True)
    cuenta_bancaria = models.CharField(max_length=100, blank=True)
    numero_factura = models.CharField(max_length=200, blank=True)
    proveedor = models.CharField(max_length=200, blank=True)
    costo = models.DecimalField(max_digits=7, decimal_places=2)
    iva = models.DecimalField(max_digits=7, decimal_places=2)
    costo_total = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return self.nombre

