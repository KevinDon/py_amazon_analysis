# coding:utf-8

from rest_framework import serializers
from appfront.dv.StatAmazonSkuBuyBoxDv import *
from appfront.model import ProductAsinModel

'''SKU资料'''
class StatAmazonSkuVo(serializers.ModelSerializer):

    class Meta:
        model = ProductAsinModel
        fields = "__all__"