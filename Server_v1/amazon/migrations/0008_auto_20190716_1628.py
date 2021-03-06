# Generated by Django 2.2.3 on 2019-07-16 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0007_auto_20190716_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategorymodel',
            name='code',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='Category Code'),
        ),
        migrations.AddField(
            model_name='productcategorymodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='amazon.ProductCategoryModel'),
        ),
    ]
