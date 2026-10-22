
from django.urls import path
from .views import (
    TaskListCreateView,
    TaskDetailView,
    SubTaskListCreateView,
    SubTaskDetailView,
)

urlpatterns = [
    # Tasks
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    # SubTasks
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailView.as_view(), name='subtask-detail'),
]


