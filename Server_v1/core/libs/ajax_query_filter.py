import logging

from django.db.models import Q
from django.http import JsonResponse
from rest_framework.exceptions import APIException

from core.libs.query_filter import QueryFilter


class AQFAuthException(APIException):
    pass


class AjaxQueryFilter:
    pageno = 1
    pagesize = 100
    pagetotal = 1
    status = 200
    error_status = 500
    msg_successful = 'successful'
    msg_unsuccessful = 'unsuccessful'
    request = None
    action = None
    params = None

    def __init__(self, request):
        self.request = request

    def need_auth(self):
        try:
            if self.request.user.is_authenticated is False:
                raise AQFAuthException('You need login')
        except Exception as e:
            logging.error(e)
            raise AQFAuthException(e)

    def parse_query_params(self, request=None, fields=()):
        """
        提取request传参
        :param request:
        :param fields:
        :return:
        """
        request = request or self.request
        return {i: request.GET.get(i) for i in fields + ('conjunction',) if request.GET.get(i)}

    def parse_conditions(self, params, can_use=True):
        conditions = Q(_connector='AND')
        if can_use and params.get('status') is None:
            params.update({'status': 1})
        for item in params:
            conditions.children.append(('%s__exact' % item, '%s' % params[item]))

        return conditions

        # if 'conjunction' in params.keys():
        #     conditions = Q(_connector=params['conjunction'].upper())
        #     params.__delitem__('conditions')
        #
        # for item in params:
        #     item_spt = item.split('__')
        #     if len(item_spt) == 1 or len(item_spt[1]) < 1:
        #         result = ('%s__exact' % item_spt[0], '%s' % params[item])
        #     elif item_spt[1] == 'null':
        #         result = ('%s__isnull' % item_spt[0], '%s' % True if params[item] == 1 else False)
        #     else:
        #         result = ('%s__exact' % item_spt[0], '-1#a_*xl')
        #     conditions.children.append(result)
        #
        # return conditions

    def successful(self, data=None, msg=None, status=None):
        """
        成功返回的格式
        :param data:
        :param msg:
        :param status:
        :return:
        """
        if data is None:
            data = []
        return JsonResponse({
            'status': status if status is not None else self.status,
            'msg': msg if msg is not None else self.msg_successful,
            'data': data,
        })

    def unsuccessful(self, msg=None, status=None):
        """
        失败返回的格式
        :param msg:
        :param status:
        :return:
        """
        return JsonResponse({
            'status': status if status is not None else self.error_status,
            'msg': msg if msg is not None else self.msg_unsuccessful,
            'data': []
        })
