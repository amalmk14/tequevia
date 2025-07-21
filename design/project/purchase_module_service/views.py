from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class CategoryViewsets(viewsets.ModelViewSet):
    queryset = Category.objects.filter(delete_status=True).order_by('-created_on')
    serializer_class = CategorySerializer

class Level2CategoryViewsets(viewsets.ModelViewSet):
    queryset = Level2Category.objects.filter(delete_status=True).order_by('-created_on')
    serializer_class = Level2Serializer

class Level3CategoryViewsets(viewsets.ModelViewSet):
    queryset = Level3Category.objects.filter(delete_status=True).order_by('-created_on')
    serializer_class = level3Serializer























class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(delete_status=False).order_by('-created_on')
    serializer_class = CategorySerializer