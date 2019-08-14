# -*- coding: utf-8 -*-
import abc

import scrapy

from core.libs.parts.public.SpiderRuleParts import SpiderRuleParts
from core.libs.parts.public.SpiderTaskParts import SpiderTaskParts


class SpiderCoreABC(metaclass=abc.ABCMeta):
    name = None  # 爬虫名字
    spider_parts = None  # 爬虫配件库

    @abc.abstractmethod
    def __init__(self, *args, **kwargs):
        """
        爬虫实例化入口
        :rtype: object
        """
        pass

    @abc.abstractmethod
    def _load_parts(self, parts):
        """
        爬虫加载配件(本方法必须在__init__中实现)
        :type parts: object
        """
        pass

    @abc.abstractmethod
    def process_open_spider(self):
        """
        爬虫启动
        """
        pass

    @abc.abstractmethod
    def process_close_spider(self):
        """
        爬虫关闭
        """
        pass


class SpiderCore(SpiderCoreABC, scrapy.Spider):


    spider_params = None  # 爬虫启动传参

    def __init__(self, *args, **kwargs):
        try:
            # 接收传参
            self._receive_open_params(**kwargs)
            # 查询任务
            self.task = SpiderTaskParts(task_code=kwargs.get('task_code'))
            # 解析rule
            self.rule = SpiderRuleParts(rule=kwargs.get('rule'))
            super(SpiderCore, self).__init__(*args, **kwargs)

        except Exception as e:
            self.logger.error(msg=e)
        pass

    def _receive_open_params(self, **kwargs):
        """
        爬虫接收启动传参
        :param kwargs:
        """
        self.spider_params = kwargs
        pass

    def _load_parts(self, parts):
        parts
    def process_open_spider(self):
        pass

    def process_close_spider(self):
        pass

    def parse(self, response):
        pass
