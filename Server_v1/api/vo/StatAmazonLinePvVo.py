# coding:utf-8

from rest_framework import serializers
from appfront.dv.StatAmazonLinePvDv import *


'''按日统计视图'''
class StatAmazonLinePvDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonLinePvDayDv
        fields = "__all__"

'''按月统计视图'''
class StatAmazonLinePvMonthDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonLinePvMonthDv
        fields = "__all__"

'''按周统计视图'''
class StatAmazonLinePvWeekDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonLinePvWeekDv
        fields = "__all__"