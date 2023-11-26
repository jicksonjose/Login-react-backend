# Generated by Django 4.1.13 on 2023-11-26 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
