from django.db import models
from django.urls import reverse

class CategoriaModel(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=100, null=False)
    slug = models.CharField(max_length=100,unique=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def get_url(self): #url para filtrado
        return reverse('producto_por_categoria',args=[self.slug])
    
    def __str__(self):
        return self.nombre