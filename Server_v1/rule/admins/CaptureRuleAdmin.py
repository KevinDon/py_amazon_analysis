import logging
import uuid

from django.contrib import admin

from rule.forms import CaptureRuleForm, CaptureRuleModel
from rule.forms.CaptureRuleUrlForm import CaptureRuleUrlForm
from rule.model import CaptureRuleUrlModel
from manager.admins import CommonAdmin


class CaptureRuleUrlAdminInline(admin.StackedInline):
    """ Capture Rule Url Admin"""
    extra = 0
    model = CaptureRuleUrlModel
    form = CaptureRuleUrlForm


@admin.register(CaptureRuleModel)
class CaptureRuleAdmin(CommonAdmin):
    """ Capture Rule Admin """
    form = CaptureRuleForm

    inlines = (CaptureRuleUrlAdminInline,)
    list_display = ('title', 'rule_code', 'scrapy_server')
    search_fields = ('title',)
    list_filter = ('scrapy_server', 'platform')
    readonly_fields = ('rule_code',)
    fieldsets = (
        (None, {
            'fields': ('status', 'title', 'spider_name', 'rule_code', 'description', 'xml_data', 'platform', 'scrapy_server')
        }),
        ('Task Config', {
            'fields': ('delay', 'max_thread', 'slice',)
        }),
        ('Request Config', {
            'fields': ('cookies', 'user_agent', 'accept', 'accept_language',)
        }),
        ('Proxy Config', {
            'fields': ('proxy_used', 'proxys_num', 'proxy',)
        }))

    def save_model(self, request, obj, form, change):
        try:
            if change:

                pass
            else:
                obj.rule_code = str(uuid.uuid4())


        except Exception as e:
            logging.error('e')
        finally:
            super(CaptureRuleAdmin, self).save_model(request, obj, form, change)
        pass
