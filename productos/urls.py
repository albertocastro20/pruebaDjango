# products/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

# El router genera automáticamente las URLs para el ViewSet:
# /api/productos/ (GET, POST)
# /api/productos/{id}/ (GET, PUT, DELETE)
router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='producto')

urlpatterns = [
    path('', include(router.urls)),
]