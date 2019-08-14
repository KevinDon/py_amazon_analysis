import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from rule.model.CaptureRuleCookieModel import CaptureRuleCookieModel
from rule.model.CaptureRuleUserAgentModel import CaptureRuleUserAgentModel
from manager.model.CommonModel import CommonModel, PlatformMixin
from system.model import RegionModel, ProxyIpModel
from system.model.ServerConfigModel import ServerConfigModel


class CaptureRuleModel(CommonModel, PlatformMixin):
    ACC_LANG = (('en', 'en',), ('en-au', 'en-au'), ('zh-cn', 'zh-cn'))
    PROXY_USED = ((1, _('Multi Proxy')), (2, _('Single Proxy')), (3, _('Not use Proxy')))

    class Meta:
        app_label = "rule"
        db_table = 'rule_capture_rule'
        verbose_name = _('Capture Rule')
        verbose_name_plural = _('Capture Rule')

    """ Capture Rule Table """
    # 标题
    title = models.CharField(null=True, max_length=100, verbose_name=_('Title'))
    # 规则编码 - 系统内部生成
    rule_code = models.UUIDField(verbose_name=_('Capture Rule Code'), null=True, help_text='Automatically generated internally by the system')
    # 爬虫名字
    spider_name = models.CharField(null=True, max_length=200, verbose_name=_('Spider Name'), default='CaptureSpider')
    # 请求间隔
    delay = models.IntegerField(null=True, verbose_name=_('Request Delay'), default=2, help_text=_('Request Delay must bigger 1 Second!!'))
    # 最大请求线程
    max_thread = models.IntegerField(null=True, verbose_name=_('Max Thread'), default=6)
    # 请求分片大小
    slice = models.IntegerField(null=True, default=300, verbose_name=_('Request Slice'))

    description = models.TextField(null=True, max_length=1000, verbose_name=_('Description'))
    accept_language = models.CharField(null=True, max_length=64, choices=ACC_LANG, default='en', verbose_name=_('Language'))
    accept = models.TextField(null=True, max_length=1000, verbose_name=_('Accept'))

    cookies = models.ForeignKey(CaptureRuleCookieModel, null=True, on_delete=models.SET(''), verbose_name=_('Cookies'), related_name='capture_cookie', blank=True)
    user_agent = models.ForeignKey(CaptureRuleUserAgentModel, null=True, on_delete=models.SET(''), verbose_name=_('User Agent'), related_name='capture_user_agent', blank=True)
    scrapy_server = models.ForeignKey(ServerConfigModel, on_delete=models.SET(''), verbose_name=_('Scrapy Server'), null=True, related_name='scrapyserver+')

    proxy_used = models.IntegerField(null=True, default=3, choices=PROXY_USED, verbose_name=_('Use the proxy'))
    proxys_city = models.ManyToManyField(RegionModel, verbose_name=_('Proxys City'), )
    proxys_num = models.IntegerField(null=True, verbose_name=_('Proxys Num'), default=0)
    proxy = models.OneToOneField(ProxyIpModel, null=True, verbose_name=_('Proxy'), related_name='proxy', on_delete=models.SET(''), blank=True)
    xml_data = models.TextField(null=True, max_length=10000, verbose_name=_('Xml Data'))

    def __str__(self):
        return '%s:%s' % (_('Capture Rule'), self.title)
