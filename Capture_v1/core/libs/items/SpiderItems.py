import json

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Identity

from core.libs.CommonUnit import getNowTime


class BaseSpiderItem(scrapy.Item):
    """
    基础内容提取处理类
    """
    target_url = scrapy.Field(output_processor=TakeFirst())
    html = scrapy.Field(output_processor=TakeFirst())
    task_code = scrapy.Field(output_processor=TakeFirst())
    rule_code = scrapy.Field(output_processor=TakeFirst())
    capture_code = scrapy.Field(output_processor=TakeFirst())
    request_code = scrapy.Field(output_processor=TakeFirst())
    job_code = scrapy.Field(output_processor=TakeFirst())
    capture_at = scrapy.Field(output_processor=TakeFirst())
    status = scrapy.Field(output_processor=TakeFirst())

    def parse_item(self, spider, response):
        """
        内容抓取
        用于提取项目内容,除了xml capture中的规则外,自动增加单次抓取动作的信息
        :param spider: 当前spider
        :param response: 当前请求响应
        :return: item_loader.load_item() -> item
        """
        item_loader = ItemLoader(item=self, response=response)
        item_loader.add_value('html', response.body.decode('utf-8'))
        item_loader.add_value('target_url', response.url)
        item_loader.add_value('task_code', spider.task_code)
        item_loader.add_value('rule_code', spider.rule_code)
        item_loader.add_value('job_code', spider.job_code)
        item_loader.add_value('capture_code', spider.rule_code)
        item_loader.add_value('request_code', response.meta['request_code'] or '')
        item_loader.add_value('status', 200)
        return item_loader.load_item()


class CaptureSpiderItem(BaseSpiderItem):

    def parse_item(self, spider, response, capture_rules=None):
        """
        内容抓取
        用于提取项目内容,除了xml capture中的规则外,自动增加单次抓取动作的信息
        :param spider: 当前spider
        :param response: 当前请求响应
        :param capture_rules: 当前spider配置的capture节点内容 -> dict
        :return: item_loader.load_item() -> item
        """
        item_loader = ItemLoader(item=self, response=response)
        if capture_rules is not None:
            for item in capture_rules:
                capture_rule = capture_rules[item]
                item_loader.add_xpath(item, capture_rule['xpath'])

        # 使用response本身的编码进行解码
        item_loader.add_value('html', response.body.decode(response.encoding))
        # item_loader.add_value('body', '')
        item_loader.add_value('target_url', response.url)
        item_loader.add_value('task_code', spider.task_code)
        item_loader.add_value('rule_code', spider.rule_code)
        item_loader.add_value('capture_code', spider.rule_code)
        item_loader.add_value('job_code', spider.job_code)
        item_loader.add_value('request_code', response.meta['request_code'] or '')
        item_loader.add_value('status', 200)
        return item_loader.load_item()


class ApiSyncSpiderItem(BaseSpiderItem):
    status = scrapy.Field(output_processor=TakeFirst())
    msg = scrapy.Field(output_processor=TakeFirst())
    data = scrapy.Field(output_processor=Identity())
    page = scrapy.Field(output_processor=TakeFirst())
    tp = scrapy.Field(output_processor=TakeFirst())
    tr = scrapy.Field(output_processor=TakeFirst())

    def parse_item(self, spider, response):
        """
        内容抓取
        用于提取项目内容,除了xml capture中的规则外,自动增加单次抓取动作的信息
        :param spider: 当前spider
        :param response: 当前请求响应
        :return: item -> item
        """
        try:
            response_dict = json.loads(response.body)
            item_loader = ItemLoader(item=self, response=response)
            item_loader.add_value('status', response_dict.get('status'))
            item_loader.add_value('msg', response_dict.get('msg'))
            item_loader.add_value('data', response_dict.get('data'))
            item_loader.add_value('page', response_dict.get('page'))
            item_loader.add_value('tp', response_dict.get('tp'))
            item_loader.add_value('tr', response_dict.get('tr'))
            return item_loader.load_item()
        except Exception as e:
            spider.logger.error('响应接收非标准API REST JSON格式')
            spider.logger.error(e)
            return self


class AjaxSyncSpiderItem(BaseSpiderItem):
    status = scrapy.Field(output_processor=TakeFirst())
    msg = scrapy.Field(output_processor=TakeFirst())
    data = scrapy.Field(output_processor=Identity())

    def parse_item(self, spider, response):
        """
        内容抓取
        用于提取项目内容,除了xml capture中的规则外,自动增加单次抓取动作的信息
        :param spider: 当前spider
        :param response: 当前请求响应
        :return: item -> item
        """
        try:
            response_dict = json.loads(response.body)
            item_loader = ItemLoader(item=self, response=response)
            item_loader.add_value('status', response_dict.get('status'))
            item_loader.add_value('msg', response_dict.get('msg'))
            item_loader.add_value('data', response_dict.get('data'))
            return item_loader.load_item()
        except Exception as e:
            spider.logger.error('响应接收非标准JSON格式')
            spider.logger.error(e)
            return self
