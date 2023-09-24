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


class CreateViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ['lesson', 'view_time']

    def save(self, **kwargs):
        user = self.context['request'].user
        view = View.objects.create(user=user, **self.validated_data)
        return view


class ViewSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    status = serializers.SerializerMethodField(source='status')

    class Meta:
        model = View
        fields = ['user', 'lesson', 'view_time', 'status']

    def get_status(self, obj):
        if obj.view_time >= obj.lesson.duration * 0.8:
            return 'viewed'
        else:
            return 'not viewed'

