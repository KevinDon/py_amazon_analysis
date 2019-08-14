# -*- coding: utf-8 -*-
from core.libs.MongoDbHandler import MongoDB


class SpiderRuleModel(MongoDB):
    class Meta:
        db_table = 'pub_spider_rule'

    def __init__(self):
        super(SpiderRuleModel, self).__init__()
        pass
