from rest_framework import serializers

from rule.model import CaptureRuleUrlModel


class CaptureRuleUrlVo(serializers.ModelSerializer):
    # hosts = HostField
    class Meta:
        model = CaptureRuleUrlModel
        fields = '__all__'
