# coding:utf-8

from django import forms
from django.utils.translation import ugettext as _
from django.core.handlers.base import logger

from system.model import ProxyIpModel, RegionIpModel
from dictionary.model import *
from django.forms import fields, widgets
import socket,struct


class ProxyIpForm(forms.ModelForm):

    class Meta:
        model = ProxyIpModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProxyIpForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ProxyIpForm, self).clean()
        if cleaned_data.get("city") is None and cleaned_data.get("region") is None and cleaned_data.get("country") is None:
            proxy_ip = cleaned_data.get("proxy_ip")
            ip_int = socket.ntohl(struct.unpack("I", socket.inet_aton(proxy_ip))[0])
            region = RegionIpModel.objects.filter(ip_from__lte=ip_int, ip_to__gte=ip_int).first()
            if region is not None:
                cleaned_data['city'] = region.city
                cleaned_data['region'] = region.region
                cleaned_data['country'] = region.country
                cleaned_data['country_code'] = region.country_code
        return cleaned_data

