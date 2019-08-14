# Generated by Django 2.2 on 2019-07-11 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system', '0006_auto_20190711_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisRuleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('platform', models.CharField(default='amazon', max_length=100, verbose_name='Platform')),
                ('platform_id', models.IntegerField(default=0, editable=False, null=True, verbose_name='Platform Id')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('rule_code', models.UUIDField(help_text='Automatically generated internally by the system', null=True, verbose_name='Analysis Rule Code')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Analysis Rule',
                'verbose_name_plural': 'Analysis Rule',
                'db_table': 'rule_analysis_rule',
            },
        ),
        migrations.CreateModel(
            name='CaptureRuleCookieModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('cookies', models.TextField(max_length=1000, null=True, verbose_name='Cookies')),
                ('expired', models.DateTimeField(null=True, verbose_name='Expire Time')),
            ],
            options={
                'verbose_name': 'Capture Rule Cookie',
                'verbose_name_plural': 'Capture Rule Cookie',
                'db_table': 'rule_capture_rule_cookie',
            },
        ),
        migrations.CreateModel(
            name='CaptureRuleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('platform', models.CharField(default='amazon', max_length=100, verbose_name='Platform')),
                ('platform_id', models.IntegerField(default=0, editable=False, null=True, verbose_name='Platform Id')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('rule_code', models.UUIDField(help_text='Automatically generated internally by the system', null=True, verbose_name='Capture Rule Code')),
                ('delay', models.IntegerField(default=1, null=True, verbose_name='Request Delay')),
                ('max_thread', models.IntegerField(default=6, null=True, verbose_name='Max Thread')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('accept_language', models.CharField(choices=[('en', 'en'), ('en-au', 'en-au'), ('zh-cn', 'zh-cn')], default='en', max_length=64, null=True, verbose_name='Language')),
                ('accept', models.TextField(max_length=1000, null=True, verbose_name='Accept')),
                ('cookies', models.OneToOneField(blank=True, null=True, on_delete=models.SET(''), related_name='capture_cookie', to='rule.CaptureRuleCookieModel', verbose_name='Cookies')),
                ('scrapy_server', models.ForeignKey(null=True, on_delete=models.SET(''), related_name='scrapyserver+', to='system.ServerConfigModel', verbose_name='Scrapy Server')),
            ],
            options={
                'verbose_name': 'Capture Rule',
                'verbose_name_plural': 'Capture Rule',
                'db_table': 'rule_capture_rule',
            },
        ),
        migrations.CreateModel(
            name='CaptureRuleUserAgentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('user_agent', models.TextField(max_length=1000, null=True, verbose_name='UserAgent')),
            ],
            options={
                'verbose_name': 'Capture Rule User Agent',
                'verbose_name_plural': 'Capture Rule User Agent',
                'db_table': 'rule_capture_rule_user_agent',
            },
        ),
        migrations.CreateModel(
            name='CaptureRuleUrlModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('protocol', models.CharField(choices=[('http', 'http'), ('https', 'https')], default='https', max_length=64, null=True, verbose_name='Url Protocol')),
                ('host', models.CharField(max_length=200, null=True, verbose_name='Host')),
                ('path', models.TextField(null=True, verbose_name='Path Params')),
                ('params', models.TextField(null=True, verbose_name='Url Params')),
                ('capture_rule', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='capture_rule', to='rule.CaptureRuleModel', verbose_name='rule')),
            ],
            options={
                'verbose_name': 'Capture Rule Url',
                'verbose_name_plural': 'Capture Rule Url',
                'db_table': 'rule_capture_rule_url',
            },
        ),
        migrations.AddField(
            model_name='capturerulemodel',
            name='user_agent',
            field=models.OneToOneField(blank=True, null=True, on_delete=models.SET(''), related_name='capture_user_agent', to='rule.CaptureRuleUserAgentModel', verbose_name='User Agent'),
        ),
        migrations.CreateModel(
            name='AnalysisRuleItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('match', models.CharField(choices=[('xpath', 'XPath'), ('re', 'Regex'), ('beautiful_soup', 'BeautifulSoup4')], default='xpath', max_length=64, null=True, verbose_name='Match Mode')),
                ('value', models.TextField(null=True, verbose_name='Match')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('analysis_rule', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fetch_rule', to='rule.AnalysisRuleModel', verbose_name='rule')),
            ],
            options={
                'verbose_name': 'Analysis Rule',
                'verbose_name_plural': 'Analysis Rule',
                'db_table': 'rule_analysis_rule_item',
            },
        ),
    ]
