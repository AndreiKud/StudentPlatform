# Generated by Django 2.2.12 on 2020-05-26 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlatformApp', '0006_auto_20200526_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyproject',
            name='attached_file',
            field=models.FileField(blank=True, null=True, upload_to='proj_files', verbose_name='Прикрепленные файлы'),
        ),
        migrations.AlterField(
            model_name='studyproject',
            name='customer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_customer', to=settings.AUTH_USER_MODEL, verbose_name='Заказчик'),
        ),
        migrations.AlterField(
            model_name='studyproject',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='studyproject',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_executor', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
    ]
