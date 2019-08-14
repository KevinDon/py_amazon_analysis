from django.db import models
from django.utils.translation import ugettext_lazy as _

from rule.model import AnalysisRuleModel
from manager.model import CommonModel
from manager.model.CommonModel import PlatformMixin


class AnalysisRuleItemModel(CommonModel):
    MATCH_TYPE = (('xpath', 'XPath'), ('re', 'Regex'), ('beautiful_soup', 'BeautifulSoup4'))
    MATCH_ATTR = (('text', 'Text'), ('trim', 'Trim Text'), ('dom', 'Dom Text'), ('attr', 'Dom Attr'))

    class Meta:
        app_label = "rule"
        db_table = 'rule_analysis_rule_item'
        verbose_name = _('Analysis Rule')
        verbose_name_plural = _('Analysis Rule')

    """ Fetch Data Rule Item Table """
    title = models.CharField(null=True, max_length=100, verbose_name=_('Title'))
    match = models.CharField(null=True, max_length=64, choices=MATCH_TYPE, default='xpath', verbose_name=_('Match Mode'))
    value = models.TextField(null=True, verbose_name=_('Match'))
    analysis_rule = models.ForeignKey(AnalysisRuleModel, null=True, on_delete=models.CASCADE, verbose_name=_('rule'), editable=False, related_name='fetch_rule')

    description = models.TextField(null=True, max_length=1000, verbose_name=_('Description'))

    def __str__(self):
        return self.title
