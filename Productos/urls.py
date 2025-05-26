from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductoListAPIView.as_view(), name='products'),  # Obtener productos
]