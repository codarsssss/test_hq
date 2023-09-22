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

    def __init__(self, request, *args, **kwargs):

        super().__init__(**kwargs)
        data = request.data

        lesson_id = data.get('lesson')
        lesson = Lesson.objects.get(id=lesson_id)

        duration = lesson.duration

        viewed_time = data.get('view_time')

        viewed_percentage = (viewed_time / duration) * 100

        if viewed_percentage >= 80:
            data['status'] = 'Да'
        else:
            data['status'] = 'Нет'

        # Создаем запись о просмотре урока
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
