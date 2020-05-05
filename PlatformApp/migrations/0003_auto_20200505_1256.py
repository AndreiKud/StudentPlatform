# Generated by Django 3.0.5 on 2020-05-05 07:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PlatformApp', '0002_auto_20200505_0638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studyproject',
            old_name='content',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='studyproject',
            name='author',
        ),
        migrations.AddField(
            model_name='studyproject',
            name='customer',
            field=models.CharField(default='empty', max_length=100),
        ),
        migrations.AddField(
            model_name='studyproject',
            name='date_deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='studyproject',
            name='executor',
            field=models.CharField(default='empty', max_length=100),
        ),
        migrations.AddField(
            model_name='studyproject',
            name='result',
            field=models.CharField(default='empty', max_length=100),
        ),
    ]