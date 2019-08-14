import base64
import os
import zlib

from core.libs.handlers.SyncSpiderHandler import SyncSpiderHandler


class SyncProductSpider(SyncSpiderHandler):
    name = 'SyncProductSpider'
    task_name = 'sync_product'
    task_resource = 'product'

    def __init__(self, *args, **kwargs):
        """ 开发测试配置 """
        # '''测试数据'''
        # import sys
        # from core.libs.parts.public.SpiderRuleParts import SpiderRuleParts
        # kwargs.__setitem__('task_code', 'test sync product spider task_code')
        # kwargs.__setitem__('rule_code', 'test sync product spider task_code')
        # xml_path = os.path.join(sys.path[2], 'data', 'proxySyncRuleExample.xml')
        # rule = SpiderRuleParts._load_xml_file(xml_path)
        # kwargs.__setitem__('rule', base64.b64encode(zlib.compress(rule)))
        # '''上线后请删除'''
        super(SyncProductSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        self.logger.info('Spider %s Begin Requests!' % __class__)
        try:
            return self.sync_requests()
        except Exception as e:
            self.logger.error('Error for Request')

    def parse(self, response):
        print(response.status)
        self.logger.info(response.status)
        try:
            yield self.process_parse_item(self.process_item, response)
        except Exception as e:
            self.logger.error('Spider process item failed ,url = %s', response.url)
            self.logger.error(e)

    # Bingo! Here we get the result and You can restore or output it
    def handle_spider_closed(self, spider):
        self.logger.info('爬虫同步产品数据结束')
