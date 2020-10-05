# Generated by Django 3.1 on 2020-10-05 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_book_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='course',
        ),
        migrations.RemoveField(
            model_name='class',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='course',
            name='school',
        ),
        migrations.AddField(
            model_name='book',
            name='book_img',
            field=models.ImageField(default='default.jpg', upload_to='books_image'),
        ),
    ]
