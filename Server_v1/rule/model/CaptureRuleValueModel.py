from django.db import models
from django.utils.translation import ugettext_lazy as _
from manager.model import CommonModel
from manager.model.CommonModel import PlatformMixin

#
# class CaptureRuleValueModel(CommonModel, PlatformMixin):
#     class Meta:
#         app_label = "rule"
#         db_table = 'capture_rule'
#         verbose_name = _('Capture Rule')
#         verbose_name_plural = _('Capture Rule')
#
#     """ Capture Rule Value Table """
#
#     title = model.CharField(null=True, max_length=100, verbose_name=_('Title'))
#     description = model.CharField(null=True, max_length=1000, verbose_name=_('Description'))
#     type = model.IntegerField(null=True,default=1,verbose_name=_('Rule Type'))

