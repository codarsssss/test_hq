from rest_framework import serializers
from .models import Product, Lesson, View


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']
        read_only_fields = ['owner']


class LessonSerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(
        queryset=Product.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Lesson
        fields = ['name', 'video_link', 'duration', 'products']


class ViewSerializer(serializers.ModelSerializer):
    lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all())

    class Meta:
        model = View
        fields = ['lesson', 'view_time']

    def create(self, validated_data):
        user = self.context['request'].user  # Получаем текущего пользователя
        lesson_pk = validated_data.pop('lesson').id
        view = View.objects.create(user=user, lesson_id=lesson_pk, **validated_data)
        return view

