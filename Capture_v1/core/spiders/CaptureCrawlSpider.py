# -*- coding: utf-8 -*-
from core.libs.handlers.CaptureCrawlSpiderHandler import CaptureCrawlSpiderHandler

# todo 步进爬虫待开发
class CaptureCrawlSpider(CaptureCrawlSpiderHandler):
    name = "CaptureDrillSpider"

    def __init__(self, task_code=None, rule_code=None, rule=None, *args, **kwargs):
        super(CaptureCrawlSpider, self).__init__(task_code, rule_code, rule, *args, **kwargs)
