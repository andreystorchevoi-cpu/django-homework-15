
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название категории"
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )
    status = models.CharField(
        max_length=50,
        default='new',
        verbose_name="Статус"
    )
    deadline = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дедлайн"
    )

    def __str__(self):
        return self.title


class SubTask(models.Model):
    task = models.ForeignKey(
        Task,
        related_name='subtasks',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Основная задача"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок подзадачи"
    )
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title

