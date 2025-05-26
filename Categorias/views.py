from django.shortcuts import render
from rest_framework import generics
from .models import CategoriaModel
from .serializers import CategoriaSerializer

class CategoriaListView(generics.ListAPIView):
    queryset = CategoriaModel.objects.all()
    serializer_class = CategoriaSerializer
