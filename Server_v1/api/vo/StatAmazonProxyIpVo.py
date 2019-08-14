# coding:utf-8

from rest_framework import serializers

from system.model import ProxyIpModel

''' Proxy Ip 资料'''


class StatAmazonProxyIpVo(serializers.ModelSerializer):
    class Meta:
        model = ProxyIpModel
        fields = "__all__"
