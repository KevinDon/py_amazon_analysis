from django.contrib import admin

from rule.forms import CaptureRuleForm, CaptureRuleCookieModel, CaptureRuleCookieForm
from manager.admins import CommonAdmin


@admin.register(CaptureRuleCookieModel)
class CaptureRuleCookieAdmin(CommonAdmin):
    """ Capture Rule Admin """
    form = CaptureRuleCookieForm

    list_display = ('title', 'cookies', 'expired', 'description')
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'cookies', 'expired', 'description',)
    #     }),
    # )
