# -*- coding: utf-8 -*-


from core.libs.handlers.BaseSpiderHandler import BaseSpiderImplementation


class CaptureSpiderHandler(BaseSpiderImplementation):
    urls = []  # 爬取的urls

    # 配置储存管道与中间件
    custom_settings = {
        # todo 转移到xml配置中
        # 开启节流模式,scrapy内部根据请求流量进行队列执行
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_DEBUG': True,
        'COOKIES_ENABLED': False,
        # 下载延迟
        'DOWNLOAD_DELAY': 0.5,
        # 请求开始延迟
        'AUTOTHROTTLE_START_DELAY': 0.1,
        # 下载线程
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 20,
        # 请求线程
        'CONCURRENT_REQUESTS': 100,
        # 每个域名的请求线程
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'ITEM_PIPELINES': {
            'core.libs.pipelines.SpiderPipelines.CaptureHTMLBodyPipeline': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'core.middlewares.RandomUserAgentMiddleware': 300,
            'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
            'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 400,
            'core.libs.middlewares.SpiderMiddlewares.CaptureHTMLBodyMiddlewares': 543,
            'scrapy.downloadermiddlewares.chunked.ChunkedTransferMiddleware': 830,
            'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
        },
    }

    def __init__(self, *args, **kwargs):
        super(CaptureSpiderHandler, self).__init__(*args, **kwargs)

    def process_spider_task(self, rule_task_dict: dict = ()):
        self.task_mode = 1
        super(CaptureSpiderHandler, self).process_spider_task(rule_task_dict)
        pass

    def process_parse_item(self, process_item, response):
        return process_item().parse_item(self, response, self.rule_part.get_rule_part('capture'))
        pass
