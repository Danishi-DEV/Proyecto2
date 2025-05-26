from django.db import models
from Categorias.models import CategoriaModel
from django.urls import reverse

class Producto(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)
    
    is_available = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def get_url(self): #devuelve una url para poder ver el detalle mas adelante
        return reverse('producto_informacion',args=[self.categoria.slug,self.slug])
    
    def __str__(self):
        return self.nombre

class ImagenProducto(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')
    es_portada = models.BooleanField(default=False)

    def __str__(self):
        return f"Imagen de {self.producto.nombre} ({'Portada' if self.es_portada else 'Secundaria'})"