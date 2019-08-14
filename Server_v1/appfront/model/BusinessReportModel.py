# coding:utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

class BusinessReportModel(models.Model):
    asin_parent = models.CharField(max_length=20, verbose_name= _('Asin Parent'), null=True)
    asin_child = models.CharField(max_length=20, verbose_name= _('Asin Child'), null=True)
    title = models.CharField(max_length=255, verbose_name= _('Title'), null=True)
    sessions = models.IntegerField(default=0, verbose_name= _('UV'), null=True)
    sessions_percentage = models.FloatField(default=0, verbose_name= _('UV per.'), null=True)
    page_view = models.IntegerField(default=0, verbose_name= _('PV'), null=True)
    page_view_percentage = models.FloatField(default=0, verbose_name= _('PV per.'), null=True)
    buy_box_percentage = models.FloatField(default=0, verbose_name= _('Buy Box per.'), null=True)
    units_ordered = models.IntegerField(default=0, verbose_name= _('Units Ordered'), null=True)
    unit_session_percentage = models.FloatField(default=0, verbose_name= _('Unit UV per.'), null=True)
    ordered_product_sales = models.FloatField(default=0, verbose_name= _('Ordered Product'), null=True)
    total_order_items = models.IntegerField(default=0, verbose_name=_('Total Order Items'), null=True)
    report_date = models.DateTimeField(verbose_name= _('Report Date'), null=True, auto_now=True)
    created_at = models.DateTimeField(verbose_name=_('Created At'), null=True, auto_now_add=True)

    def __str__(self):
        return _('ASIN: %s') % self.asin_child

    class Meta:
        app_label = "appfront"
        db_table = 'na_business_report'
        # unique_together = ('-report_date', 'asin_child',)
        verbose_name = _('Business Report')
        verbose_name_plural = _('Business Report')
