from django.db import models
from django.utils.translation import ugettext_lazy as _
from manager.model import CommonModel


class CaptureRuleCookieModel(CommonModel):

    class Meta:
        app_label = "rule"
        db_table = 'rule_capture_rule_cookie'
        verbose_name = _('Capture Rule Cookie')
        verbose_name_plural = _('Capture Rule Cookie')

    """ Capture Rule Cookie Table """
    title = models.CharField(null=True, max_length=100, verbose_name=_('Title'))
    description = models.TextField(null=True, max_length=1000, verbose_name=_('Description'))
    cookies = models.TextField(null=True, max_length=1000, verbose_name=_('Cookies'))
    expired = models.DateTimeField(null=True, verbose_name=_('Expire Time'))

    def __str__(self):
        return self.title
