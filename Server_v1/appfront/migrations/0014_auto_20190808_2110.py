# Generated by Django 2.2 on 2019-08-08 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('manager', '0002_departmentmodel_purchase_id'),
        ('appfront', '0013_auto_20190807_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='productasinmodel',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.DepartmentModel', verbose_name='Department'),
        ),
    ]
