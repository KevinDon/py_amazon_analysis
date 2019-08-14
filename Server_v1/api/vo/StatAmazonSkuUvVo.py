# coding:utf-8

from rest_framework import serializers
from appfront.dv.StatAmazonSkuUvDv import *


'''按日统计视图'''
class StatAmazonSkuUvDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuUvDayDv
        fields = "__all__"

'''按月统计视图'''
class StatAmazonSkuUvMonthDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuUvMonthDv
        fields = "__all__"

'''按周统计视图'''
class StatAmazonSkuUvWeekDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuUvWeekDv
        fields = "__all__"