from pathlib import Path
import shutil
import hashlib
from datetime import datetime

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from books.models import Book


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("add_books")
        c = 0
        destination_folder = settings.BASE_DIR
        for file in Path('/Users/Mac/Downloads').glob('*.epub'):
            c += 1
            print(file.name)
            destination_path = '{}/files/{}'.format(destination_folder, file.name)
            shutil.move(file, destination_path)