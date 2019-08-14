# coding:utf-8


from core.libs.handlers.CaptureSpiderHandler import CaptureSpiderHandler

# todo Splash 爬虫功能(js渲染抓取)
class CaptureSpider(CaptureSpiderHandler):

    name = "CaptureSplashSpider"

    def __init__(self, *args, **kwargs):
        '''测试数据'''
        import base64
        import os
        import sys
        import zlib
        from core.libs.parts.public.SpiderRuleParts import SpiderRuleParts
        kwargs.__setitem__('task_code','test capture spider task_code')
        kwargs.__setitem__('rule_code','test capture spider rule_code')
        xml_path = os.path.join(sys.path[2], 'data', 'captureRuleExample_jd.xml')
        rule = SpiderRuleParts._load_xml_file(xml_path)
        kwargs.__setitem__('rule',base64.b64encode(zlib.compress(rule)))
        # '''上线后请删除'''
        super(CaptureSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        try:
            for url in self.urls:
                self.logger.info('发起请求%s' % url)
                yield self.start_request(
                    url=url,
                    callback=self.parse,
                    headers=self.request_header
                )
        except Exception as e:
            self.logger.error('Error for Request')

    def parse(self, response):
        self.logger.info(response.status)
        try:
            yield self.process_parse_item(self.process_item, response)
        except Exception as e:
            import traceback;
            traceback.print_exc();
            self.logger.error('抓取失败,url = %s', response.url)
            self.logger.error(e)

    # Bingo! Here we get the result and You can restore or output it
    def handle_spider_closed(self, spider):
        self.logger.info('结束关闭')
