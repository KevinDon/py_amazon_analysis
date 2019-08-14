# coding:utf-8

from rest_framework import serializers
from appfront.dv.StatAmazonLineUvDv import *


'''按日统计视图'''
class StatAmazonLineUvDayDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonLineUvDayDv
        fields = "__all__"

'''按月统计视图'''
class StatAmazonLineUvMonthDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonLineUvMonthDv
        fields = "__all__"

'''按周统计视图'''
class StatAmazonLineUvWeekDvVo(serializers.ModelSerializer):

    class Meta:
        model = StatAmazonLineUvWeekDv
        fields = "__all__"