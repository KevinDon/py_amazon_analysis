from system.model import *
from django.contrib.auth.admin import *
from system.forms import *
from cronjob.model import CronjobModel
from manager.admin import CommonAdmin


@admin.register(MessageTemplateModel)
class MessageTemplateAdmin(CommonAdmin):
    list_display = ('name', 'message_type_display', 'status')
    form = MessageTemplateForm
    search_fields = ('name',  'message_type')
    list_editable = ('status',)
    list_filter = ('status',)
    fieldsets = (
        (None, {
            'fields': ('name', 'describe', 'condition', 'type', 'message_type', 'cronjob', 'dingtalk')
        }),
        ('Content', {
            'fields': ( 'content',)
        }))

    # def save_model(self, request, obj, form, change):
    #     if obj.frequency == 'day':
    #         cronjob = CronjobModel(type=2, code=obj.message_type, title=obj.name, dy='*/1', hr=obj.hr, mi=obj.mi, se=obj.se,
    #                                command='task.cronjobs.{}.handle()'.format(obj.message_type), command_type=1)
    #     elif obj.frequency == 'week':
    #         cronjob = CronjobModel(type=2, code=obj.message_type, title=obj.name, wk='*/1', dy_of_week=obj.dy_of_week, hr=obj.hr, mi=obj.mi, se=obj.se,
    #                                command='task.cronjobs.{}.handle()'.format(obj.message_type), command_type=1)
    #     else:
    #         cronjob = CronjobModel(type=2, code=obj.message_type, title=obj.name, hr='*/1', mi=obj.mi, se=obj.se,
    #                                command='task.cronjobs.{}.handle()'.format(obj.message_type), command_type=1)
    #     if obj.cronjob is not None:
    #         cronjob.id = obj.cronjob.id
    #     cronjob.creator = request.user
    #     cronjob.save()
    #     obj.cronjob = cronjob
    #     obj.creator = request.user
    #     super().save_model(request, obj, form, change)


