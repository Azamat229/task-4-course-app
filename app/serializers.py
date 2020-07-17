from .models import Course
from rest_framework import serializers


class CourseListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    branch = serializers.SlugRelatedField(slug_field='address', read_only=True)
    contact = serializers.SlugRelatedField(slug_field='value', read_only=True)

    class Meta:
        model = Course
        fields = '__all__'  # исправить сделать несколько полей


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
