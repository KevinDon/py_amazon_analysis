# coding:utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cronjob.model import CronjobModel


class CronjobJobStoreModel(models.Model):
    name = models.CharField(max_length=255, unique=True)  # id of job
    next_run_time = models.DateTimeField(db_index=True, blank=True, null=True)
    job_state = models.BinaryField()
    cronjob_id = models.IntegerField(verbose_name=_('Cronjob'), null=True)
    task_type = models.IntegerField(verbose_name=_('Task Type'), choices=CronjobModel.CHOICES_TASKTYPE, null=True)
    updated_at = models.DateTimeField(verbose_name= _('Update At'), null=True, auto_now=True)
    created_at = models.DateTimeField(verbose_name=_('Created At'), null=True, auto_now_add=True)

    def __str__(self):
        status = 'next run at: %s' % self.next_run_time if self.next_run_time else 'paused'
        return '%s (%s)' % (self.name, status)

    class Meta:
        app_label = "cronjob"
        db_table = 'na_cronjob_job_store'
        ordering = ('next_run_time',)
        verbose_name = _('Task List')
        verbose_name_plural = _('Task List')
