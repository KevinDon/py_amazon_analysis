from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import *
from manager.model.CommonModel import CommonModel, PlatformMixin
from amazon.model import AmazonProductCategoryModel


class CaptureSkuBestsellerRankModel(CommonModel, PlatformMixin):
    sku = models.CharField(max_length=100, verbose_name=_('Sku'))
    asin = models.CharField(max_length=100, verbose_name=_('Asin'))
    link = models.CharField(max_length=255, verbose_name=_('Link'), null=True)
    capture_at = models.DateTimeField(verbose_name=_('Capture At'), null=True)
    category = models.ForeignKey(AmazonProductCategoryModel, on_delete=models.CASCADE,
                                 related_name='category+', editable=False, null=True, verbose_name=_('Category'))
    category_title = models.CharField(max_length=100, verbose_name=_('Category Title'))
    rank_on = models.IntegerField(default=0, verbose_name=_('Rank On'))
    rank_page = models.IntegerField(default=0, verbose_name=_('Rank Page'))

    def __str__(self):
        return self.sku

    class Meta:
        app_label = "amazon"
        db_table = 'amazon_capture_sku_bestseller_rank'
        verbose_name = _("Sku Bestseller Rank")
        verbose_name_plural = _("Sku Bestseller Rank")