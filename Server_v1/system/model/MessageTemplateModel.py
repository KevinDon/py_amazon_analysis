from django.db import models
from django.contrib.auth.models import User
from system.model.DingTalkModel import *
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel
from dictionary.model import *
from task.model import TaskMessageListModel


class MessageTemplateModel(CommonModel):
    CHOICES_TYPE = (('markdown', _('Markdown')),)
    CHOICES_FREQUENCY = (('hour', _('Every Hour')), ('day', _('Every Day')), ('week', _('Every Week')),)
    name = models.CharField(verbose_name=_('Name'), max_length=100, null=True)
    describe = models.CharField(max_length=255, verbose_name=_('Describe'), null=True)
    condition = models.TextField(max_length=10000, verbose_name=_('Condition'), null=True)
    content = models.TextField(max_length=10000, verbose_name=_('Content'), null=True)
    type = models.CharField(choices=CHOICES_TYPE, max_length=50, verbose_name=_('Type'))
    message_type = models.CharField(max_length=50, verbose_name=_('Message Type'), null=True)
    cronjob = models.ForeignKey(TaskMessageListModel, on_delete=models.SET(0), related_name='cronjob+', verbose_name=_('Cronjob'))
    dingtalk = models.ManyToManyField(DingTalkModel, verbose_name=_('Dingtalk'))

    def message_type_display(self):
        if self.message_type is not None:
            dictionary = DataDictionaryModel.objects.get(code_main='message_type')
            value = DataDictionaryValueModel.objects.filter(dict_id=dictionary.id, value=self.message_type).first()
            return '' if value is None else value.title
        else:
            return None
    message_type_display.short_description = _('Message Type')

    def __str__(self):
        return self.name

    class Meta:
        app_label = "system"
        db_table = 'system_message_template'
        verbose_name = _("Message Template")
        verbose_name_plural = _("Message Template")


