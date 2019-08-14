from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel


class ApiUserLogModel(CommonModel):
    title = models.CharField(verbose_name=_('title'), max_length=100, null=True, blank=True)
    content = models.TextField(max_length=10000, verbose_name=_('Content'), null=True)
    action = models.CharField(max_length=100, verbose_name=_('Action'), null=True)
    ip = models.GenericIPAddressField(verbose_name=_('IP'), null=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "system"
        db_table = 'system_api_user_log'
        verbose_name = _("User Log")
        verbose_name_plural = _("User Log")


