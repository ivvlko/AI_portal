# Generated by Django 3.1.3 on 2020-11-16 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsSection', '0009_auto_20201116_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='text2',
        ),
    ]
