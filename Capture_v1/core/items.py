# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class CoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#
# class RequestBody(scrapy.Item):
#     url = scrapy.Field(output_processor=TakeFirst())
#     title = scrapy.Field(output_processor=TakeFirst())
#     header = scrapy.Field(output_processor=TakeFirst())
#     htmlBody = scrapy.Field(output_processor=TakeFirst())
#     capture_at = scrapy.Field(output_processor=TakeFirst())
#     task_code = scrapy.Field(output_processor=TakeFirst())
#     pass
