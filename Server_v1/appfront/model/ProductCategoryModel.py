from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import *
from manager.model.CommonModel import CommonModel, PurchaseParentResourceMixin
from amazon.model import AmazonProductCategoryModel as AmazonCate


class ProductCategoryModel(CommonModel, PurchaseParentResourceMixin):
    code = models.CharField(_('Category Code'), max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    level = models.IntegerField(default=0, verbose_name=_('Level'))

    amazon_category = models.ManyToManyField(AmazonCate, related_name='amazon_category', verbose_name=_('Amazon Category'), editable=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "appfront"
        db_table = 'pub_product_category'
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Category")


class ProductCategoryLogModel(CommonModel):

    class Meta:
        app_label = "appfront"
        db_table = 'pub_product_category_mod_log'
        verbose_name = _("Product Category Modify Log")
        verbose_name_plural = _("Product Category  Modify Logs")

    category = models.CharField(null=True, max_length=100, verbose_name=_('Product Category'))
    modify_fields = models.CharField(null=True, max_length=200, verbose_name=_('Modify Field'))
    old_val = models.TextField(null=True, verbose_name=_('Old Value'))
    new_val = models.TextField(null=True, verbose_name=_('New Value'))

    def __str__(self):
        return 'Modify %s' % self.category

