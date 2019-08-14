# coding:utf-8

from django.db import models

from django.utils.translation import ugettext as _


'''按Line统计的每天视图数据'''
class StatAmazonLineUvItemsConversionRateDayDv(models.Model):
    line_id = models.IntegerField(verbose_name= _('Line_ID'), null=True)
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    dy = models.DateField(verbose_name=_('Day'), null=True)
    num = models.FloatField(verbose_name=_('Count'), null=True)

    def __str__(self):
        return _('Line: %s') % self.title

    class Meta:
        app_label = "appfront"
        managed = False
        db_table = 'view_i_amazon_line_uv_items_conversion_rate_day'
        ordering = ['line_id']
        verbose_name_plural = _('Line Items/UV for days')
