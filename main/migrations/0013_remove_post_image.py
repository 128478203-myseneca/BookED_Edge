# Generated by Django 3.1 on 2020-09-23 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
