import time
from itertools import islice
from django.core.management.base import BaseCommand
from core.models import Entry


class Command(BaseCommand):

    def handle(self, *args, **options):
        start = time.time()
        print("select")
        k = 0
        for name in Entry.objects.iterator():
            k +=1
        print(k)
        print(time.time() - start)
