# -*- coding: utf-8 -*-
from core.libs.XMLAnalyzer import XMLEtAnalyzer
from core.models.SpiderRuleModel import SpiderRuleModel


class SpiderRuleParts(object):
    spider = None  # spider instance
    rule_db = SpiderRuleModel()
    rule_tree = None
    rule_analyzer = None

    def __init__(self, spider):
        self.spider = spider
        spider.rule_part = self

    @staticmethod
    def _load_xml_file(xml_path):
        """
        加载xml文件 - 非必要使用
        :param xml_file:
        """
        xml_file = open(xml_path, 'rb')
        xml_list = xml_file.readlines()
        rule = ''.join([i.decode() for i in xml_list]).encode()
        xml_file.close()
        return rule

    def load_rule(self, xml_rule_str: str = None):
        """
        分析xml规则字符串(str)
        :param xml_rule_str: 应该是解压缩后的字符串
        """
        if xml_rule_str is None:
            raise Exception('Spider Rule Parts can not load a None rule string')
        # self.spider.logger.debug('爬虫接收rule内容 %s' % xml_rule_str)
        self.rule_analyzer = XMLEtAnalyzer(xml_str=xml_rule_str)
        # self.spider.logger.debug('爬虫解析rule对象 %s' % str(self.rule_analyzer.get_dict_tree()))
        self.rule_tree = self.rule_analyzer.get_dict_tree()

    def get_rule_part(self, name):
        if self.rule_tree is None:
            self.spider.logger.info('当前规则为空,默认返回空字典')
            return None
        else:
            return self.rule_tree.get(name)

    # def get_task_rule(self):
    #     return self.get_rule_part('task')
    #
    # def get_requests_rule(self):
    #     return self.get_rule_part('requests')
    #
    # def get_urls_rule(self):
    #     return self.get_rule_part('urls')
    #
    # def get_steps_rule(self):
    #     return self.get_rule_part('steps')
    #
    # def get_proxys_rule(self):
    #     return self.get_rule_part('proxys')
    #
    # def get_capture_rule(self):
    #     return self.get_rule_part('capture')


if __name__ == '__main__':
    import os, sys

    xml_path = os.path.join(sys.path[2], 'data', 'captureRuleExample.xml')
    srp = SpiderRuleParts()
    rule = srp._load_xml_file(xml_path)
    srp.load_rule(rule.decode())
    pass
