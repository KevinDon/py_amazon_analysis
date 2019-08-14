from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import *
from manager.model.CommonModel import CommonModel


class MessageContentModel(CommonModel):
    SEND_STATUS = ((1, _('Successful')), (2, _('Unsuccessful')), (3, _('Error')),)

    title = models.CharField(_('Title'), max_length=100, blank=True)
    send_status = models.IntegerField(verbose_name=_('Send Status'), choices=SEND_STATUS, default=2, editable=False)
    sending_type = models.CharField(_('Sending Type'), max_length=50, blank=True)
    content = models.TextField(max_length=10000, verbose_name=_('Content'), null=True)
    condition = models.CharField(_('Condition'), max_length=255, blank=True)
    group_name = models.CharField(_('Group Name'), max_length=50, blank=True)
    token = models.CharField(_('Token'), max_length=100, blank=True)
    message_type = models.CharField(_('Message Type'), max_length=50, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "system"
        verbose_name = _('Message Content')
        verbose_name_plural = _('Message Content')
        db_table = 'system_message_content'
