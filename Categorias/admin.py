from django.contrib import admin
from .models import CategoriaModel

class CategoriaModelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'descripcion')  # Campos que se mostrarán en la lista
    search_fields = ('nombre', 'descripcion')  # Campos en los que se puede buscar
    prepopulated_fields = {'slug': ('nombre',)}  # Crear el slug automáticamente desde el nombre
    ordering = ('nombre',)  # Ordenar por nombre de categoría
    list_editable = ('slug',)  # Permitir la edición directa del slug desde la lista
    fieldsets = (
        (None, {
            'fields': ('nombre', 'slug', 'descripcion')
        }),
    )

admin.site.register(CategoriaModel, CategoriaModelAdmin)
