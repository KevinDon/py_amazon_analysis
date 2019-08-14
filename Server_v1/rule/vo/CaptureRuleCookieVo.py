from rest_framework import serializers

from rule.model.CaptureRuleCookieModel import CaptureRuleCookieModel


class CaptureRuleCookieVo(serializers.ModelSerializer):
    class Meta:
        model = CaptureRuleCookieModel
        fields = '__all__'
        depth = 1
