# coding:utf-8

from rest_framework import serializers
from appfront.dv.StatAmazonSkuPvDv import *


'''按日统计视图'''
class StatAmazonSkuPvDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuPvDayDv
        fields = "__all__"

'''按月统计视图'''
class StatAmazonSkuPvMonthDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuPvMonthDv
        fields = "__all__"

'''按周统计视图'''
class StatAmazonSkuPvWeekDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuPvWeekDv
        fields = "__all__"