import logging
import uuid

from django.contrib import admin

from rule.admins import CaptureRuleAdmin
from rule.forms import AnalysisRuleForm
from rule.model import AnalysisRuleModel, AnalysisRuleItemModel
from manager.admins import CommonAdmin


class AnalysisRuleItemAdminInline(admin.StackedInline):
    """ Fetch Rule Item Admin"""
    extra = 1
    model = AnalysisRuleItemModel


@admin.register(AnalysisRuleModel)
class AnalysisRuleAdmin(CommonAdmin):
    """ Fetch Rule Admin """
    form = AnalysisRuleForm

    inlines = (AnalysisRuleItemAdminInline,)
    list_display = ('id', 'title', 'rule_code', 'capture_rule',)
    search_fields = ('title',)
    readonly_fields = ('rule_code',)
    fieldsets = (
        (None, {
            'fields': ('title', 'rule_code', 'description',  'capture_rule', 'xml_data', 'analysis_last_id', 'sync_last_id', 'platform',)
        }),)

    def save_model(self, request, obj, form, change):
        try:
            if change:

                pass
            else:
                obj.rule_code = str(uuid.uuid4())
        except Exception as e:
            logging.error('e')
        finally:
            super(AnalysisRuleAdmin, self).save_model(request, obj, form, change)
        pass
