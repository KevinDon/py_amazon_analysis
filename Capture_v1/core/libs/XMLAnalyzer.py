# -*- coding: utf-8 -*-
import html
import logging
import os
import re
import sys
import urllib
import itertools
from string import Template
from urllib.parse import urlencode
from xml.etree.cElementTree import ElementTree as ET, fromstring, fromstringlist

from core.libs.LocalConfigHandler import LocalConfigHandler
from core.libs.MongoDbHandler import MongoDB


class XMLEtAnalyzer(ET):
    """爬虫项目 任务配置 XML文件 解析器"""

    def __init__(self, xml_file=None, xml_str=None):
        """
        实例化
        优先处理字符串传入rule
        :param xml_file: XML file xml文件路径
        :param xml_str: XML str xml字符串 单行str文本
        """
        if xml_str is not None:
            if re.match('^<\?xml', xml_str) is None:
                xml_str = ''.join(('<?xml version="1.0" encoding="utf-8" ?>', xml_str))
            if type(xml_str) is list:
                super(XMLEtAnalyzer, self).__init__(element=fromstringlist(xml_str))
            else:
                super(XMLEtAnalyzer, self).__init__(element=fromstring(xml_str))
        else:
            super(XMLEtAnalyzer, self).__init__(file=xml_file)

    @property
    def get_urls(self):
        """
        获取urls节点
        :return: list(node)
        """
        return list(self.iter('urls'))

    @property
    def get_all_urls_text(self):
        """
        获取所有url拼装后的文本
        :return: list('http://www.example.com/?a=1&b=2',...)
        (url参数中文参数已转码)
        [
            'http://amazon.com.au/?category=beautify&page=2&page2=None',
            'http://amazon.com.au/?category=beautify%E4%B8%AD%E6%96%87&keyword=beautify&page=2',
            'http://amazon.com.au/?category=beautify&page=2'
        ]
        """
        from core.libs.CommonUnit import getVariantValueList
        config = LocalConfigHandler()
        text_list = []
        try:
            urls = list(self.iter('url'))
            for url_item in urls:
                # 每一大组urls使用想用的page变量,需要单独抽离处理
                variant_injection_list = {}
                # 捕获配置中存在的变量列表
                # variant_list = re.findall("\${(%s)}" % '|'.join((config.config.options('resources'))), params_str.text)
                # 提取url配置中出现的变量名 并 去重
                variant_list = list(set(re.findall("\${(.*?)}", self.get_element(url_item, 'path', './path').text or '')))
                variant_list += list(set(re.findall("\${(.*?)}", self.get_element(url_item, 'params', './params').text or '')))
                # variant_regex = list(re.finditer("\${(.*?)}", self.get_element(url_item, 'params', './params').text or ''))
                # variant_list = [variant_regex[i.span()[0]:i.span()[1]] for i in variant_regex]
                if variant_list:
                    # 获取系统变量库中允许输入的变量词典
                    variant_value_list = getVariantValueList()
                    # func_diff_keyword = lambda: list(set(variant_list).difference(set(list(map(lambda t: t.replace(':', '_'), variant_value_list)))))
                    # if len(func_diff_keyword()) != 0:
                    #     # 模板中存在配置中不允许的变量名
                    #     raise Exception('Spider url params has illegal variant name :%s' % str(func_diff_keyword()))
                    # 有变量注入
                    logging.info('爬虫解析变量注入')
                    # 遍历当前url配置下的condition节点,生成注入变量表
                    for variant in variant_list:
                        variant_injection_list[variant] = []
                        # condition 节点
                        variant_element = self.get_element(url_item, variant, './condition/%s' % variant)
                        # type 变量类型
                        variant_type = self.get_element(variant_element, 'type', './type')
                        # if variant_type.text == 'page':
                        #     page 页面范围抽离
                        # urls_page_element = variant_type
                        # break
                        # customs 自定义节点
                        variant_customs = self.get_elements(variant_element, './custom')
                        # range 范围节点
                        variant_range = self.get_element(variant_element, 'range', './range')

                        if variant_type.text == 'var':
                            # 变量类型
                            if variant_customs is not None:
                                # 自定义变量值提取
                                for var_cus in variant_customs:
                                    variant_injection_list[variant].append(var_cus.text)
                            elif variant_range is not None:
                                # 查询对应的资源进行赋值范围提取
                                variant_element_resource = self.get_element(variant_element, 'resource', './resource').text.split(':')
                                if variant_element_resource[0] in config.config.options('resources'):
                                    variant_range_db = MongoDB('pub_%s' % variant_element_resource[0])
                                    if variant_range.text == '__all__':
                                        resource_collection = variant_range_db.conn.find({'status':1}, {variant_element_resource[1]: 1})
                                        variant_injection_list[variant] += [coll.get(variant_element_resource[1]) for coll in resource_collection]
                                    # todo 可增加其他范围的查询条件
                        elif variant_type.text == 'page':
                            # 分页类型
                            if variant_customs is not None:
                                for var_cus in variant_customs:
                                    variant_injection_list[variant].append(var_cus.text)
                            elif variant_range is not None:
                                # 生成页码范围
                                variant_range_num = variant_range.text.split(':')
                                variant_injection_list[variant] += list(range(int(variant_range_num[0]), int(variant_range_num[1]) + 1, int(variant_range_num[2])))
                        pass
                    # 变量值表对齐并降维
                    flat_var_list = itertools.product(*[variant_injection_list[i] for i in variant_injection_list])
                    # 合并变量表与变量值表,得到变量词典表集合
                    flat_list = map(lambda v: {i[1]: urllib.parse.quote(str(v[i[0]])) for i in enumerate(variant_list)}, flat_var_list)
                    func_url_format = lambda u, p: Template(urllib.parse.urlunsplit([k.text or '' for k in u.getchildren()[0:5]])).substitute(p)
                    # 遍历变量词典表集合,采用url模板生成url
                    text_list += [func_url_format(url_item, flat_item) for flat_item in flat_list]
                else:
                    text_list += [k.text or '' for k in url_item.getchildren()[0:5]]
            yield text_list
        except Exception as e:
            import traceback;
            traceback.print_exc();
            logging.error('XML解析错误')
            logging.error(e)
        finally:
            return text_list

    @property
    def get_requests(self):
        """
        获取请求配置节点
        :return:
        """
        return list(self.iter('requests'))

    @property
    def get_requests_dict(self):
        """
        获取请求配置节点的dict
        :return: dict('delay':1,...)
        {
            'delay': '1',
            'max_thread': '16',
            'cookies': '123',
            'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/68.0.3440.106 Safari/537.36',
            'user_accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        """
        try:
            items = list(self.iter('requests'))[0].getchildren()
            return {i.tag: i.text for i in items}
        except Exception as e:
            logging.error('XML解析错误')
            logging.info(e)
            return {}

    @property
    def get_task(self):
        return list(self.iter('task'))

    @property
    def get_task_dict(self):
        try:
            items = list(self.iter('task'))[0].getchildren()
            return {i.tag: i.text for i in items}
        except Exception as e:
            logging.error('XML解析错误')
            logging.info(e)
            return {}

    @property
    def get_proxy(self):
        """
        获取代理节点
        :return:
        """
        return list(self.iterfind('proxys/proxy'))

    @property
    def get_proxy_list(self):
        """
        获取代理配置列表
        :return:
        [
            {'type': '1', 'proxy': '8.8.8.8'},
            {'type': '1', 'proxy': '8.8.8.7'},
            {'type': '1', 'proxy': '8.8.8.9'},
            {'type': '1', 'proxy': '8.8.8.6'}
        ]
        """
        proxy_list = self.get_proxy
        return [{**i.attrib, 'proxy': i.text} for i in proxy_list]

    def node_has_children(self, node=None):
        return node and len(node.getchildren()) > 0

    def get_tree(self, node=None, node_list=None):
        """
        遍历XML节点树
        :param node: 起始节点
        :param node_list: 当前节点列表
        :return: 遍历节点树 list(dict(),dict(),dict(child_node:list()))
        """

        if node_list is None:
            node_list = []
        if node is None:
            node = self._root

        children = node.getchildren()
        if len(children) > 0:
            for child in children:
                if child.getchildren():
                    child_list = self.get_tree(node=child)
                else:
                    child_list = []

                child_node = dict(name=child.tag, value=child.text, children=child_list, attrib=child.attrib, **child)
                node_list.append(child_node)

        return node_list

    def get_dict_tree(self, node=None, node_dict=None):
        """
        获取xml字典树
        :param node:
        :param node_dict:
        :return:
        """
        if node is None:
            node = self._root
        if node_dict is None:
            node_dict = {}

        if node.tag == 'items':
            return [self.get_dict_tree(item) for item in node.getchildren()]

        if node.getchildren():
            for child in node.getchildren():
                node_dict[child.tag] = self.get_dict_tree(child)
        else:
            node_dict = node.text
        return node_dict

    @property
    def get_all_rules(self):
        rules_area = ('requests', 'urls')
        all_rules = {i: None for i in rules_area}
        # 结构首层
        for node_area in self._root.getchildren():
            if node_area.tag == 'urls':
                all_rules['urls'] = self.get_all_urls_text

            elif node_area.tag == 'proxys':
                all_rules['proxys'] = list()
                all_rules['proxy_used'] = True
                for proxy_area in node_area.getchildren():
                    proxy_area_item = proxy_area.text.split('-')
                    all_rules['proxys'].append({
                        'country': proxy_area_item[0],
                        'region': proxy_area_item[1],
                        'city': proxy_area_item[2]}
                    )

            elif node_area.tag == 'proxys_num':
                all_rules['proxys_num'] = node_area.text
                all_rules['proxy_used'] = True
            elif node_area.tag == 'proxy':
                all_rules['proxy'] = node_area.text
                all_rules['proxy_used'] = False

            elif node_area.tag == 'capture':
                all_rules[node_area.tag] = {
                    node_capture.tag: {node_capture_attr.tag: node_capture_attr.text for node_capture_attr in
                                       node_capture.getchildren()} for node_capture in node_area.getchildren()}
                # for node_capture in node_area.getchildren():
                #     node_capture_dict = {node_capture_attr.tag: node_capture_attr.text for node_capture_attr in node_capture.getchildren()}

            elif self.node_has_children(node_area):
                all_rules[node_area.tag] = {node_child_area.tag: node_child_area.text for node_child_area in
                                            node_area.getchildren()}

        return all_rules

    @property
    def get_request_header(self):
        return self.get_all_rules.get('requsets')

    def get_elements(self, node_element=None, xpath=None):
        """
        相对多个节点
        :param node_element:
        :param xpath:
        :return:
        """
        if node_element is None or xpath is None:
            return None
        else:
            match_element = list(node_element.iterfind(xpath))
            if len(match_element) > 0:
                return match_element
            else:
                return None

    def get_element(self, node_element=None, name=None, xpath=None, index=0):
        """
        单个节点
        :param node_element:
        :param name:
        :param xpath:
        :param index:
        :return:
        """
        if node_element is None or xpath is None:
            return None
        else:
            match_element = list(node_element.iterfind(xpath))
            if name is not None and len(match_element) > 0 and match_element[index].tag == name:
                return match_element[index]
            else:
                return None


if __name__ == '__main__':
    xml_file = os.path.join(sys.path[2], 'data', 'captureRuleExample.xml')
    XMLEA = XMLEtAnalyzer(xml_file)
    rules = XMLEA.get_all_rules
    pass
