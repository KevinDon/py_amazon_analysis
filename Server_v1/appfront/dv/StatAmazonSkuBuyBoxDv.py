# coding:utf-8

from django.db import models

from django.utils.translation import ugettext as _


'''按SKU统计的每天视图数据'''
class StatAmazonSkuBuyBoxDayDv(models.Model):
    sku = models.CharField(max_length=100, verbose_name= _('SKU'))
    asin = models.CharField(max_length=20, verbose_name= _('Asin'))
    dy = models.DateField(verbose_name=_('Day'), null=True)
    num = models.IntegerField(verbose_name=_('Count'), null=True)

    def __str__(self):
        return _('Sku: %s') % self.sku

    class Meta:
        app_label = "appfront"
        managed = False
        db_table = 'view_i_amazon_sku_buy_box_day'
        ordering = ['sku']
        verbose_name_plural = _('SKU Buy Box for days')
