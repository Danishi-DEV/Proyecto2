from django.contrib import admin
from .models import Producto, ImagenProducto

class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1

class ProductoModelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'is_available', 'date_created', 'date_modified')  # Campos que se muestran en la lista
    list_filter = ('categoria', 'is_available')  # Filtros en la barra lateral
    search_fields = ('nombre', 'descripcion', 'subtitulo')  # Campos en los que se puede buscar
    list_editable = ('is_available',)  # Permitir la edición directa desde la lista
    ordering = ('-date_created',)  # Ordenar por fecha de creación descendente
    prepopulated_fields = {'slug': ('nombre',)}  # Crear el slug automáticamente desde el nombre
    date_hierarchy = 'date_created'  # Añadir una jerarquía de fechas en la parte superior
    fieldsets = (
        (None, {
            'fields': ('nombre', 'slug', 'categoria', 'descripcion', 'subtitulo', 'is_available')
        }),
    )
    readonly_fields = ('date_created', 'date_modified')  #Mostrar como solo lectura
    inlines = [ImagenProductoInline]
    
admin.site.register(Producto, ProductoModelAdmin)
