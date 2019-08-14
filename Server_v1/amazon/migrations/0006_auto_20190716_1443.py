# Generated by Django 2.2.3 on 2019-07-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0005_merge_20190712_1339'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductAsinLogModel',
        ),
        migrations.AlterField(
            model_name='captureskubuyboxstatemodel',
            name='capture_at',
            field=models.DateTimeField(null=True, verbose_name='Capture At'),
        ),
        migrations.AlterField(
            model_name='captureskucategoryrankmodel',
            name='capture_at',
            field=models.DateTimeField(null=True, verbose_name='Capture At'),
        ),
        migrations.AlterField(
            model_name='captureskukeywordrankmodel',
            name='capture_at',
            field=models.DateTimeField(null=True, verbose_name='Capture At'),
        ),
        migrations.AlterField(
            model_name='captureskupricemodel',
            name='capture_at',
            field=models.DateTimeField(null=True, verbose_name='Capture At'),
        ),
        migrations.AlterField(
            model_name='captureskureviewmodel',
            name='capture_at',
            field=models.DateTimeField(null=True, verbose_name='Capture At'),
        ),
        migrations.AlterField(
            model_name='captureskureviewmodel',
            name='version',
            field=models.IntegerField(default=1, editable=False, verbose_name='Version'),
        ),
        migrations.AlterModelTable(
            name='productcategorylogmodel',
            table='amazon_product_category_mod_log',
        ),
        migrations.AlterModelTable(
            name='productcategorymodel',
            table='amazon_product_category',
        ),
    ]
