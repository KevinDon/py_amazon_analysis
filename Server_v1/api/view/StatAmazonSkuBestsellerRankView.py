from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

from api.vo import *
from core.libs import QueryFilter as QF


class StatAmazonSkuBestsellerRankDaySet(APIView):
    versioning_class = URLPathVersioning

    def post(self, request, *args, **kwargs):
        # 反向生成URL
        request.versioning_scheme.reverse('statamazonskubestsellerrankday', request=request)
        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonSkuBestsellerRankDayDv, StatAmazonSkuBestsellerRankDayDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())


class StatAmazonSkuBestsellerRankMonthSet(APIView):
    versioning_class = URLPathVersioning
    def post(self, request, *args, **kwargs):
        # 反向生成URL
        request.versioning_scheme.reverse('statamazonskubestsellerrankmonth', request=request)

        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonSkuBestsellerRankMonthDv, StatAmazonSkuBestsellerRankMonthDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())


class StatAmazonSkuBestsellerRankWeekSet(APIView):
    versioning_class = URLPathVersioning
    def post(self, request, *args, **kwargs):

        # 反向生成URL
        request.versioning_scheme.reverse('statamazonskubestsellerrankweek', request=request)

        qf = QF()
        try:
            result = qf.parseRequestToFilter(request, StatAmazonSkuBestsellerRankWeekDv, StatAmazonSkuBestsellerRankWeekDvVo)
            return Response(result)
        except APIException as e:
            print(e)
            return Response(qf.unsuccessful())