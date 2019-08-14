from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

from api.vo import *
from core.libs import QueryFilter as QF


class StatAmazonSkuTotalItemsDaySet(APIView):
    versioning_class = URLPathVersioning

    def post(self, request, *args, **kwargs):
        # 反向生成URL
        request.versioning_scheme.reverse('statamazonskutotalitemsday', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonSkuTotalItemsDayDv, StatAmazonSkuTotalItemsDayDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())


class StatAmazonSkuTotalItemsMonthSet(APIView):
    versioning_class = URLPathVersioning
    def post(self, request, *args, **kwargs):
        # 反向生成URL
        request.versioning_scheme.reverse('statamazonskutotalitemsmonth', request=request)

        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonSkuTotalItemsMonthDv, StatAmazonSkuTotalItemsMonthDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())



class StatAmazonSkuTotalItemsWeekSet(APIView):
    versioning_class = URLPathVersioning
    def post(self, request, *args, **kwargs):

        # 反向生成URL
        request.versioning_scheme.reverse('statamazonskutotalitemsweek', request=request)

        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonSkuTotalItemsWeekDv, StatAmazonSkuTotalItemsWeekDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())