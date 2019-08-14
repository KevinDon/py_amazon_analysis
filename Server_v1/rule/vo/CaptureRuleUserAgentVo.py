from rest_framework import serializers

from rule.model import CaptureRuleUserAgentModel


class CaptureRuleUserAgentVo(serializers.ModelSerializer):
    class Meta:
        model = CaptureRuleUserAgentModel
        fields = '__all__'
        depth = 1
