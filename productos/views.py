# products/views.py
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver o editar productos.
    """
    queryset = Producto.objects.all().order_by('-id')
    serializer_class = ProductoSerializer