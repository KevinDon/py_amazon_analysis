# coding:utf-8
from manager.model import *
from django.contrib.auth.admin import *
from django.utils.translation import ugettext_lazy as _
from manager.forms.UserProfileForm import *


class UserInline(admin.StackedInline):
    model = UserProfileModel
    verbose_name = 'profile'
    fields = ('department', 'nick', 'ding_talk_account',)
    form = UserInlineForm


class UserProfileAdmin(UserAdmin):
    inlines = (UserInline,)
    list_display = ('username', 'email', 'department', 'nick', 'ding_talk_account', 'last_login', 'date_joined', 'is_staff')
    form = UserProfileForm

    def department(self, obj):
        return '' if obj.user_profile.department is None else obj.user_profile.department.name
    department.short_description = _('department')

    def nick(self, obj):
        return '-' if obj.user_profile is None else obj.user_profile.nick
    nick.short_description = _('nick')

    def ding_talk_account(self, obj):
        return obj.user_profile.ding_talk_account
    ding_talk_account.short_description = _('ding talk account')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not hasattr(obj, 'user_profile'):
            profile = UserProfileModel(user=obj, nick=request.POST['user_profile-0-nick'],
                                       ding_talk_account=request.POST['user_profile-0-ding_talk_account'])
            profile.save()


admin.site.unregister(User)
admin.site.register(UserModel, UserProfileAdmin)
