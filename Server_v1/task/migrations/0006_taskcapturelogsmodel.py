# Generated by Django 2.2.3 on 2019-07-15 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cronjob', '0007_auto_20190715_1704'),
        ('task', '0005_taskmessagelistmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCaptureLogsModel',
            fields=[
            ],
            options={
                'verbose_name': 'Capture Logs',
                'verbose_name_plural': 'Capture Logs',
                'managed': False,
                'proxy': True,
            },
            bases=('cronjob.cronjoblogsmodel',),
        ),
    ]
