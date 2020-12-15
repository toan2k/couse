# Generated by Django 3.1.4 on 2020-12-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customeruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='address',
            field=models.CharField(default='1', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customeruser',
            name='phone_number',
            field=models.CharField(default='a', max_length=15),
            preserve_default=False,
        ),
    ]
