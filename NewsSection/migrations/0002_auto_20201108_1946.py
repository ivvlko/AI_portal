# Generated by Django 3.1.3 on 2020-11-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsSection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[['Computer Vision and Images', 'Computer Vision and Images'], ['Natural Language Processing', 'Natural Language Processing'], ['Robotics', 'Robotics']], max_length=50),
        ),
    ]
