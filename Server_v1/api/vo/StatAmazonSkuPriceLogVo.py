# coding:utf-8

from rest_framework import serializers
from amazon.dv.StatAmazonSkuPriceLogDv import *


'''按日统计视图'''
class StatAmazonSkuPriceLogDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuPriceLogDayDv
        fields = "__all__"


'''按月统计视图'''
class StatAmazonSkuPriceLogMonthDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuPriceLogMonthDv
        fields = "__all__"

'''按周统计视图'''
class StatAmazonSkuPriceLogWeekDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuPriceLogWeekDv
        fields = "__all__"