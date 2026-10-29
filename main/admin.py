from django.contrib import admin
from .models import Category, Task, SubTask

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_deleted', 'deleted_at')
    list_filter = ('is_deleted',)
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'task')
    search_fields = ('title',)