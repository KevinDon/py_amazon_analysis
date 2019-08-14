# coding:utf-8

from django.db import models
from django.utils.translation import ugettext as _

from cronjob.model import CronjobModel, format_html


class CronjobLogsModel(models.Model):
    CHOICES_STATUS = ((1, _('Successful')), (2, _('Unsuccessful')), (3, _('Error')),)

    cronjob = models.ForeignKey(CronjobModel, on_delete=models.CASCADE, editable=True, null=True)
    status = models.IntegerField(verbose_name= _('Status'), choices=CHOICES_STATUS, default=1, editable=False )
    content = models.TextField(max_length=10000, verbose_name=_('Content'), null=True)
    process = models.CharField(max_length=100, verbose_name=_('Process ID'), null=True)
    thread = models.IntegerField(verbose_name=_('Thread ID'), null=True)
    time_long = models.FloatField(verbose_name=_('Time Long'), default=0)
    date_begin = models.DateTimeField(verbose_name=_('Begin'), null=True)
    date_end = models.DateTimeField(verbose_name=_('End'), null=True)
    task_type = models.IntegerField(verbose_name=_('Task Type'), choices=CronjobModel.CHOICES_TASKTYPE, null=True)
    created_at = models.DateTimeField(verbose_name=_('Created At'), null=True, auto_now_add=True)

    def __str__(self):
        return _('ID: %s') % self.id

    class Meta:
        app_label = "cronjob"
        db_table = 'na_cronjob_logs'
        verbose_name = _('Logs for Run')
        verbose_name_plural = _('Logs for Run')

    def colored_status(self):
        if self.status == 1:
            color_name = 'green'
            _label = self.CHOICES_STATUS[0][1]
        elif self.status == 2:
            color_name = 'orange'
            _label = self.CHOICES_STATUS[1][1]
        else:
            color_name = 'red'
            _label = self.CHOICES_STATUS[2][1]

        return format_html(
            '<span style="color:{};">{}</span>',
            color_name,
            _label,
        )
    colored_status.short_description = _('Status')