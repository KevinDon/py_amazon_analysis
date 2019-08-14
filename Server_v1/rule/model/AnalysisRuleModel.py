from django.db import models
from django.utils.translation import ugettext_lazy as _
from manager.model import CommonModel
from manager.model.CommonModel import PlatformMixin
from rule.model import CaptureRuleModel
from task.model.TaskAnalysisModel import TaskAnalysisListModel


class AnalysisRuleModel(CommonModel, PlatformMixin):
    class Meta:
        app_label = "rule"
        db_table = 'rule_analysis_rule'
        verbose_name = _('Analysis Rule')
        verbose_name_plural = _('Analysis Rule')

    """ Fetch Rule Table """
    title = models.CharField(null=True, max_length=100, verbose_name=_('Title'))
    rule_code = models.UUIDField(verbose_name=_('Analysis Rule Code'), null=True,
                                 help_text='Automatically generated internally by the system')
    description = models.TextField(null=True, max_length=10000, verbose_name=_('Description'))
    capture_rule = models.ForeignKey(CaptureRuleModel, on_delete=models.CASCADE, verbose_name=_('Capture Rule'), null=True)
    xml_data = models.TextField(null=True, max_length=10000, verbose_name=_('Xml Data'))
    analysis_at = models.DateTimeField(verbose_name=_('Analysis At'), null=True)
    sync_at = models.DateTimeField(verbose_name=_('Sync At'), null=True)
    analysis_last_id = models.BigIntegerField(default=0, verbose_name=_('Analysis Last Id'), null=True)
    sync_last_id = models.BigIntegerField(default=0, verbose_name=_('Sync Last Id'), null=True)

    def __str__(self):
        return self.title
