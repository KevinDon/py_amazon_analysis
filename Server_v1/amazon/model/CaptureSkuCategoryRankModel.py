from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import *
from amazon.model import AmazonProductCategoryModel
from manager.model.CommonModel import CommonModel, PlatformMixin


class CaptureSkuCategoryRankModel(CommonModel, PlatformMixin):
    sku = models.CharField(max_length=100, verbose_name=_('Sku'))
    asin = models.CharField(max_length=100, verbose_name=_('Asin'))
    category = models.ForeignKey(AmazonProductCategoryModel, on_delete=models.CASCADE,
                                 related_name='category+', editable=False, null=True, verbose_name=_('Category'))
    category_title = models.CharField(max_length=100, verbose_name=_('Category Title'))
    rank_on = models.IntegerField(default=0, verbose_name=_('Rank On'))
    rank_page = models.IntegerField(default=0, verbose_name=_('Rank Page'))
    capture_at = models.DateTimeField(verbose_name=_('Capture At'), null=True)
    link = models.CharField(max_length=255, verbose_name=_('Link'), null=True)

    def __str__(self):
        return self.sku

    class Meta:
        app_label = "amazon"
        db_table = 'amazon_capture_sku_category_rank'
        verbose_name = _("Sku Category Rank")
        verbose_name_plural = _("Sku Category Rank")