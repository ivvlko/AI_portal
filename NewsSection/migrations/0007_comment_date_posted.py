# Generated by Django 3.1.3 on 2020-11-16 09:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('NewsSection', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
