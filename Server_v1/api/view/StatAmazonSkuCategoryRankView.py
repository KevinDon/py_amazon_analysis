from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

from api.vo import *
from core.libs import QueryFilter as QF


class StatAmazonSkuCategoryRankDaySet(APIView):
    versioning_class = URLPathVersioning

    def post(self, request, *args, **kwargs):
        # 反向生成URL
        request.versioning_scheme.reverse('statamazonskucategoryrankday', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonSkuCategoryRankDayDv, StatAmazonSkuCategoryRankDayDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())


class StatAmazonSkuCategoryRankMonthSet(APIView):
    versioning_class = URLPathVersioning
    def post(self, request, *args, **kwargs):
        # 反向生成URL
        request.versioning_scheme.reverse('statamazonskucategoryrankmonth', request=request)

        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonSkuCategoryRankMonthDv, StatAmazonSkuCategoryRankMonthDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())


class StatAmazonSkuCategoryRankWeekSet(APIView):
    versioning_class = URLPathVersioning
    def post(self, request, *args, **kwargs):

        # 反向生成URL
        request.versioning_scheme.reverse('statamazonskucategoryrankweek', request=request)

        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonSkuCategoryRankWeekDv, StatAmazonSkuCategoryRankWeekDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())