from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Lesson, View
from .serializers import ProductSerializer, LessonSerializer, ViewSerializer, CreateViewSerializer
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class ViewViewSet(viewsets.ModelViewSet):
    queryset = View.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateViewSerializer
        else:
            return ViewSerializer

    def perform_create(self, serializer):
        user = self.request.user
        lesson_id = self.request.data['lesson']
        lesson = Lesson.objects.get(id=lesson_id)
        view_time = self.request.data.get('view_time')  # Получаем значение view_time из запроса
        view = View.objects.create(user=user, lesson=lesson, view_time=view_time)
        serializer.instance = view