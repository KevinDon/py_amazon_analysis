# -*- coding: utf-8 -*-
import random
import urllib.parse

import pymongo

from core.models.ProxyIpPoolModel import ProxyIpPoolModel, ProxyChannelModel


class SpiderProxyParts(object):
    spider = None  # spider instance
    proxy_type = 1  # spider proxy type
    proxy_ip_pool_db = ProxyIpPoolModel()
    proxy_channel_db = ProxyChannelModel()

    def __init__(self, spider):
        self.spider = spider
        spider.proxy_part = self

    def proxy_selector(self, proxy_type: int = 1, rule_proxy_dict: dict = None):
        """
        代理选择器
        :param rule_proxy_dict:
        :param proxy_type:
        """
        if rule_proxy_dict is None:
            rule_proxy_dict = dict()

        proxy_url = None
        if proxy_type == 1:
            # 不采用代理(使用本机代理)
            proxy_url = None
            pass
        elif proxy_type == 2:
            # 指定代理
            proxy_custom = rule_proxy_dict.get('custom', None)
            if proxy_custom is None:
                raise Exception('爬虫采用指定代理模式失败,缺少指定的代理配置(proxy.custom)')
            proxy_url = urllib.parse.urljoin(proxy_custom)
            pass
        elif proxy_type == 3:
            # 渠道代理
            _channel = rule_proxy_dict.get('channel', None)
            # todo 增加代理渠道信息调用
            if _channel is None:
                raise Exception('爬虫采用渠道代理模式失败,缺少channel的配置(proxy.channel)')
            proxy_url = self.get_proxy_by_channel(_channel)
            pass
        elif proxy_type == 4:
            # 区域代理 - 区域内选取权重优先的前20条的随机一条
            _cites = rule_proxy_dict.get('cites')
            _proxy_num = int(rule_proxy_dict.get('proxy_num', 20))
            if _cites is None:
                raise Exception('爬虫生成区域代理过滤条件错误,缺少cites的配置项(proxy.cites)')

            proxy_list = self.spider.proxy_part.proxy_db.conn.find(
                filter=dict(
                    city__in=[city.split('-')[3] for city in _cites],
                    status=1
                ),
                limit=20,
                sort=[{'priority': pymongo.ASCENDING}]
            )

            proxy_url = [proxy for proxy in proxy_list][int(random.random() * _proxy_num)]

        return proxy_url

    # def get_proxy_by_channel(self, channel):
    #     username = 'lum-customer-hl_7cd782cc-zone-static'
    #     password = 'rffbz47cy5ew'
    #     port = 22225
    #     session_id = random.random()
    #     return ('http://%s-country-au-session-%s:%s@zproxy.lum-superproxy.io:%d' %
    #             (username, session_id, password, port))

    def get_proxy_by_channel(self, channel):
        # 公司帐号
        username = 'lum-customer-hl_b84c314f-zone-static'
        password = '5eu4ypkeqsj5'
        port = 22225
        session_id = random.random()
        return ('http://%s-country-au-session-%s:%s@zproxy.lum-superproxy.io:%d' %
                (username, session_id, password, port))
