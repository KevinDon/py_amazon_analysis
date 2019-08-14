# @Time : 2019/8/1 15:17 
# @Author : Kevin
# @File : DbAmazonCategoryKeywordRelation.py 
# @Software: PyCharm
# coding:utf-8


import sys,os
import time, socket
import peewee
from app.lib.db import pgDbClection

'''运程服务器日志'''
class Amazon_Product_Category_Keyword_Relation(peewee.Model):
    id = peewee.IntegerField()
    amazon_category_id = peewee.IntegerField()
    amazon_keyword_id = peewee.IntegerField()


    class Meta:
        database = pgDbClection().Conn()

    def add(self, **entries):
        try:
            pubScriptResult = Amazon_Product_Category_Keyword_Relation()
            pubScriptResult.__dict__.update(entries)
            pubScriptResult.save()
        except Exception as e:
            print(e)