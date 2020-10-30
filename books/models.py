from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=1024)
    file = models.FileField(upload_to='books')
    checksum = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
