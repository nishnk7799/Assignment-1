# Generated by Django 2.2.2 on 2020-06-20 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_auto_20200613_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='register',
            name='phone',
        ),
    ]