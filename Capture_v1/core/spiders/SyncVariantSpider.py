from core.libs.handlers.SyncSpiderHandler import SyncSpiderHandler


class SyncVariantSpider(SyncSpiderHandler):
    name = 'SyncVariantSpider'
    task_name = 'sync_variant'
    task_resource = 'variant'

    def __init__(self, *args, **kwargs):
        super(SyncVariantSpider, self).__init__(*args, **kwargs)

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
        self.logger.info('Spider is Finished')
