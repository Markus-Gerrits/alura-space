# Generated by Django 5.0.7 on 2024-08-20 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_phothography_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='phothography',
            name='phothography_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
