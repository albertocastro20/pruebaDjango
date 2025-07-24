# products/models.py
from django.db import models

class Producto(models.Model):
    # id (auto generado) [cite: 13] Django lo crea automáticamente.
    nombre = models.CharField(max_length=255) # nombre (char, requerido) [cite: 14]
    descripcion = models.TextField(blank=True, null=True) # descripcion (texto, opcional) [cite: 15]
    precio = models.DecimalField(max_digits=10, decimal_places=2) # precio (decimal, requerido) [cite: 16]
    disponible = models.BooleanField(default=True) # disponible (booleano, default=True) [cite: 17]

    def __str__(self):
        return self.nombre