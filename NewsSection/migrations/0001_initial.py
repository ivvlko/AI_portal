# Generated by Django 3.1.3 on 2020-11-08 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=3000)),
                ('category', models.CharField(choices=[['Computer Vision and Images', 'Computer Vision and Images'], ['Natural Language Processing', 'Natural Language Processing'], ['Robotics', 'Robotics'], ['Hardware and Innovations', 'Hardware and Innovations']], max_length=50)),
                ('img_url', models.URLField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
