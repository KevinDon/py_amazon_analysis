# coding:utf-8

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models import Q
from django.utils.translation import ugettext as _
from amazon.model.AmazonProductCategoryModel import SkuKeywordModel, AmazonProductCategoryModel
from appfront.model.ProductAsinModel import ProductAsinModel


class SkuKeywordForm(forms.ModelForm):
    # sku_list = forms.ModelMultipleChoiceField(
    #     queryset=ProductAsinModel.objects.exclude(Q(status=3)),
    #     required=False,
    #     widget=FilteredSelectMultiple(
    #         verbose_name=_('Relation Product Sku'),
    #         is_stacked=False
    #     )
    # )

    amazon_category_list = forms.ModelMultipleChoiceField(
        queryset=AmazonProductCategoryModel.objects.exclude(Q(status=3)),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Relation Amazon Category'),
            is_stacked=False
        )
    )

    class Meta:
        model = SkuKeywordModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SkuKeywordForm, self).__init__(*args, **kwargs)
        # self.fields["parent"].widget.choices.queryset = self.fields["parent"].widget.choices.queryset.exclude(status=3)
        _instance = kwargs.get('instance')
        if _instance:
            # self.fields["sku_list"].initial = _instance.productasinmodel_set.all()
            self.fields['amazon_category_list'].initial = _instance.amazonproductcategorymodel_set.all()

    def save(self, commit=True):
        keyword = super(SkuKeywordForm, self).save(commit=False)

        if commit:
            keyword.save()

        if keyword is None or keyword.pk is None:
            keyword = super(SkuKeywordForm, self).save(commit=True)

        if keyword.pk:
            # 增加m2m保存方法,把已选的的sku到关系表中
            # keyword.productasinmodel_set.set(self.cleaned_data['sku_list'])
            # 增加amazon category关系
            keyword.amazonproductcategorymodel_set.set(self.cleaned_data['amazon_category_list'])
            self.save_m2m()

        return keyword
