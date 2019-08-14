# coding:utf-8

import scrapy, os, time, traceback

class TestSpider(scrapy.Spider):
    name = "TestSpider"

    '''接收指令的Code参数'''
    def __init__(self, code=None, rule=None, *args, **kwargs):
        super(TestSpider, self).__init__(*args, **kwargs)
        '''指令编码'''
        self.code = code
        '''指令规则'''
        self.rule = rule

    def start_requests(self):
        self.logger.info('CODE: %s' % self.code)
        if (self.code is not None):
            self.logger.info('Begin Capture: %s' % self.code)
            yield scrapy.Request(
                url='http://192.168.1.227:8080',
                callback=self.parse,
                meta={
                    'cid': -10
                }
            )
        else:
            self.logger.error('Error for Request')

    def parse(self, response):
        print(response.status)
        self.logger.info(response.status)



    # Bingo! Here we get the result and You can restore or output it
    def handle_spider_closed(self, spider):
        # print(self.result_pool.get(self.asin))
        self.logger.info('结束关闭')