from rest_framework import viewsets
from .models import Product, Lesson, View
from .serializers import ProductSerializer, LessonSerializer, ViewSerializer, CreateViewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Устанавливаем владельца продукта перед сохранением
        serializer.save(owner=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class ViewViewSet(viewsets.ModelViewSet):
    queryset = View.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            # Используем CreateViewSerializer при создании объекта View
            return CreateViewSerializer
        else:
            # Используем ViewSerializer для остальных действий
            return ViewSerializer

    def perform_create(self, serializer):
        user = self.request.user
        lesson_name = self.request.data['lesson_name']

        try:
            lesson = Lesson.objects.get(name=lesson_name)
        except Lesson.DoesNotExist:
            raise ValidationError("Урок с указанным именем не существует.")

        view_time = self.request.data.get('view_time')
        view = View.objects.create(user=user, lesson=lesson, view_time=view_time)

        serializer.instance = view