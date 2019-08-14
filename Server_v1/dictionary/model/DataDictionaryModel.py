import logging

from django.db import models
from django.utils.translation import ugettext as _
from .DataDictionaryCategoryModel import DataDictionaryCategoryModel as DictCateModel
from manager.model.CommonModel import CommonModel, PlatformMixin

INNER_TYPE = (1, _('Single')), (2, _('Enum'))


class DataDictionaryModel(CommonModel, PlatformMixin):
    class Meta:
        app_label = "dictionary"
        db_table = 'pub_data_dictionary'
        # unique_together = ('-report_date', 'asin_child',)
        verbose_name = _('Dict')
        verbose_name_plural = _('Dict')

    """ Data Dictionary Table """
    title = models.CharField(null=True, max_length=100, verbose_name=_('Title'), )
    code_main = models.CharField(null=True, max_length=64, verbose_name=_('Main Code'), )
    code_sub = models.CharField(null=True, max_length=64, verbose_name=_('Sub Code'), )
    description = models.TextField(null=True, max_length=1000, verbose_name=_('Description'), )
    category = models.ForeignKey(DictCateModel, null=True, on_delete=models.SET(0), default=0,
                                 verbose_name=_('Dict Category'), blank=True,related_name='dicts')
    type = models.IntegerField(null=True, default=1, choices=INNER_TYPE, verbose_name='Dictionary Type',
                               )

    def __str__(self):
        return _('Dictionary: %s') % self.title

    # @staticmethod
    # def get_dicts_structured(dicts, dict_values, ):
    #     """
    #     获取结构化数据字典
    #     :param dicts: 数据字典集合
    #     :param dict_values: 数据字典值集合
    #     :return:
    #     """
    #     if len(dicts) > 0 and len(dict_values) > 0:
    #         dicts = dicts.values()
    #         dict_values = dict_values.values()
    #
    #         dicts_structure = []
    #         for item in dicts:
    #             item_structure = {'dict': item, 'values': []}
    #             for val in dict_values:
    #                 if val['dict_id'] == item['id']:
    #                     item_structure['values'].append(val)
    #             dicts_structure.append(item_structure)
    #         return dicts_structure
    #     else:
    #         return []
