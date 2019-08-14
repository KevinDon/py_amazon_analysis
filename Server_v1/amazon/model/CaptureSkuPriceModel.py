from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import *
from manager.model.CommonModel import CommonModel, PlatformMixin


class CaptureSkuPriceModel(CommonModel, PlatformMixin):
    sku = models.CharField(max_length=100, verbose_name=_('Sku'))
    asin = models.CharField(max_length=100, verbose_name=_('Asin'))
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=_('Price'), null=True)
    link = models.CharField(max_length=255, verbose_name=_('Link'), null=True)
    capture_at = models.DateTimeField(verbose_name=_('Capture At'), null=True)

    def __str__(self):
        return self.sku

    class Meta:
        app_label = "amazon"
        db_table = 'amazon_capture_sku_price'
        verbose_name = _("Sku Price Log")
        verbose_name_plural = _("Sku Price Log")