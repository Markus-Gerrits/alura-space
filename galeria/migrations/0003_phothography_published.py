# Generated by Django 5.0.7 on 2024-08-20 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_phothography_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='phothography',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
