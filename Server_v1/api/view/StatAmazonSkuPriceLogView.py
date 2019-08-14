from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

from api.vo import *
from core.libs import QueryFilter as QF


class StatAmazonSkuPriceLogDaySet(APIView):
    versioning_class = URLPathVersioning

    def post(self, request, *args, **kwargs):
        # 反向生成URL
        request.versioning_scheme.reverse('statamazonskupricelogday', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonSkuPriceLogDayDv, StatAmazonSkuPriceLogDayDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())


class StatAmazonSkuPriceLogMonthSet(APIView):
    versioning_class = URLPathVersioning
    def post(self, request, *args, **kwargs):
        # 反向生成URL
        request.versioning_scheme.reverse('statamazonskupricelogmonth', request=request)

        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonSkuPriceLogMonthDv, StatAmazonSkuPriceLogMonthDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())


class StatAmazonSkuPriceLogWeekSet(APIView):
    versioning_class = URLPathVersioning
    def post(self, request, *args, **kwargs):

        # 反向生成URL
        request.versioning_scheme.reverse('statamazonskupricelogweek', request=request)

        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonSkuPriceLogWeekDv, StatAmazonSkuPriceLogWeekDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())