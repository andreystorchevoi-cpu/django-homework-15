
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task, SubTask
from .serializers import (
    TaskCreateSerializer,
    TaskDetailSerializer,
    SubTaskCreateSerializer,
    SubTaskSerializer,
)


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['-id']


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.select_related('task').all()
    serializer_class = SubTaskCreateSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ['completed', 'task__deadline']
    search_fields = ['title', 'task__title']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class SubTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer




