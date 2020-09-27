# Generated by Django 3.1 on 2020-09-22 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post_sponsored'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name_plural': 'Schools'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='school',
        ),
        migrations.AddField(
            model_name='post',
            name='schools',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.school'),
        ),
        migrations.AddField(
            model_name='school',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.school'),
        ),
        migrations.AddField(
            model_name='school',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='school',
            unique_together={('slug', 'parent')},
        ),
    ]
