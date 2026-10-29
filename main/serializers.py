from rest_framework import serializers
from .models import Category, Task, SubTask

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'is_deleted', 'deleted_at']
        read_only_fields = ['is_deleted', 'deleted_at']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'category', 'description']

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'title', 'task']