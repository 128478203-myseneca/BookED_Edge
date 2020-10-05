# Generated by Django 3.1 on 2020-10-02 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200927_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='course',
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course'),
        ),
        migrations.RemoveField(
            model_name='class',
            name='school',
        ),
        migrations.AddField(
            model_name='class',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.school'),
        ),
        migrations.RemoveField(
            model_name='class',
            name='semester',
        ),
        migrations.AddField(
            model_name='class',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.semester'),
        ),
    ]
