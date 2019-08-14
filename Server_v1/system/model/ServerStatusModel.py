from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel


class ServerStatusModel(CommonModel):
    RUNNING_STATUS = (0, _('Stopped')), (1, _('Running')), (2, _('Error'))
    running_status = models.IntegerField(choices=RUNNING_STATUS, default=0, verbose_name=_('Running Status'), editable=False)
    jobs = models.IntegerField(default=0, verbose_name=_('Jobs'))

    def __str__(self):
        return self.RUNNING_STATUS[self.running_status][1].__str__()

    class Meta:
        app_label = "system"
        db_table = 'system_server_status'
        verbose_name = _("Server Status")
        verbose_name_plural = _("Server Status")


