# coding:utf-8

from django.db import models

from django.utils.translation import ugettext as _


class CaptureSkuReviewDv(models.Model):
    sku = models.CharField(max_length=100, verbose_name=_('Sku'))
    asin = models.CharField(max_length=100, verbose_name=_('Asin'))
    review_at = models.DateTimeField(verbose_name=_('Review At'))
    review_rank = models.CharField(max_length=10, verbose_name=_('Review Rank'))
    author = models.CharField(max_length=50, verbose_name=_('Author'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    content = models.TextField(max_length=10000, verbose_name=_('Content'))
    selection = models.CharField(max_length=100, verbose_name=_('Selection'))
    link = models.CharField(max_length=255, verbose_name=_('Link'))
    platform = models.CharField(max_length=100, verbose_name=_('Platform'), default='amazon')
    # category_id = models.IntegerField(verbose_name=_('Category'))
    line_id = models.IntegerField(verbose_name=_('Line'))

    def __str__(self):
        return _('Sku: %s') % self.sku

    class Meta:
        app_label = "amazon"
        managed = False
        db_table = 'view_i_amazon_sku_review'
        verbose_name_plural = _('SKU Review')

