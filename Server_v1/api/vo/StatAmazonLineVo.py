# coding:utf-8

from rest_framework import serializers
from appfront.model import ProductLineModel

'''Line资料'''
class StatAmazonLineVo(serializers.ModelSerializer):

    class Meta:
        model = ProductLineModel
        fields = "__all__"