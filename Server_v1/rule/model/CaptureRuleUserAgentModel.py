from django.db import models
from django.utils.translation import ugettext_lazy as _
from manager.model import CommonModel


class CaptureRuleUserAgentModel(CommonModel):
    class Meta:
        app_label = "rule"
        db_table = 'rule_capture_rule_user_agent'
        verbose_name = _('Capture Rule User Agent')
        verbose_name_plural = _('Capture Rule User Agent')

    """ Capture Rule Cookie Table """
    title = models.CharField(null=True, max_length=100, verbose_name=_('Title'))
    description = models.TextField(null=True, max_length=1000, verbose_name=_('Description'))
    user_agent = models.TextField(null=True, max_length=1000, verbose_name=_('UserAgent'))


    def __str__(self):
        return self.title
