# Generated by Django 3.2.3 on 2021-05-21 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='caption',
        ),
    ]
