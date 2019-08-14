# coding:utf-8

from django import forms
from django.db.models import Q

from amazon.model import SkuKeywordModel
from appfront.model import ProductAsinModel, ProductCategoryModel
from manager.forms import CommonModelForm
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext as _


class ProductAsinForm(CommonModelForm):
    require_fields = ('sku')

    class Meta:
        model = ProductAsinModel
        fields = '__all__'

    # 自定义 ProductAsinCombineField
    combine_related_product_list = forms.ModelMultipleChoiceField(
        queryset=ProductAsinModel.objects.exclude(Q(status=3)),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Combine Related Product'),
            is_stacked=True
        )
    )

    # 自定义 ProductCategoryField 是个过滤型多选
    category_list = forms.ModelMultipleChoiceField(
        queryset=ProductCategoryModel.objects.exclude(Q(status=3)),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Product Category'),
            is_stacked=True
        )
    )

    # 自定义 Product keyword 是个过滤型多选
    keyword_list = forms.ModelMultipleChoiceField(
        queryset=SkuKeywordModel.objects.exclude(Q(status=3)),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Product Keyword'),
            is_stacked=True
        )
    )

    def __init__(self, *args, **kwargs):
        super(ProductAsinForm, self).__init__(*args, **kwargs)
        _instance = kwargs.get('instance')
        if _instance:
            # 实例化赋值
            self.fields["category_list"].initial = _instance.category.exclude(Q(status=3))
            self.fields["keyword_list"].initial = _instance.keyword.exclude(Q(status=3))
            self.fields["combine_related_product_list"].initial = _instance.combine_relation.exclude(Q(status=3))
        self.fields["amazon_category"].widget.choices.queryset = self.fields["amazon_category"].widget.choices.queryset.exclude(Q(status=3))
        self.fields["combine_related_product_list"].widget.choices.queryset = self.fields["combine_related_product_list"].widget.choices.queryset.exclude(Q(id=_instance.id) and Q(status=3))

    def clean_sku(self):
        sku = self.cleaned_data.get('sku')
        return sku.upper()

    def save(self, commit=True):
        product = super(ProductAsinForm, self).save(commit=False)

        if commit:
            product.save()

        if product is None or product.pk is None:
            product = super(ProductAsinForm, self).save(commit=True)

        if product.pk:
            # 修改
            # 增加m2m保存方法,把已选的category值保存到关系表中
            product.category.set(self.cleaned_data['category_list'])
            # 增加m2m保存方法,把已选的keyword值保存到关系表中
            product.keyword.set(self.cleaned_data['keyword_list'])
            # 增加m2m保存方法,把已选的Relation Product值保存到关系表中
            product.combine_relation.set(self.cleaned_data['combine_related_product_list'])
            self.save_m2m()

        return product
