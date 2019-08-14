# coding:utf-8

from django.contrib import admin, messages
from django.shortcuts import get_object_or_404, redirect
from django.utils.html import format_html
from cronjob.forms.CronjobForm import *
from django.utils.translation import ugettext as _
from cronjob.libs.cronjob_util import MySchedulers


# @admin.register(CronjobModel)
from cronjob.model import CronjobJobStoreModel


class CronjobAdmin(admin.ModelAdmin):
    list_display = ('title', 'colored_type',  'colored_status', 'command_type', 'code', 'command', 'start_date', 'end_date', 'updated_at', 'creator', 'running', 'data_operations')
    search_fields = ('code', 'title', 'command', 'start_date', 'end_date', 'updated_at')
    list_filter = ('type', 'code', 'status')

    readonly_fields = ('updated_at', 'created_at', 'creator')
    ordering = ['-created_at']

    # form set
    fieldsets = (
        (None, {
            'fields': ('status', 'title', 'code', 'task_type', 'command_type', 'rule_id', 'command')
        }),
        ('Timer Options', {
            'classes': ('collapse',),
            'fields': ('type', 'timezone',  ('yr','hr'), ('mo', 'mi'), ('dy', 'se'), ('wk', 'dy_of_week'), 'start_date', 'end_date')
        }),
        ('System Info', {
            'classes': ('collapse',),
            'fields': ('updated_at', 'created_at', 'creator')
        }),
    )

    show_change_link = True
    form = CronjobForm
    # Action选项都是在页面上方显示
    actions_on_top = False
    # Action选项都是在页面下方显示
    actions_on_bottom = True
    # 是否显示选择个数
    actions_selection_counter = True

    class Media:
        js = ('cronjob/admin.js',)

    '''运行状态'''
    def running(self, obj):
        cjs = CronjobJobStoreModel.objects.filter(cronjob_id=obj.id).first()

        result = _('Yes') if cjs is not None else _('No')
        color_name = _('green') if cjs is not None else _('gray')

        return format_html('<span style="color:{};">{}</span>', color_name, result)

    '''保存记录'''
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.save()
        super().save_model(request, obj, form, change)


    def data_operations(self, obj):
        _html = ''
        dest = '{0}start/'.format(obj.pk)
        title = _('Start')
        _html += '<a class="button" href="{0}">{1}</a>'.format(dest, title)

        dest = '{0}stop/'.format(obj.pk)
        title = _('Stop')
        _html += ' <a class="button" href="{0}">{1}</a>'.format(dest, title)

        dest = '/admin/cronjob/cronjoblogsmodel/?cronjob__id__exact={0}'.format(obj.pk)
        title = _('Logs')
        _html += ' <a class="button" href="{0}" target="_blank">{1}</a>'.format(dest, title)

        return format_html(_html)

    data_operations.short_description = 'Operations'
    data_operations.allow_tags = True

    # actions = ['copy_one']
    def get_urls(self):
        """添加一个url，指向实现复制功能的函数copy_one"""
        from django.conf.urls import url
        urls = [
            url('^(?P<pk>\d+)start/?$', self.admin_site.admin_view(self.act_job_start), name='act_job_start'),
            url('^(?P<pk>\d+)stop/?$', self.admin_site.admin_view(self.act_job_stop), name='act_job_start'),
        ]
        return urls + super(CronjobAdmin, self).get_urls()

    '''加载定时设置'''
    def act_job_start(self, request, *args, **kwargs):
        obj = get_object_or_404(CronjobModel, pk=kwargs['pk'])

        msg ={'SUCCESS': [], 'ERROR':[] }
        try:
            if(obj.status == 1):
                _mysch = MySchedulers(self)
                if(_mysch.addJob(obj)):
                    self.message_user(request, 'Start Successful: %s' % obj.title, messages.SUCCESS)
                else:
                    self.message_user(request, 'Start Failed: %s' % obj.title, messages.ERROR)
            else:
                self.message_user(request, 'Start Failed: %s Status is Disabled' % obj.title , messages.ERROR)

        except Exception as e:
            msg['ERROR'].append('%s' % (e))
            self.message_user(request, 'Start Failed: %s' % ('/'.join(msg['ERROR'])), messages.ERROR)

        co_path = request.path.split('/')
        co_path[-2] = ''
        return redirect('/'.join(co_path).replace('//', '/'))

    '''停止定时设置'''
    def act_job_stop(self, request, *args, **kwargs):
        obj = get_object_or_404(CronjobModel, pk=kwargs['pk'])

        msg = {'SUCCESS': [], 'ERROR': []}
        try:

            _mysch = MySchedulers()
            if(_mysch.stopJob(obj)):
                self.message_user(request, 'Stop Successful: %s' % obj.title, messages.SUCCESS)
            else:
                self.message_user(request, 'Stop Failed: %s' % obj.title, messages.ERROR)

        except Exception as e:
            msg['ERROR'].append('%s' % (e))
            self.message_user(request, 'Stop Failed: %s' % ('/'.join(msg['ERROR'])), messages.ERROR)

        co_path = request.path.split('/')
        co_path[-2] = ''
        return redirect('/'.join(co_path).replace('//', '/'))