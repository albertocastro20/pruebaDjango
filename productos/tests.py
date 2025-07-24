# products/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Producto

class ProductoAPITests(APITestCase):
    def test_crear_y_listar_producto(self):
        """
        Asegura que podemos crear un nuevo producto y luego listarlo.
        """
        # Usamos reverse para obtener la URL dinámicamente
        url = reverse('producto-list')
        data = {'nombre': 'Teclado Mecánico', 'precio': '99.99'}

        # Probar la creación (POST)
        response_post = self.client.post(url, data, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Producto.objects.count(), 1)
        self.assertEqual(Producto.objects.get().nombre, 'Teclado Mecánico')

        # Probar el listado (GET)
        response_get = self.client.get(url, format='json')
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_get.data), 1)
        self.assertEqual(response_get.data[0]['nombre'], 'Teclado Mecánico')