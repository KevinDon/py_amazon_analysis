from django.db import models
from django.utils.translation import ugettext_lazy as _

from rule.model import CaptureRuleModel
from manager.model import CommonModel


class CaptureRuleUrlModel(CommonModel):
    URL_PROTOCOL = (('http', 'http'), ('https', 'https'))

    class Meta:
        app_label = "rule"
        db_table = 'rule_capture_rule_url'
        verbose_name = _('Capture Rule Url')
        verbose_name_plural = _('Capture Rule Url')

    protocol = models.CharField(null=True, max_length=64, choices=URL_PROTOCOL, default='https',
                                verbose_name=_('Url Protocol'))
    host = models.CharField(null=True, max_length=200, verbose_name=_('Host'))
    path = models.TextField(null=True, verbose_name=_('Url Path'), default='')
    params = models.TextField(null=True, verbose_name=_('Url Params'), default='')
    capture_rule = models.ForeignKey(CaptureRuleModel, null=True, on_delete=models.CASCADE, verbose_name=_('rule'),
                                     editable=False, related_name='capture_rule_urls')

    condition = models.TextField(null=True, default='', verbose_name=_('Url Params Condition'),
                                 help_text='This is a JSON Format field')

    def __str__(self):
        return self.host
