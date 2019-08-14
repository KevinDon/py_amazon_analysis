import logging
from typing import Union


from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

from collections import Iterable

# 抓取规则XML结构
REQUEST_TEMPLATE = dict(title=None,
                        delay=None,
                        max_thread=None,
                        cookies=None,
                        user_agent=None,
                        accept='text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        accept_language='en')

URL_TEMPLATE = dict(protocol=None,
                    host=None,
                    path=None,
                    params=None)

CAPTURE_TEMPLATE = dict(title={"single": 1, "xpath": "//html/head/title/text()"},
                        meta={"single": 2, "xpath": "//html/head/meta"},
                        keyword={"single": 1, "xpath": '//html/head/meta[@name="keywords"]'},
                        head={"single": 1, "xpath": "//html/head"},
                        body={"single": 1, "xpath": "//html/body"}
                        )


class XMLException(Exception):
    pass


class XMLETConstructor:
    """ XML 规则构造器 """
    xml: Union[str, bytes]
    xml_node_template = r'<![CDATA[%s]]>'

    xml_dict = None
    xml_root = None

    def __init__(self, xml_dict=None):
        """
        实例化
        :param xml_dict: 实例化传入一个抓取规则的dict查询结果
        """
        if xml_dict is None:
            raise XMLException('Rule dict is None')
        else:
            # 读取xml文件
            for item in xml_dict:
                if type(xml_dict[item]) is not list and type(xml_dict[item]) is not str and isinstance(xml_dict[item], Iterable):
                    xml_dict[item] = xml_dict[item][item] or xml_dict[item]['value'] or None
            self.xml_dict = xml_dict
            self.dict_to_xml(self.xml_dict)
            # 获取xml_dict中的对应区域的配置

            # self.dict_to_tree(self.xml_dict)

    def dict_to_xml(self, capture_data):
        try:
            xml_root = Element('spider')  # 根节点
            request_root = SubElement(xml_root, 'requests')

            # Request
            for item in REQUEST_TEMPLATE:
                SubElement(request_root, item).text = r'<![CDATA[%s]]>' % self.xml_dict[item] or REQUEST_TEMPLATE[item]

            # Urls
            if capture_data.get('capture_rule_urls'):
                url_node = SubElement(xml_root, 'urls')
                for url in capture_data.get('capture_rule_urls'):
                    url_dict = dict(url)
                    capture_rule_node = SubElement(url_node, 'url')
                    for item in URL_TEMPLATE:
                        # todo 需要把变量注入装成字符串 ?
                        SubElement(capture_rule_node, item).text = self.xml_node_template % (url_dict[item] or '',)


            # Capture
            capture_node = SubElement(xml_root, 'capture')
            for capture_child in CAPTURE_TEMPLATE:
                capture_child_node = SubElement(capture_node, capture_child)
                for capture_child_attr in CAPTURE_TEMPLATE[capture_child]:
                    SubElement(capture_child_node, capture_child_attr).text = self.xml_node_template % CAPTURE_TEMPLATE[capture_child][capture_child_attr] or ''

            # proxys
            if capture_data.get('proxy_used') == 1:
                # 代理区域
                proxys_node_root = SubElement(xml_root, 'proxys')
                for city in capture_data.get('proxys_city'):
                    city_dict = dict(city)
                    SubElement(proxys_node_root, 'city').text = self.xml_node_template % '{0}-{1}-{2}'.format(city_dict.get('country'), city_dict.get('region'), city_dict.get('city'))

                SubElement(xml_root, 'proxys_num').text = self.xml_node_template % capture_data.get('proxys_num') or '0'

            elif capture_data.get('proxy_used') == 2:
                # 指定ip
                SubElement(xml_root, 'proxy').text = self.xml_node_template % dict(capture_data.get('proxy_used').get('host'))

            self.xml_root = xml_root

        except Exception as e:
            import traceback;
            traceback.print_exc();
            logging.error(e)

    def get_xml(self):
        self.xml = tostring(self.xml_root)
        return self.xml

    def get_xml_format(self):
        return parseString(self.get_xml()).toprettyxml()

# 开发体验
#         capture_rule = CaptureRuleModel.objects.get(id=2)
#         capture_data = CaptureRuleVo(instance=capture_rule).data
#         XMlec = XMLETConstructor(dict(capture_data))
#         xml_str = XMlec.get_xml()
#         xml_format = XMlec.get_xml_format()
