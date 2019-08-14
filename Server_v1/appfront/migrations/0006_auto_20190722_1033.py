# Generated by Django 2.2 on 2019-07-22 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfront', '0005_auto_20190716_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='productasinmodel',
            name='purchase_id',
            field=models.CharField(editable=False, max_length=200, null=True, verbose_name='Purchase Item ID'),
        ),
        migrations.AddField(
            model_name='productlinemodel',
            name='purchase_id',
            field=models.CharField(editable=False, max_length=200, null=True, verbose_name='Purchase Item ID'),
        ),
        migrations.AddField(
            model_name='productlinemodel',
            name='purchase_parent_id',
            field=models.CharField(editable=False, max_length=200, null=True, verbose_name='Purchase Item Parent ID'),
        ),
    ]
