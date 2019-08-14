from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import *
from manager.model.CommonModel import CommonModel, PlatformMixin


class CaptureSkuBuyBoxStateModel(CommonModel, PlatformMixin):
    CHOICES_STATE = ((1, _('Occupy')), (2, _('No Occupy')))

    sku = models.CharField(max_length=100, verbose_name=_('Sku'))
    asin = models.CharField(max_length=100, verbose_name=_('Asin'))
    link = models.CharField(max_length=255, verbose_name=_('Link'), null=True)
    buy_box_state = models.IntegerField(choices=CHOICES_STATE, default=2,
                                        verbose_name=_('Buy Box State'), null=True)
    capture_at = models.DateTimeField(verbose_name=_('Capture At'), null=True)
    sold_by = models.CharField(max_length=100, verbose_name=_('Sold By'))
    sold_by_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Sold By Price'))

    def __str__(self):
        return self.sku

    class Meta:
        app_label = "amazon"
        db_table = 'amazon_capture_sku_buy_box_state'
        verbose_name = _("Sku Buy Box State")
        verbose_name_plural = _("Sku Buy Box State")