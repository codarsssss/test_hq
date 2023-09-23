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
    class Meta:
        model = View
        fields = '__all__'
