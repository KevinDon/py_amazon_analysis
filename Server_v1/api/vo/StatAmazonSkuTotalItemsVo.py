# coding:utf-8

from rest_framework import serializers
from appfront.dv.StatAmazonSkuTotalItemsDv import *


'''按日统计视图'''
class StatAmazonSkuTotalItemsDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuTotalItemsDayDv
        fields = "__all__"

'''按月统计视图'''
class StatAmazonSkuTotalItemsMonthDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuTotalItemsMonthDv
        fields = "__all__"

'''按周统计视图'''
class StatAmazonSkuTotalItemsWeekDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonSkuTotalItemsWeekDv
        fields = "__all__"