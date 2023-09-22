from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Lesson, View
from .serializers import ProductSerializer, LessonSerializer, ViewSerializer
from django.shortcuts import render


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class ViewViewSet(viewsets.ModelViewSet):
    queryset = View.objects.all()
    serializer_class = ViewSerializer