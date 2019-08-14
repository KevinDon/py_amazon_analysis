from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import *

from amazon.model.SkuKeywordModel import SkuKeywordModel
from manager.model.CommonModel import CommonModel, PlatformMixin


class AmazonProductCategoryModel(CommonModel, PlatformMixin):
    code = models.CharField(_('Category Code'), max_length=100, blank=True, unique=True)
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    url_alias = models.CharField(null=True, max_length=200, verbose_name=_('Url Alias'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=1)
    level = models.IntegerField(default=0, verbose_name=_('Level'))

    keyword = models.ManyToManyField(SkuKeywordModel, verbose_name=_('Keyword'), through='AmazonProductCategoryKeywordRelation')

    def __str__(self):
        return self.title

    class Meta:
        app_label = "amazon"
        db_table = 'amazon_product_category'
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Category")


class AmazonProductCategoryLogModel(CommonModel):
    class Meta:
        app_label = "amazon"
        db_table = 'amazon_product_category_mod_log'
        verbose_name = _("Product Category Modify Log")
        verbose_name_plural = _("Product Category  Modify Logs")

    category = models.CharField(null=True, max_length=100, verbose_name=_('Product Category'))
    modify_fields = models.CharField(null=True, max_length=200, verbose_name=_('Modify Field'))
    old_val = models.TextField(null=True, verbose_name=_('Old Value'))
    new_val = models.TextField(null=True, verbose_name=_('New Value'))

    def __str__(self):
        return 'Modify %s' % self.category


class AmazonProductCategoryKeywordRelation(models.Model):
    class Meta:
        auto_created = True
        db_table = "amazon_product_category_keyword_relation"

    amazon_keyword = models.ForeignKey(SkuKeywordModel, null=True, on_delete=models.CASCADE, verbose_name=_('Amazon Keyword'))
    amazon_category = models.ForeignKey(AmazonProductCategoryModel, null=True, on_delete=models.CASCADE, verbose_name=_('Amazon Category'))
