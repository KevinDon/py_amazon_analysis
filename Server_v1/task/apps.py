
from django.utils.translation import ugettext_lazy as _
from appfront.apps import AppsConfig


class TaskConfig(AppsConfig):
    name = 'task'
    verbose_name = _('Task Center')
    verbose_name_plural = _('Task Center')
