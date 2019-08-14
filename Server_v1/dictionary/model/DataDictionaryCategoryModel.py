from django.db import models
from django.utils.translation import ugettext as _
from manager.model.CommonModel import CommonModel, PlatformMixin


class DataDictionaryCategoryModel(CommonModel, PlatformMixin):
    """ Data Dictionary Category Table """
    DATA_TYPE_LIST = ((1, 'data'), (2, 'config'))
    code = models.CharField(null=True, max_length=100, unique=True, verbose_name=_('Code'))
    title = models.CharField(null=True, max_length=100, verbose_name=_('Title'))

    data_type = models.IntegerField(null=True, default=1, choices=DATA_TYPE_LIST, verbose_name='Dictionary Type',
                               )
    description = models.TextField(null=True, max_length=1000, verbose_name=_('Description'))
    parent = models.ForeignKey('self', null=True, on_delete=models.SET(0), editable=True, blank=True,
                               verbose_name=_('Parent Cate'))

    def __str__(self):
        return _('Dictionary Category: %s') % self.title

    class Meta:
        app_label = "dictionary"
        db_table = 'pub_data_dictionary_category'
        # unique_together = ('-report_date', 'asin_child',)
        verbose_name = _('Dict Category')
        verbose_name_plural = _('Dict Category')
