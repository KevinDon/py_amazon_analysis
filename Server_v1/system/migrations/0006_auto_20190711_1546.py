# Generated by Django 2.2 on 2019-07-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_taskmessagelistmodel'),
        ('system', '0005_auto_20190711_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetemplatemodel',
            name='cronjob',
            field=models.ForeignKey(on_delete=models.SET(0), related_name='cronjob+', to='task.TaskMessageListModel', verbose_name='Cronjob'),
        ),
    ]
