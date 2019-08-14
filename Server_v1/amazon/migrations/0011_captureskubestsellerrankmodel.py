# Generated by Django 2.2.3 on 2019-07-23 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0010_auto_20190723_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaptureSkuBestsellerRankModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update At')),
                ('creator_id', models.IntegerField(editable=False, null=True, verbose_name='Creator')),
                ('status', models.IntegerField(choices=[(1, 'Enabled'), (2, 'Disabled')], default=1, null=True, verbose_name='Status')),
                ('sort', models.IntegerField(default=0, null=True, verbose_name='Sort')),
                ('platform', models.CharField(default='amazon', max_length=100, verbose_name='Platform')),
                ('platform_id', models.IntegerField(default=0, editable=False, null=True, verbose_name='Platform Id')),
                ('sku', models.CharField(max_length=100, verbose_name='Sku')),
                ('asin', models.CharField(max_length=100, verbose_name='Asin')),
                ('link', models.CharField(max_length=255, null=True, verbose_name='Link')),
                ('capture_at', models.DateTimeField(null=True, verbose_name='Capture At')),
                ('category_title', models.CharField(max_length=100, verbose_name='Category Title')),
                ('rank_on', models.IntegerField(default=0, verbose_name='Rank On')),
                ('rank_page', models.IntegerField(default=0, verbose_name='Rank Page')),
                ('category', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category+', to='amazon.AmazonProductCategoryModel', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Sku Bestseller Rank',
                'verbose_name_plural': 'Sku Bestseller Rank',
                'db_table': 'amazon_capture_sku_bestseller_rank',
            },
        ),
    ]