from core.libs.handlers.SyncSpiderHandler import SyncSpiderHandler


class SyncKeywordSpider(SyncSpiderHandler):
    name = 'SyncKeywordSpider'
    task_name = 'sync_keyword'
    task_resource = 'keyword'

    def __init__(self,  *args, **kwargs):
        """ 开发测试配置 """
        # import sys
        # import os
        # import base64
        # import zlib
        # from core.libs.parts.public.SpiderRuleParts import SpiderRuleParts
        # kwargs.__setitem__('task_code', 'test sync keyword spider task_code')
        # kwargs.__setitem__('rule_code', 'test sync keyword spider task_code')
        # xml_path = os.path.join(sys.path[2], 'data', 'proxySyncRuleExample.xml')
        # # rule = SpiderRuleParts._load_xml_file(xml_path)
        # rule = ''.encode()
        # kwargs.__setitem__('rule', base64.b64encode(zlib.compress(rule)))
        # '''上线后请删除'''
        super(SyncKeywordSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        self.logger.info('爬虫同步开始')
        try:
            return self.sync_requests()
        except Exception as e:
            self.logger.error('请求错误')

    def parse(self, response):
        print(response.status)
        self.logger.info(response.status)
        try:
            yield self.process_parse_item(self.process_item, response)
        except Exception as e:
            self.logger.error('爬虫处理结果失败 ,url = %s', response.url)
            self.logger.error(e)

    # Bingo! Here we get the result and You can restore or output it
    def handle_spider_closed(self, spider):
        self.logger.info('爬虫同步关键词数据结束')
