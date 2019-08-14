from django.db import models
from django.utils.translation import ugettext as _
from manager.model.CommonModel import CommonModel, PlatformMixin
# from .DataDictionay import DataDictionaryModel as DictModel
from . import DataDictionaryModel

VALUE_TYPE = (1, _('Text')), (2, _('ImageBase64')), (3, _('Url'))


class DataDictionaryValueModel(CommonModel, PlatformMixin):
    """ Data Dictionary Value Table """
    title = models.CharField(null=True, max_length=100, verbose_name=_('Dict Value Title'))
    value = models.CharField(null=True, max_length=255, verbose_name=_('Dict Value'), )
    type = models.IntegerField(null=True, default=1, choices=VALUE_TYPE, verbose_name='Dict Type', )
    is_default = models.BooleanField(default=False, verbose_name=_('Default Value'), )

    dict = models.ForeignKey(DataDictionaryModel, on_delete=models.CASCADE, null=True, verbose_name=_('Dictionary'),
                             related_name='dict_values')

    def __str__(self):
        return _('Dictionary Value: %s') % self.title

    class Meta:
        app_label = "dictionary"
        db_table = 'pub_data_dictionary_value'
        verbose_name = _('Dict Value')
        verbose_name_plural = _('Dict Value')
