from django.db import models
from django.utils import timezone


class Entry(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Status(models.TextChoices):
    UNPUBLISHED = 'UN', 'Unpublished'
    PUBLISHED = 'PB', 'Published'


class Book(models.Model):
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.UNPUBLISHED,
    )
    title = models.CharField(max_length=200)

    class Meta:
        index_together = [["status", "title"]]
