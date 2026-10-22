from django.contrib import admin
from .models import Task, SubTask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'deadline') # Здесь status есть, и это верно

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'completed') # Убрали 'status' отсюда