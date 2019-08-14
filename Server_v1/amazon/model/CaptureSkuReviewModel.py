from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import *
from manager.model.CommonModel import CommonModel, PlatformMixin


class CaptureSkuReviewModel(CommonModel, PlatformMixin):
    sku = models.CharField(max_length=100, verbose_name=_('Sku'))
    asin = models.CharField(max_length=100, verbose_name=_('Asin'))
    review_id = models.CharField(max_length=100, verbose_name=_('Review Id'), null=True)
    review_at = models.DateTimeField(verbose_name=_('Review At'), null=True)
    review_rank = models.CharField(max_length=10, verbose_name=_('Review Rank'), null=True)
    author = models.CharField(max_length=100, verbose_name=_('Author'), null=True)
    title = models.CharField(max_length=100, verbose_name=_('Title'), null=True)
    content = models.TextField(max_length=10000, verbose_name=_('Content'), null=True)
    selection = models.CharField(max_length=100, verbose_name=_('Selection'))
    link = models.CharField(max_length=255, verbose_name=_('Link'), null=True)
    capture_at = models.DateTimeField(verbose_name=_('Capture At'), null=True)

    def __str__(self):
        return self.sku

    class Meta:
        app_label = "amazon"
        db_table = 'amazon_capture_sku_review'
        verbose_name = _("Sku Review")
        verbose_name_plural = _("Sku Review")