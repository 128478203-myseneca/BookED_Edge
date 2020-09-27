# Generated by Django 3.1.1 on 2020-09-27 03:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200926_2248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'Courses'},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='all_classes',
            new_name='classes',
        ),
        migrations.RemoveField(
            model_name='class',
            name='books',
        ),
        migrations.RemoveField(
            model_name='class',
            name='classes',
        ),
        migrations.RemoveField(
            model_name='course',
            name='courses',
        ),
        migrations.AddField(
            model_name='book',
            name='classes',
            field=models.ManyToManyField(to='main.Class'),
        ),
        migrations.AddField(
            model_name='course',
            name='choices_course',
            field=models.CharField(choices=[('Computer Programming', 'Computer Programming'), ('Database Application Developer', 'Database Application Developer'), ('Mechanical Technician', 'Mechanical Technician'), ('Law Clerk', 'Law Clerk')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='Year',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
