# Generated by Django 3.2.3 on 2021-06-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to='img/%y'),
        ),
    ]