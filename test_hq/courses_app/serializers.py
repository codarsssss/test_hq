from rest_framework import serializers
from .models import Product, Lesson, View


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']
        read_only_fields = ['owner']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'
