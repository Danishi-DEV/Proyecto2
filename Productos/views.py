from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

class ProductoListAPIView(generics.ListAPIView):
    queryset = Producto.objects.filter(is_available=True).prefetch_related('imagenes')
    serializer_class = ProductoSerializer


