from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel
CHOICES_TYPE = ((1, _('Group')), (2, _('Person')))


class DingTalkModel(CommonModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100, null=True)
    describe = models.TextField(max_length=255, verbose_name=_('Describe'), null=True)
    token = models.CharField(max_length=100, verbose_name=_('Token'), null=True)
    type = models.IntegerField(choices=CHOICES_TYPE, verbose_name=_('Type'), default=1, null=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "system"
        db_table = 'system_ding_talk'
        verbose_name = _("Ding Talk")
        verbose_name_plural = _("Ding Talk")


