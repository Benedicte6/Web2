# Generated by Django 5.0.6 on 2024-05-27 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agronomy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
    ]