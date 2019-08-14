from django.utils.translation import ugettext as _
from django.contrib.auth.models import *

from manager.model.CommonModel import CommonModel, PlatformMixin


class SkuKeywordModel(CommonModel, PlatformMixin):
    CHOICE_KEYWORD_TYPE = ((1, _('Sku Keyword')), (2, _('Category Keyword')))
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    keyword_type = models.IntegerField(null=True, default=1, verbose_name=_('Keyword Type'), choices=CHOICE_KEYWORD_TYPE)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "amazon"
        db_table = 'pub_sku_keyword'
        verbose_name = _("Sku Keyword")
        verbose_name_plural = _("Sku Keyword")
