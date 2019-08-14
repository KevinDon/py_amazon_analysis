from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from manager.model.CommonModel import CommonModel, PlatformMixin, PurchaseParentResourceMixin


class ProductLineModel(CommonModel, PlatformMixin, PurchaseParentResourceMixin):
    """Product Line Model"""
    title = models.CharField(max_length=100, verbose_name=_('Title'), null=True)
    code = models.CharField(max_length=255, verbose_name=_('Code'), null=True, unique=True)
    parent = models.ForeignKey('self', verbose_name=_('Parent Line'), editable=True,
                               on_delete=models.CASCADE, blank=True, null=True)
    describe = models.CharField(max_length=255, verbose_name=_('Describe'), null=True)

    def __str__(self):
        return _('SKU Line: %s') % self.title

    class Meta:
        app_label = "appfront"
        db_table = "na_product_line"
        verbose_name = _("Product Line")
        verbose_name_plural = _("Product Line")
