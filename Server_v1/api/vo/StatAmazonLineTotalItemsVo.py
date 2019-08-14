# coding:utf-8

from rest_framework import serializers
from appfront.dv.StatAmazonLineTotalItemsDv import *


'''按日统计视图'''
class StatAmazonLineTotalItemsDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonLineTotalItemsDayDv
        fields = "__all__"

'''按月统计视图'''
class StatAmazonLineTotalItemsMonthDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonLineTotalItemsMonthDv
        fields = "__all__"

'''按周统计视图'''
class StatAmazonLineTotalItemsWeekDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonLineTotalItemsWeekDv
        fields = "__all__"