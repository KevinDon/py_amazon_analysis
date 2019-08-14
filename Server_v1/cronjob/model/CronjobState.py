# coding:utf-8
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext as _

from cronjob.model import CronjobModel


class CronjobStateModel(models.Model):
    CHOICES_STATUS = ((1, _('Successfuly')), (2, _('Failed')),)
    CHOICES_ACTION = ((1, _('Start')), (2, _('Stop')),)

    cronjob = models.ForeignKey(CronjobModel, on_delete=models.CASCADE, editable=True, null=True)
    status = models.IntegerField(verbose_name= _('Status'), choices=CHOICES_STATUS, default=2, editable=False )
    action = models.IntegerField(verbose_name= _('Action'), choices=CHOICES_ACTION, default=2, editable=False )
    task_type = models.IntegerField(verbose_name=_('Task Type'), choices=CronjobModel.CHOICES_TASKTYPE, null=True)
    created_at = models.DateTimeField(verbose_name=_('Created At'), null=True, auto_now_add=True)

    def __str__(self):
        return _('ID: %s' % self.id)

    class Meta:
        app_label = "cronjob"
        db_table = 'na_cronjob_state'
        verbose_name = _('Logs for Load')
        verbose_name_plural = _('Logs for Load')


    def colored_status(self):
        if self.status == 1:
            color_name = 'green'
            _label = self.CHOICES_STATUS[0][1]
        else:
            color_name = 'red'
            _label = self.CHOICES_STATUS[1][1]
        return format_html(
            '<span style="color:{};">{}</span>',
            color_name,
            _label,
        )
    colored_status.short_description = _('Status')

    def colored_action(self):
        if self.action == 1:
            color_name = 'green'
            _label = self.CHOICES_ACTION[0][1]
        else:
            color_name = 'red'
            _label = self.CHOICES_ACTION[1][1]
        return format_html(
            '<span style="color:{};">{}</span>',
            color_name,
            _label,
        )
    colored_action.short_description = _('Action')
