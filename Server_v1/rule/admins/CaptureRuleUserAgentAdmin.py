from django.contrib import admin

from rule.forms import CaptureRuleForm, CaptureRuleCookieModel, CaptureRuleCookieForm, \
    CaptureRuleUserAgentModel, CaptureRuleUserAgentForm
from manager.admins import CommonAdmin


@admin.register(CaptureRuleUserAgentModel)
class CaptureRuleUserAgentAdmin(CommonAdmin):
    """ Capture Rule Admin """
    form = CaptureRuleUserAgentForm

    # list_display = ('title', 'cookies', 'expired', 'description')
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'cookies', 'expired', 'description',)
    #     }),
    # )
