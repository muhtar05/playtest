# Generated by Django 3.0.8 on 2020-10-21 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_checksum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='checksum',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
