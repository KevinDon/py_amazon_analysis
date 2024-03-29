# Generated by Django 2.2 on 2019-07-31 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0011_captureskubestsellerrankmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatAmazonSkuBestsellerRankDayDv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=100, verbose_name='Asin')),
                ('sku', models.CharField(max_length=100, verbose_name='Sku')),
                ('category_id', models.IntegerField(verbose_name='Category Id')),
                ('dy', models.DateField(null=True, verbose_name='Day')),
                ('num', models.IntegerField(null=True, verbose_name='Count')),
            ],
            options={
                'verbose_name_plural': 'Keyword Rank for days',
                'db_table': 'view_i_amazon_sku_bestseller_rank_day',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StatAmazonSkuBestsellerRankMonthDv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=100, verbose_name='Asin')),
                ('sku', models.CharField(max_length=100, verbose_name='Sku')),
                ('category_id', models.IntegerField(verbose_name='Category Id')),
                ('yr', models.IntegerField(null=True, verbose_name='Year')),
                ('mo', models.IntegerField(null=True, verbose_name='Month')),
                ('first_day', models.DateField(null=True, verbose_name='First Day')),
                ('last_day', models.DateField(null=True, verbose_name='Last Day')),
                ('num', models.IntegerField(null=True, verbose_name='Count')),
            ],
            options={
                'verbose_name_plural': 'Keyword Rank for months',
                'db_table': 'view_i_amazon_sku_bestseller_rank_month',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StatAmazonSkuBestsellerRankWeekDv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=100, verbose_name='Asin')),
                ('sku', models.CharField(max_length=100, verbose_name='Sku')),
                ('category_id', models.IntegerField(verbose_name='Category Id')),
                ('yr', models.IntegerField(null=True, verbose_name='Year')),
                ('wk', models.IntegerField(null=True, verbose_name='Week')),
                ('first_day', models.DateField(null=True, verbose_name='First Day')),
                ('last_day', models.DateField(null=True, verbose_name='Last Day')),
                ('num', models.IntegerField(null=True, verbose_name='Count')),
            ],
            options={
                'verbose_name_plural': 'Keyword Rank for weeks',
                'db_table': 'view_i_amazon_sku_bestseller_rank_week',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='skukeywordmodel',
            name='keyword_type',
            field=models.IntegerField(choices=[(1, 'Sku Keyword'), (2, 'Category Keyword')], default=1, null=True, verbose_name='Keyword Type'),
        ),
    ]
