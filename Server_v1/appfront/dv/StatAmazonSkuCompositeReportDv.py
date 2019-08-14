# coding:utf-8

from django.db import models

from django.utils.translation import ugettext as _


'''按SKU统计的每天视图数据'''
class StatAmazonSkuCompositeReportDayDv(models.Model):
    sku = models.CharField(max_length=100, verbose_name= _('SKU'))
    asin = models.CharField(max_length=20, verbose_name= _('Asin'))
    dy = models.DateField(verbose_name=_('Day'), null=True)
    uv_num = models.IntegerField(verbose_name=_('UV'), null=True)
    total_order_items_num = models.IntegerField(verbose_name=_('Total Order Items'), null=True)
    pv_num = models.IntegerField(verbose_name=_('PV'), null=True)
    buy_box_per_num = models.IntegerField(verbose_name=_('Buy Box Percentage'), null=True)

    def __str__(self):
        return _('Sku: %s') % self.sku

    class Meta:
        app_label = "appfront"
        managed = False
        db_table = 'view_i_amazon_sku_composite_report_day'
        ordering = ['sku']
        verbose_name_plural = _('SKU Composite Report for days')


'''按SKU统计的每月视图数据'''
class StatAmazonSkuCompositeReportMonthDv(models.Model):
    sku = models.CharField(max_length=100, verbose_name= _('SKU'))
    asin = models.CharField(max_length=20, verbose_name= _('Asin'))
    yr = models.IntegerField(verbose_name=_('Year'), null=True)
    mo = models.IntegerField(verbose_name=_('Month'), null=True)
    first_day = models.DateField(verbose_name=_('First Day'), null=True)
    last_day = models.DateField(verbose_name=_('Last Day'), null=True)
    uv_num = models.IntegerField(verbose_name=_('UV'), null=True)
    total_order_items_num = models.IntegerField(verbose_name=_('Total Order Items'), null=True)
    pv_num = models.IntegerField(verbose_name=_('PV'), null=True)
    buy_box_per_num = models.IntegerField(verbose_name=_('Buy Box Percentage'), null=True)

    def __str__(self):
        return _('Sku: %s') % self.sku

    class Meta:
        app_label = "appfront"
        managed = False
        db_table = 'view_i_amazon_sku_composite_report_month'
        ordering = ['sku']
        verbose_name_plural = _('SKU Composite Report for moths')


'''按SKU统计的每周视图数据'''
class StatAmazonSkuCompositeReportWeekDv(models.Model):
    sku = models.CharField(max_length=100, verbose_name= _('SKU'))
    asin = models.CharField(max_length=20, verbose_name= _('Asin'))
    yr = models.IntegerField(verbose_name=_('Year'), null=True)
    wk = models.IntegerField(verbose_name=_('Week'), null=True)
    first_day = models.DateField(verbose_name=_('First Day'), null=True)
    last_day = models.DateField(verbose_name=_('Last Day'), null=True)
    uv_num = models.IntegerField(verbose_name=_('UV'), null=True)
    total_order_items_num = models.IntegerField(verbose_name=_('Total Order Items'), null=True)
    pv_num = models.IntegerField(verbose_name=_('PV'), null=True)
    buy_box_per_num = models.IntegerField(verbose_name=_('Buy Box Percentage'), null=True)

    def __str__(self):
        return _('Sku: %s') % self.sku

    class Meta:
        app_label = "appfront"
        managed = False
        db_table = 'view_i_amazon_sku_composite_report_week'
        ordering = ['sku']
        verbose_name_plural = _('SKU Composite Report for weeks')
