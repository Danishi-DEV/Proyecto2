from rest_framework import serializers
from .models import Producto, ImagenProducto

class ImagenProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProducto
        fields = ('id', 'imagen', 'es_portada')

class ProductoSerializer(serializers.ModelSerializer):
    imagenes = ImagenProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'categoria', 'descripcion', 'subtitulo', 'slug', 'is_available', 'date_created', 'date_modified', 'imagenes')


