# Generated by Django 3.1.4 on 2020-12-15 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_course_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='inventory',
        ),
    ]
