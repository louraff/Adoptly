# Generated by Django 4.2.2 on 2023-06-24 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_alter_petimage_pet_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petimage',
            name='photo',
        ),
    ]
