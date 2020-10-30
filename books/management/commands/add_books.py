import os
import hashlib
from pathlib import Path
from datetime import datetime

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from books.models import Book


class Command(BaseCommand):

    def get_checksum(self, path):
        with open(path, "rb") as f:
            file_hash = hashlib.md5()
            chunk = f.read(8192)
            while chunk:
                file_hash.update(chunk)
                chunk = f.read(8192)

            return file_hash.hexdigest()

    def handle(self, *args, **options):
        print("add_books")
        folder = '{}/files'.format(settings.BASE_DIR)
        for path in Path(folder).iterdir():
            checksum = self.get_checksum(path)
            if not Book.objects.filter(checksum=checksum).exists():
                book = Book()
                book.name = os.path.basename(path)
                book.file.save(os.path.basename(path), File(open(path,'rb')))
                book.checksum = checksum
                book.save()
                print("add book", path)
                path.unlink()
            else:
                print("exists book", path)
                path.unlink()

