from django.db import models
from django.utils import timezone

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class SubTask(models.Model):
    title = models.CharField(max_length=255)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks', null=True, blank=True)

    def __str__(self):
        return self.title
