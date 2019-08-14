# coding:utf-8

from rest_framework import serializers
from appfront.dv.StatAmazonSkuCompositeReportDv import *


'''按日统计视图'''
class StatAmazonSkuCompositeReportDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuCompositeReportDayDv
        fields = "__all__"


'''按月统计视图'''
class StatAmazonSkuCompositeReportMonthDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuCompositeReportMonthDv
        fields = "__all__"


'''按周统计视图'''
class StatAmazonSkuCompositeReportWeekDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuCompositeReportWeekDv
        fields = "__all__"