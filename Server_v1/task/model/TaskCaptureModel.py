# coding:utf-8

from django.utils.translation import ugettext_lazy as _
from cronjob.model import CronjobModel
from django.db import models

class BaseManager(models.Manager):
    def get_queryset(self):
        return self._queryset_class(model=self.model, using=self._db, hints=self._hints).filter(task_type=1)

class TaskCaptureListModel(CronjobModel):
    objects = BaseManager()

    def __str__(self):
        return self.title

    class Meta:
        proxy = True
        managed = False
        app_label = "task"
        verbose_name = _('Capture List')
        verbose_name_plural = _('Capture List')
