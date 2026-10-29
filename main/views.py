from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        tasks_count = category.tasks.count()

        return Response({
            "category_id": category.id,
            "category_name": category.name,
            "tasks_count": tasks_count
        })




