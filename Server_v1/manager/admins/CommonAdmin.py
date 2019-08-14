# coding:utf-8
import logging

from manager.model import *
from django.contrib.auth.admin import *
from django.utils.translation import ugettext_lazy as _


class PlatformAdminMixin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        """
        根据Platform的选择值,同步更新记录的Platform和Platform_id
        todo 需要增加先判断model中是否含有Platform字段
        :param request:
        :param obj:
        :param form:
        :param change:
        """
        try:
            if obj.hasattr('platform'):
                from dictionary.model import DataDictionaryModel
                from dictionary.model import DataDictionaryValueModel
                platform_choice_dict = DataDictionaryModel.objects.filter(code_main='platform', code_sub='choice').first()
                platform_choice = DataDictionaryValueModel.objects.filter(dict_id=platform_choice_dict.id).all()
                platforms = [i for i in platform_choice.values('id', 'value', 'title') if i['value'] == obj.platform]
                obj.platform_id = platforms[0]['id'] if len(platforms) > 0 else 0
                print(obj)
        except Exception as e:
            logging.error(e)
        finally:
            super().save_model(request, obj, form, change)


class CommonAdmin(PlatformAdminMixin):
    show_change_link = True
    # Action选项都是在页面上方显示
    actions_on_top = False
    # Action选项都是在页面下方显示
    actions_on_bottom = True
    # 是否显示选择个数
    actions_selection_counter = True

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        if self.list_display:
            self.list_display += ('updated_at', 'created_at', 'creator',)
        if self.fieldsets:
            self.fieldsets += (('System Info', {
                'classes': ('collapse',),
                'fields': ('updated_at', 'created_at', 'creator',)
            }),)
        if self.readonly_fields:
            self.readonly_fields += ('updated_at', 'created_at', 'creator',)
        else:
            self.readonly_fields = ('updated_at', 'created_at', 'creator',)
        if self.ordering is None:
            self.ordering = ['-sort', '-created_at']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(status=3)

    def save_model(self, request, obj, form, change):
        if obj.creator_id is None:
            obj.creator_id = request.user.id
        super().save_model(request, obj, form, change)
        # obj.platform_id = PLATFORM_LIST

    def delete_model(self, request, obj):
        obj.status = 3
        obj.save()

    def delete_queryset(self, request, queryset):
        queryset.update(status=3)
