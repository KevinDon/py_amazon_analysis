# Generated by Django 2.2.3 on 2019-07-11 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cronjob', '0003_auto_20190710_1124'),
        ('task', '0004_auto_20190711_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskMessageListModel',
            fields=[
            ],
            options={
                'verbose_name': 'Message List',
                'verbose_name_plural': 'Message List',
                'managed': False,
                'proxy': True,
            },
            bases=('cronjob.cronjobmodel',),
        ),
    ]