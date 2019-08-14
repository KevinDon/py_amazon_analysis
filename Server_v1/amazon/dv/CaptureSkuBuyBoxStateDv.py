# coding:utf-8

from django.db import models

from django.utils.translation import ugettext as _


class CaptureSkuBuyBoxStateDv(models.Model):
    sku = models.CharField(max_length=100, verbose_name=_('Sku'))
    asin = models.CharField(max_length=100, verbose_name=_('Asin'))
    link = models.CharField(max_length=255, verbose_name=_('Link'))
    buy_box_state = models.IntegerField(verbose_name=_('Buy Box State'), null=True)
    capture_at = models.DateTimeField(verbose_name=_('Capture At'), null=True,)
    sold_by = models.CharField(max_length=255, verbose_name=_('Sold By'))
    sold_by_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Sold By Price'))
    platform = models.CharField(max_length=100, verbose_name=_('Platform'), default='amazon')
    # category_id = models.IntegerField(verbose_name=_('Category'))
    line_id = models.IntegerField(verbose_name=_('Line'))

    def __str__(self):
        return _('Sku: %s') % self.sku

    class Meta:
        app_label = "amazon"
        managed = False
        db_table = 'view_i_amazon_sku_boy_box_state'
        verbose_name_plural = _('SKU Buy Box State')

