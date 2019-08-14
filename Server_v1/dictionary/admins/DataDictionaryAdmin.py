# coding:utf-8
import logging

from django.contrib import admin
from django.utils.translation import ugettext as _
from django.views.generic.base import logger

from dictionary.forms import DataDictionaryForm
from dictionary.model import DataDictionaryValueModel, DataDictionaryModel
from manager.admin import CommonAdmin


class DataDictionaryValueInline(admin.TabularInline):
    """ data dictionary value inline """
    extra = 1
    model = DataDictionaryValueModel


@admin.register(DataDictionaryModel)
class DataDictionaryAdmin(CommonAdmin):
    """ data dictionary admin """
    inlines = (DataDictionaryValueInline,)
    list_display = ('title', 'code_main', 'code_sub', 'category', 'type', 'platform',)
    search_fields = ('title', 'updated_at', 'created_at')
    list_filter = ('code_main', 'platform', 'category', 'type')
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'code_main', 'code_sub', 'describe', 'category', 'type', 'dict_value', 'platform',)
    #     }),)

    form = DataDictionaryForm

    class Media:
        js = ('dictionary/add-dictionary-form.js','common/Dictionary.js')

    def save_model(self, request, obj, form, change):
        try:
            if form.is_valid():
                super().save_model(request, obj, form, change)
                # 保存Dictionary Value
                if request.POST['type'] is '1':
                    dictionary = form.save(commit=False)
                    if change:
                        # 修改
                        dict_val_res = DataDictionaryValueModel.objects.filter(
                            dict_id=dictionary.id).order_by('sort', 'id')
                        
                        if len(dict_val_res) < 1:
                            # 创建 dict_val
                            dict_val_res = DataDictionaryValueModel()
                            dict_val_res.dict_id = dictionary.id
                            dict_val_res.title = r'_'.join((dictionary.code_main.upper(), dictionary.code_sub.upper()))
                        else:
                            dict_val_res = dict_val_res[0]
                        dict_val_res.value = request.POST['dict_value']
                    else:
                        # 新增
                        dict_val_res = DataDictionaryValueModel()
                        dict_val_res.dict_id = dictionary.id
                        dict_val_res.title = r'_'.join((dictionary.code_main.upper(), dictionary.code_sub.upper()))
                        dict_val_res.value = request.POST['dict_value']

                    dict_val_res.save()
        except Exception as e:
            import traceback;
            traceback.print_exc();
            logging.error(e)
