# Generated by Django 4.1.13 on 2023-11-26 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]