# Generated by Django 2.2 on 2019-07-02 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataDictionaryCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True,
                                               verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('platform', models.CharField(default='amazon', max_length=100, verbose_name='Platform')),
                ('platform_id', models.IntegerField(default=0, editable=False, null=True, verbose_name='Platform Id')),
                ('code', models.CharField(max_length=100, null=True, unique=True, verbose_name='Code')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('data_type',
                 models.IntegerField(choices=[(1, 'data'), (2, 'config')], default=1, null=True,
                                     verbose_name='Type')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=models.SET(0),
                                             to='dictionary.DataDictionaryCategoryModel', verbose_name='Parent Cate')),
            ],
            options={
                'verbose_name': 'Dict Category',
                'verbose_name_plural': 'Dict Category',
                'db_table': 'pub_data_dictionary_category',
            },
        ),
        migrations.CreateModel(
            name='DataDictionaryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True,
                                               verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('platform', models.CharField(default='amazon', max_length=100, verbose_name='Platform')),
                ('platform_id', models.IntegerField(default=0, editable=False, null=True, verbose_name='Platform Id')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title')),
                ('code_main', models.CharField(max_length=64, null=True, verbose_name='Main Code')),
                ('code_sub', models.CharField(max_length=64, null=True, verbose_name='Sub Code')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('type', models.IntegerField(choices=[(1, 'Single'), (2, 'Enum')], default=1, null=True,
                                             verbose_name='Dictionary Type')),
                ('category',
                 models.ForeignKey(blank=True, default=0, null=True, on_delete=models.SET(0), related_name='dicts',
                                   to='dictionary.DataDictionaryCategoryModel', verbose_name='Dict Category')),
            ],
            options={
                'verbose_name': 'Dict',
                'verbose_name_plural': 'Dict',
                'db_table': 'pub_data_dictionary',
            },
        ),
        migrations.CreateModel(
            name='DataDictionaryValueModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True,
                                               verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('platform', models.CharField(default='amazon', max_length=100, verbose_name='Platform')),
                ('platform_id', models.IntegerField(default=0, editable=False, null=True, verbose_name='Platform Id')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Dict Value Title')),
                ('value', models.CharField(max_length=255, null=True, verbose_name='Dict Value')),
                ('type',
                 models.IntegerField(choices=[(1, 'Text'), (2, 'ImageBase64'), (3, 'Url')], default=1, null=True,
                                     verbose_name='Dict Type')),
                ('is_default', models.BooleanField(default=False, verbose_name='Default Value')),
                ('dict',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dict_values',
                                   to='dictionary.DataDictionaryModel', verbose_name='Dictionary')),
            ],
            options={
                'verbose_name': 'Dict Value',
                'verbose_name_plural': 'Dict Value',
                'db_table': 'pub_data_dictionary_value',
            },
        ),
    ]