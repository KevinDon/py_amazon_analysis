# coding:utf-8
# from rest_framework.utils import json
import json, math

from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

class QueryFilter:
    pageno = 1
    pagesize = 100
    pagetotal = 1
    rows = 0
    status = 200
    msg_successful = 'successful'
    msg_unsuccessful = 'unsuccessful'

    def parseRequestToFilter(self, request, dbModel, serModel):
        if(request.body is not None):
            try:
                queryset = dbModel.objects.all()

                page = PageNumberPagination()

                try:
                    if request.body != '':
                        req_params = json.loads('%s' % request.body.decode().replace('\n',''))
                    else:
                        req_params = None
                except Exception as e:
                    req_params = None
                    print('step0: %s' % e)

                # 分页
                try:
                    self.pageno = int(request.GET.get('page', 1))

                    if req_params is not None and req_params['pager'] is not None:
                        # if req_params['pager']['page'] is not None:
                        #     page.page = req_params['pager']['page']
                        #     self.pageno = int(req_params['pager']['page'])
                        # else:
                        #     page.page = self.pageno

                        if req_params['pager']['size'] is not None:
                            page.page_size = req_params['pager']['size']
                            self.pagesize = int(req_params['pager']['size'])
                        else:
                            page.page_size = self.pagesize

                except Exception as e:
                    page.page = self.pageno
                    page.page_size = self.pagesize
                    print('step1: %s' %e)

                # 字段筛选
                try:
                    if req_params is not None and req_params['filter'] != '':
                        condtions = self.parseCondtions(req_params['filter'])
                        queryset = queryset.filter(condtions)
                except Exception as e:
                    print('step2: %s' %e)

                # 排序
                try:
                    if req_params is not None and req_params['order'] is not None:
                        queryset = queryset.order_by(*req_params['order'])
                except Exception as e:
                    print('step3: %s' %e)
                    pass

                # 计算总页数
                self.rows = queryset.count()
                if self.rows > 0: self.pagetotal = math.ceil(self.rows / self.pagesize)

                # 查询
                page_roles = page.paginate_queryset(queryset=queryset, request=request, view=self)
                ser = serModel(instance=page_roles, many=True)


                return self.successful(data=ser.data)

            except Exception as e:
                print('step4: %s' %e)
                return  self.unsuccessful(msg= str(e))

        else:
            return  self.unsuccessful()

    '''解析查询条件'''
    '''
    eq : __exact 精确等于 like 'aaa'
    ieq: __iexact 精确等于 忽略大小写 ilike 'aaa'
    lk: __contains 包含 like '%aaa%'
    ilk: __icontains 包含 忽略大小写 ilike '%aaa%'，但是对于sqlite来说，contains的作用效果等同于icontains。
    gt: __gt 大于
    gte: __gte 大于等于
    lt: __lt 小于
    lte: __lte 小于等于
    in: __in 存在于一个list范围内
    lks: __startswith 以...开头
    ilks: __istartswith 以...开头 忽略大小写
    lke: __endswith 以...结尾
    ilke: __iendswith 以...结尾，忽略大小写
    rg:__range 在...范围内
    yr: __year 日期字段的年份
    mo: __month 日期字段的月份
    dy: __day 日期字段的日
    null: __isnull=True/False
    '''
    def parseField(self, field, operator, value):
        if operator.lower() == 'eq':
            result = ('%s__exact' % field, '%s' % value)
        elif operator.lower() == 'ieq':
            result = ('%s__iexact' % field, '%s' % value)
        elif operator.lower() == 'lk':
            result = ('%s__contains' % field, '%s' % value)
        elif operator.lower() == 'ilk':
            result = ('%s__icontains' % field, '%s' % value)
        elif operator.lower() == 'gt':
            ('%s__gt' % field, '%s' % value)
        elif operator.lower() == 'gte':
            result = ('%s__gte' % field, '%s' % value)
        elif operator.lower() == 'lt':
            result = ('%s__lt' % field, '%s' % value)
        elif operator.lower() == 'lte':
            result = ('%s__lte' % field, '%s' % value)
        elif operator.lower() == 'in':
            result = ('%s__in' % field, '%s' % value)
        elif operator.lower() == 'lks':
            result = ('%s__startswith' % field, '%s' % value)
        elif operator.lower() == 'ilks':
            result = ('%s__istartswith' % field, '%s' % value)
        elif operator.lower() == 'lke':
            result = ('%s__endswith' % field, '%s' % value)
        elif operator.lower() == 'ilke':
            result = ('%s__iendswith' % field, '%s' % value)
        elif operator.lower() == 'rg':
            result = ('%s__range' % field, '%s' % value)
        elif operator.lower() == 'yr':
            result = ('%s__year' % field, '%s' % value)
        elif operator.lower() == 'mo':
            result = ('%s__month' % field, '%s' % value)
        elif operator.lower() == 'dy':
            result = ('%s__day' % field, '%s' % value)
        elif operator.lower() == 'null':
            result = ('%s__isnull' % field, '%s' % True if value == 1 else False)
        else:
            result = ('%s__exact' % field, '-1#a_*xl')
        return result

    def parseCondtions(self, filter):
        condtions = Q(_connector='AND')
        for items in filter:
            subcondtions = Q(_connector='OR')
            for item in items:
                key = list(item.keys())[0]
                print('1aa %s' % key)
                value = list(item.values())[0]
                _keys = key.split('-')
                if key is None:
                    continue
                subcondtions.children.append(self.parseField(_keys[0], _keys[1], value))
            if subcondtions.__len__() > 0:
                condtions.children.append(subcondtions)
        return condtions


    '''成功返回格式'''
    def successful(self, data=[], page=None, total=None, msg=None, status=None):
        return {
            'status': status if status is not None else self.status,
            'msg': msg if msg is not None else self.msg_successful,
            'page': page if page is not None else self.pageno,
            'tp': total if total is not None else self.pagetotal,
            'tr': self.rows,
            'data': data
        }

    '''失败返回格式'''
    def unsuccessful(self, msg=None, status=500):
        return {
            'status': status,
            'msg': msg if msg is not None else self.msg_unsuccessful,
            'page': 0,
            'tp': 0,
            'tr': 0,
            'data': []
        }