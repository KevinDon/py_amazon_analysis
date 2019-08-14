import logging
from xml.etree import ElementTree as ET

from rest_framework import serializers

from rule.model.CaptureRuleModel import CaptureRuleModel
from rule.vo.CaptureRuleScrapyServerVo import CaptureRuleScrapyServerVo
from rule.vo.CaptureRuleUserAgentVo import CaptureRuleUserAgentVo
from rule.vo.CaptureRuleCookieVo import CaptureRuleCookieVo
from rule.vo.CaptureRuleUrlVo import CaptureRuleUrlVo
from system.vo import RegionVo


class CaptureRuleVo(serializers.ModelSerializer):

    cookies = CaptureRuleCookieVo(many=False)
    user_agent = CaptureRuleUserAgentVo(many=False)
    scrapy_server = CaptureRuleScrapyServerVo(many=False,label='Scrapy Server')

    capture_rule_urls = CaptureRuleUrlVo(many=True)
    proxys_city = RegionVo(many=True)

    class Meta:
        model = CaptureRuleModel
        fields = '__all__'
        depth = 3

    def get_xml_string(self, capture_rule, task_code=None):
        try:
            xml_root = ET.Element("spider")
            area_nodes = ('task', 'request','proxys', 'urls', 'capture')
            for an in area_nodes:
                area_node = ET.SubElement(xml_root, an)
                if an == 'request':
                    pass
        except Exception as e:
            logging.error(e)



    class xml_structural:
        structure = dict({})

