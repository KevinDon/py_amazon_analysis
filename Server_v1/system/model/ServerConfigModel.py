from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel, PlatformMixin
from system.model.ServerStatusModel import ServerStatusModel


class ServerConfigModel(CommonModel, PlatformMixin):
    CHOICES_TIMEZONE = (('Australia/Melbourne', _('Australia/Melbourne')), ('Asia/Shanghai', _('Asia/Shanghai')),)

    name = models.CharField(verbose_name=_('Name'), max_length=100, null=True)
    ip = models.CharField(max_length=15, verbose_name=_('IP'), null=True)
    port = models.CharField(max_length=6, verbose_name=_('Port'), null=True)
    server_status = models.OneToOneField(ServerStatusModel, on_delete=models.CASCADE, verbose_name=_('Running Status'))
    timezone = models.CharField(max_length=100, verbose_name=_('Timezone'), null=True, choices=CHOICES_TIMEZONE)
    key = models.CharField(max_length=100, verbose_name=_('Key'), null=True)
    token_expire = models.IntegerField(default=360, verbose_name=_('Token Expire (day)'), null=True)
    api_account = models.CharField(max_length=60, verbose_name=_('Account'), null=True)
    api_password = models.CharField(max_length=60, verbose_name=_('Password'), null=True)
    instance_id = models.CharField(max_length=60, verbose_name=_('Instance Id'), null=True)
    region_id = models.CharField(max_length=60, verbose_name=_('Region Id'), null=True)
    max_process = models.IntegerField(default=1, verbose_name=_('Max Process'))
    process = models.IntegerField(default=1, verbose_name=_('Process'))
    remark = models.TextField(max_length=10000, verbose_name=_('Remark'), null=True)

    def jobs(self):
        return self.server_status.jobs

    def __str__(self):
        return self.name

    class Meta:
        app_label = "system"
        db_table = 'system_server_config'
        verbose_name = _("Scrapy Server Config")
        verbose_name_plural = _("Scrapy Server Config")


