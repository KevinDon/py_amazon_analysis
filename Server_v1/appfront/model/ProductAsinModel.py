# coding:utf-8
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from appfront.model import ProductCategoryModel as PubCate
from amazon.model import AmazonProductCategoryModel as AmazonCate, SkuKeywordModel
from .ProductLineModel import ProductLineModel as Line
from manager.model.CommonModel import CommonModel, PlatformMixin, PurchaseResourceMixin


class ProductAsinModel(CommonModel, PlatformMixin, PurchaseResourceMixin):
    """ Product Asin Model """

    # todo 转数据字典
    CHOICES_COMBINE_TYPE = ((1, _('Single SKU')),
                            (2, _('Combo SKU')),
                            (3, _('Variation SKU')),
                            (4, _('FBA SKU')),
                            (5, _('Parent SKU')),)

    sku = models.CharField(max_length=100, verbose_name=_('SKU'))
    asin = models.CharField(max_length=20, verbose_name=_('Asin'), null=True, help_text=_('Amazon Platform Product Code'))

    department = models.ForeignKey('manager.DepartmentModel', null=True, verbose_name=_('Department'), on_delete=models.SET_NULL)

    combine_type = models.IntegerField(null=True, default=1, verbose_name=_('Product Combine Type'), choices=CHOICES_COMBINE_TYPE)
    combine_relation = models.ManyToManyField('appfront.ProductAsinModel', verbose_name=_('Product Combine Relation'), related_name='combine_product_relation', through='ProductAsinCombineRelationModel')

    amazon_category = models.ManyToManyField(AmazonCate, verbose_name=_('Amazon Category'), editable=True)
    line = models.ForeignKey(Line, verbose_name=_('Line'), on_delete=models.SET_NULL, editable=True,
                             null=True)

    category = models.ManyToManyField(PubCate, verbose_name=_('Category'), editable=True, through='ProductCategoryRelationModel')
    keyword = models.ManyToManyField(SkuKeywordModel, verbose_name=_('Keyword'), through='ProductAsinSkuKeywordRelation')

    def __str__(self):
        return _('SKU: %s') % self.sku

    class Meta:
        app_label = "appfront"
        db_table = 'na_product_asin'
        # unique_together = ('-created_at', 'sku',)
        verbose_name = _('Product Asin')
        verbose_name_plural = _('Product Asin')

    @staticmethod
    def skuGet(request, **kwargs):
        sku_list = ProductAsinModel.objects.filter(kwargs.get('filters')).values('sku', 'asin', 'category').distinct()
        return list(sku_list)


class ProductAsinCombineRelationModel(models.Model):
    class Meta:
        auto_created = True
        db_table = "na_product_asin_combine_relation"

    product = models.ForeignKey(ProductAsinModel, null=True, verbose_name=_('Combine Product Id'), related_name='product_id', on_delete=models.CASCADE)
    related_product = models.ForeignKey(ProductAsinModel, null=True, verbose_name=_('Related Product Id'), related_name='related_product_id', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ProductCategoryRelationModel(models.Model):
    product = models.ForeignKey(ProductAsinModel, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(PubCate, null=True, on_delete=models.CASCADE)
    update_at = models.DateTimeField(auto_now=timezone.now)

    purchase_product_id = models.CharField(null=True, max_length=200, verbose_name=_('Purchase Product Id'))
    purchase_category_id = models.CharField(null=True, max_length=200, verbose_name=_('Purchase Product Id'))

    class Meta:
        db_table = "pub_product_asin_category_relation"


class ProductAsinSkuKeywordRelation(models.Model):
    product = models.ForeignKey(ProductAsinModel, related_name='keyword_product_relation', null=True, on_delete=models.CASCADE)
    keyword = models.ForeignKey(SkuKeywordModel, null=True, on_delete=models.CASCADE)
    update_at = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        auto_created = True
        db_table = "pub_product_asin_keyword_relation"


class ProductAsinLogModel(CommonModel):
    class Meta:
        app_label = "appfront"
        db_table = 'na_product_mod_log'
        verbose_name = _("Product Modify Log")
        verbose_name_plural = _("Product Modify Logs")

    sku = models.CharField(null=True, max_length=100, verbose_name=_('Product SKU'))
    modify_fields = models.CharField(null=True, max_length=200, verbose_name=_('Modify Field'))
    old_val = models.TextField(null=True, verbose_name=_('Old Value'))
    new_val = models.TextField(null=True, verbose_name=_('New Value'))

    def __str__(self):
        return 'Modify %s' % self.sku
