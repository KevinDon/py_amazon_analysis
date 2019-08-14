# Generated by Django 2.1.5 on 2019-07-04 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20190704_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyIpLogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('platform', models.CharField(default='amazon', max_length=100, verbose_name='Platform')),
                ('platform_id', models.IntegerField(default=0, editable=False, null=True, verbose_name='Platform Id')),
                ('proxy_ip', models.CharField(max_length=15, null=True, verbose_name='Proxy Ip')),
                ('proxy_port', models.CharField(max_length=6, null=True, verbose_name='Proxy Port')),
                ('agent_type', models.IntegerField(choices=[(1, 'Third'), (2, 'Inner'), (3, 'Other')], default=1, null=True, verbose_name='Agent Type')),
                ('request_content', models.TextField(max_length=10000, null=True, verbose_name='Request Content')),
                ('response_result', models.TextField(max_length=10000, null=True, verbose_name='Response Result')),
                ('call_state', models.IntegerField(choices=[(1, 'Success'), (2, 'Failed')], default=1, null=True, verbose_name='Call State')),
            ],
            options={
                'verbose_name': 'Proxy Ip Run Log',
                'verbose_name_plural': 'Proxy Ip Run Log',
                'db_table': 'system_proxy_ip_log',
            },
        ),
    ]
