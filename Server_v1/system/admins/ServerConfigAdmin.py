from django.shortcuts import redirect, get_object_or_404

from system.model import *
from django.contrib.auth.admin import *
from manager.admin import CommonAdmin
from system.forms import *
from django.utils.html import format_html
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.DescribeInstanceStatusRequest import DescribeInstanceStatusRequest
from aliyunsdkecs.request.v20140526.StartInstanceRequest import StartInstanceRequest
from aliyunsdkecs.request.v20140526.StopInstanceRequest import StopInstanceRequest
import json


@admin.register(ServerConfigModel)
class ServerConfigAdmin(CommonAdmin):
    list_display = ('name', 'ip', 'port', 'running_status', 'jobs')
    search_fields = ('name', 'ip', 'remark')
    # list_filter = ('running_status',)
    fieldsets = (
        (None, {
            'fields': ('name', 'key', 'ip', 'port', 'api_account', 'api_password', 'instance_id', 'region_id',
                       'max_process', 'process', 'timezone', 'remark')
        }),)
    form = ServerConfigForm

    def running_status(self, obj):
        if self.status_list.get(obj.instance_id, '') == 'Running' and obj.server_status.running_status != 1:
            obj.server_status.running_status = 1
            obj.server_status.save()
        if self.status_list.get(obj.instance_id, '') == 'Stopped' and obj.server_status.running_status != 0:
            obj.server_status.running_status = 0
            obj.server_status.save()
        return obj.server_status

    def get_queryset(self, request):
        api_account = 'LTAIXwk2fSw6fDxW'
        api_password = 'HTIiAIbxJVdbtt7PJHSxVyQg5r9kEx'
        region_id = 'ap-southeast-2'
        # 创建 AcsClient 实例
        self.acsclient = AcsClient(api_account, api_password, region_id)
        _request = DescribeInstanceStatusRequest()
        _request.set_accept_format('json')
        _request.set_PageSize(50)
        self.status_list = {}
        try:
            data = self.acsclient.do_action_with_exception(_request)
            _response = json.loads(data.decode('utf-8'))
            for s in _response['InstanceStatuses']['InstanceStatus']:
                self.status_list[s['InstanceId']] = s['Status']
        except Exception as e:
            pass

        return super().get_queryset(request)

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.list_display += ('data_operations',)

    def data_operations(self, obj):
        _html = ''
        dest = '{0}start/'.format(obj.pk)
        title = 'Start'
        _html += '<a class="button" href="{0}">{1}</a>'.format(dest, title)

        dest = '{0}stop/'.format(obj.pk)
        title = 'Stop'
        _html += ' <a class="button" href="{0}">{1}</a>'.format(dest, title)

        return format_html(_html)

    data_operations.short_description = 'Operations'
    data_operations.allow_tags = True

    def get_urls(self):
        """添加一个url，指向实现复制功能的函数copy_one"""
        from django.conf.urls import url
        urls = [
            url('^(?P<pk>\d+)start/?$', self.admin_site.admin_view(self.act_start), name='act_start'),
            url('^(?P<pk>\d+)stop/?$', self.admin_site.admin_view(self.act_stop), name='act_start'),
        ]
        return urls + super(ServerConfigAdmin, self).get_urls()

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'server_status'):
            status = ServerStatusModel(running_status=0, jobs=0)
            status.save()
            obj.server_status = status
        super().save_model(request, obj, form, change)

    def act_start(self, request, *args, **kwargs):
        obj = get_object_or_404(ServerConfigModel, pk=kwargs['pk'])
        _request = StartInstanceRequest()
        _request.set_accept_format('json')
        _request.set_InstanceId(obj.instance_id)
        try:
            self.acsclient.do_action_with_exception(_request)
            obj.server_status.running_status = 1
            obj.server_status.save()
            self.message_user(request, 'Start Successful', messages.SUCCESS)
        except Exception as e:
            obj.server_status.running_status = 2
            obj.server_status.save()
            self.message_user(request, 'Start Failed: %s' % e.message, messages.ERROR)
        co_path = request.path.split('/')
        co_path[-2] = ''
        return redirect('/'.join(co_path).replace('//', '/'))

    def act_stop(self, request, *args, **kwargs):
        obj = get_object_or_404(ServerConfigModel, pk=kwargs['pk'])
        # 创建 AcsClient 实例
        _request = StopInstanceRequest()
        _request.set_accept_format('json')
        _request.set_InstanceId(obj.instance_id)
        try:
            self.acsclient.do_action_with_exception(_request)
            obj.server_status.running_status = 0
            obj.server_status.save()
            self.message_user(request, 'Stop Successful', messages.SUCCESS)
        except Exception as e:
            obj.server_status.running_status = 2
            obj.server_status.save()
            self.message_user(request, 'Stop Failed: %s' % e.message, messages.ERROR)
        co_path = request.path.split('/')
        co_path[-2] = ''
        return redirect('/'.join(co_path).replace('//', '/'))
