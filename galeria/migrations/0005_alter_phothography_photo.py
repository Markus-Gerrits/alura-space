# Generated by Django 5.0.7 on 2024-08-22 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_phothography_phothography_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phothography',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
