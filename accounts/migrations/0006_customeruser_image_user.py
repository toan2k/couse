# Generated by Django 3.1.4 on 2020-12-15 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='image_user',
            field=models.ImageField(default=None, upload_to='static/media/user'),
        ),
    ]