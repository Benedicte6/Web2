# Generated by Django 5.0.2 on 2024-03-21 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
