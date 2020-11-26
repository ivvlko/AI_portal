# Generated by Django 3.1.3 on 2020-11-21 18:50

import NewsSection.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsSection', '0015_auto_20201118_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(max_length=3000, validators=[NewsSection.validators.only_english_validator, django.core.validators.MinValueValidator(100)]),
        ),
    ]
