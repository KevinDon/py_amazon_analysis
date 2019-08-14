# coding:utf-8

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models import Q
from appfront.model import ProductCategoryModel, ProductAsinModel
from django.utils.translation import ugettext as _

from manager.forms import CommonModelForm


class ProductCategoryForm(CommonModelForm):
    require_fields = ('code', 'title')

    sku_list = forms.ModelMultipleChoiceField(
        queryset=ProductAsinModel.objects.exclude(Q(status=3)),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('Relation Product Sku'),
            is_stacked=True
        )
    )

    class Meta:
        model = ProductCategoryModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductCategoryForm, self).__init__(*args, **kwargs)
        _instance = kwargs.get('instance')
        if _instance:
            self.fields["parent"].widget.choices.queryset = self.fields["parent"].widget.choices.queryset.exclude(Q(status=3) | Q(id=_instance.pk))
            self.fields["amazon_category"].widget.choices.queryset = self.fields["amazon_category"].widget.choices.queryset.exclude(status=3)
            # 使用关联查询当前category关联的sku集合
            self.fields["sku_list"].initial = _instance.productasinmodel_set.all()

    def save(self, commit=True):
        category = super(ProductCategoryForm, self).save(commit=False)
        # model内字段修改

        if commit:
            category.save()

        # model关联字段修改
        if category is None or category.pk is None:
            category = super(ProductCategoryForm, self).save(commit=True)

        if category.pk:
            # 增加m2m保存方法,把已选的的sku到关系表中
            category.productasinmodel_set.set(self.cleaned_data['sku_list'])
            self.save_m2m()

        return category
