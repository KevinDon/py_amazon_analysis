from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from manager.model.CommonModel import CommonModel
CHOICES_TYPE = ((1, _('String')), (2, _('Number')), (3, _('Date')),
                (4, _('DateTime')), (5, _('Boolean')), (6, _('Enum')),)
CHOICES_SCOPE = ((1, _('System')), (2, _('Multi Model')), (3, _('Single Model')),)


class TemplateVarModel(CommonModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100, null=True)
    code = models.CharField(max_length=50, verbose_name=_('Code'), null=True, unique=True)
    type = models.IntegerField(choices=CHOICES_TYPE, verbose_name=_('Type'), default=1, null=True)
    scope = models.IntegerField(choices=CHOICES_SCOPE, verbose_name=_('Scope'), default=1, null=True)
    message_type = models.CharField(max_length=50, verbose_name=_('Message Type'), null=True, blank=True)
    is_custom = models.BooleanField(_('Is Custom'), default=False)
    value = models.TextField(max_length=10000, verbose_name=_('Value'), null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "system"
        db_table = 'system_template_var'
        verbose_name = _("Template Variant")
        verbose_name_plural = _("Template Variant")


