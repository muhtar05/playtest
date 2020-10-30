import time
from itertools import islice
from django.core.management.base import BaseCommand
from core.models import Entry


class Command(BaseCommand):

    def common_insert_approach(self):
        for i in range(100000):
            entry = Entry()
            entry.name = "Test {}".format(i)
            entry.save()

    def bulk_insert_approach(self):
        batch_size = 500
        objs = (Entry(name='Test %s' % i) for i in range(1000000))
        while True:
            batch = list(islice(objs, batch_size))
            if not batch:
                break
            Entry.objects.bulk_create(batch, batch_size)

    def handle(self, *args, **options):
        start = time.time()
        print("Start entry")
        # self.common_insert_approach()
        self.bulk_insert_approach()
        print(time.time() - start)