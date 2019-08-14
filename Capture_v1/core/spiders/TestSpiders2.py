# coding:utf-8
from core.libs.handlers.BaseSpiderHandler import BaseSpiderImplementation

class TestSpider2(BaseSpiderImplementation):
    name = "TestSpiders2"

    '''接收指令的Code参数'''

    def __init__(self, code=None, rule=None, *args, **kwargs):
        '''指令编码'''
        self.code = code or self.code
        '''指令规则 - 解析指令'''
        import os
        import base64
        xml_path = os.path.realpath(os.path.join('data', 'captureRuleExample.xml'))
        xml_file = open(xml_path, 'rb')
        xml_list = xml_file.readlines()
        xml_file.close()
        rule = base64.b64encode(''.join([i.decode() for i in xml_list]).encode())
        self.rule = self.load_rule(rule)
        super(TestSpider2, self).__init__(*args, **kwargs)

    def start_requests(self):
        self.logger.info('CODE: %s' % self.code)
        if self.code is not None:
            self.logger.info('Begin Capture: %s' % self.code)
            for url in self.urls:
                self.logger.info('发起请求%s' % url)

                yield self.start_request(
                    url=url,
                    callback=self.parse,
                )
        # 创建task_request_code
        # self.request_code = base64.b64encode(str('%s_%s' % (self.code, self.uuid)).encode())
        else:
            self.logger.error('Error for Request')

    def parse(self, response):
        print(response.status)
        self.logger.info(response.status)
        try:
            yield self.process_parse_item(self.process_item, response)
        except Exception as e:
            self.logger.error('抓取失败,url = %s', response.url)
            self.logger.error(e)
            import traceback;
            traceback.print_exc();

    # Bingo! Here we get the result and You can restore or output it
    def handle_spider_closed(self, spider):
        self.logger.info('结束关闭')
