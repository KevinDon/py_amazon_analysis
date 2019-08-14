# coding:utf-8

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models import Q
from django.utils.translation import ugettext as _
from django.core.handlers.base import logger

from amazon.model.SkuKeywordModel import SkuKeywordModel
from amazon.model.AmazonProductCategoryModel import AmazonProductCategoryModel
from appfront.model.ProductCategoryModel import ProductCategoryModel as NA_ProductCategoryModel


class AmazonProductCategoryForm(forms.ModelForm):
    class Meta:
        model = AmazonProductCategoryModel
        fields = '__all__'

    # 自定义 product category field
    na_product_category_list = forms.ModelMultipleChoiceField(
        queryset=NA_ProductCategoryModel.objects.exclude(Q(status=3)),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('NewAim Product Category'),
            is_stacked=False
        )
    )

    # 自定义 keyword field
    amazon_keyword_list = forms.ModelMultipleChoiceField(
        queryset=SkuKeywordModel.objects.exclude(Q(status=3)),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Amazon Keyword'),
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(AmazonProductCategoryForm, self).__init__(*args, **kwargs)
        _instance = kwargs.get('instance')
        if _instance:
            self.fields["parent"].widget.choices.queryset = self.fields["parent"].widget.choices.queryset.exclude(status=3)
            self.fields["na_product_category_list"].initial = _instance.amazon_category.exclude(Q(status=3))
            self.fields['amazon_keyword_list'].initial = _instance.keyword.all()

    def save(self, commit=True):
        try:
            amazon_product_category = super(AmazonProductCategoryForm, self).save(commit=False)

            if commit:
                amazon_product_category.save()

            if amazon_product_category is None or amazon_product_category.pk is None:
                try:
                    _max_id = AmazonProductCategoryModel.objects.latest('id').id
                except AmazonProductCategoryModel.DoesNotExist as e:
                    _max_id = 1
                amazon_product_category.id = _max_id
                amazon_product_category.save()

            if amazon_product_category.pk:
                # amazon_product_category.amazonproductcategorymodel_set.set(self.cleaned_data['na_product_category_list'])
                amazon_product_category.amazon_category.set(self.cleaned_data['na_product_category_list'])
                amazon_product_category.keyword.set(self.cleaned_data['amazon_keyword_list'])
                self.save_m2m()
        except Exception as e:
            import traceback;
            traceback.print_exc();

        return amazon_product_category
