from pathlib import Path
from django.db import models
from django.dispatch import receiver
from books.models import Book


@receiver(models.signals.post_delete, sender=Book)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        current_file = Path(instance.file.path)
        if current_file.is_file():
            current_file.unlink()
