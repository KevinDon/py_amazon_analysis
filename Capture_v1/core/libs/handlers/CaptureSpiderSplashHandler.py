# -*- coding: utf-8 -*-


from core.libs.handlers.BaseSpiderHandler import BaseSpiderImplementation


class CaptureSpiderHandler(BaseSpiderImplementation):
    urls = []  # 爬取的urls

    # 配置储存管道与中间件
    custom_settings = {
        'DOWNLOAD_DELAY': 3,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 16,
        'CONCURRENT_REQUESTS_PER_IP': 16,
        'SPLASH_URL': 'http://192.168.1.120:8050',
        'SPLASH_COOKIES_DEBUG': True,
        'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
        'HTTPCACHE_STORAGE': 'scrapy_splash.SplashAwareFSCacheStorage',
        'SPIDER_MIDDLEWARES': {
            'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
        },
        'ITEM_PIPELINES': {
            'core.libs.pipelines.SpiderPipelines.CaptureHTMLBodyPipeline': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'core.libs.middlewares.SpiderMiddlewares.CaptureHTMLBodyMiddlewares': 543,
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
        },
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
        },
    }

    def __init__(self, *args, **kwargs):
        super(CaptureSpiderHandler, self).__init__(*args, **kwargs)

        try:
            # 生成请求头
            # header_dict = self.rule_part.get_rule_part('requests')
            # self.request_header = {i.replace('_', '-'): header_dict[i] for i in header_dict if
            #                        i in ['cookies', 'user_agent', 'accept', 'accept_language']}
            # 获取urls
            self.urls = [i.get('url', '') for i in self.task_urls]
            # self.urls = self.rules_analyzer.get_urls_text
        except Exception as e:
            import traceback;
            traceback.print_exc();
            self.logger.error(e)

    def process_spider_task(self, rule_task_dict: dict = ()):
        self.task_mode = 1
        super(CaptureSpiderHandler, self).process_spider_task(rule_task_dict)
        pass

    def process_parse_item(self, process_item, response):
        return process_item().parse_item(self, response, self.rule_part.get_rule_part('capture'))
        pass
