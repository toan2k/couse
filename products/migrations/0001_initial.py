# Generated by Django 3.1.4 on 2020-12-13 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('slug', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('teaching', models.CharField(default='', max_length=255)),
                ('image_teacher', models.ImageField(default=None, upload_to='static/media/teacher')),
                ('slug', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('image_course', models.ImageField(default=None, upload_to='static/media/course')),
                ('description', models.TextField(default='')),
                ('price', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.teacher')),
            ],
        ),
    ]