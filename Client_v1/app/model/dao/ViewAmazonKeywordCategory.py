# @Time : 2019/8/9 10:24 
# @Author : Kevin
# @File : ViewAmazonKeywordCategory.py 
# @Software: PyCharm
# coding:utf-8


import sys,os
import time, socket
import peewee
from app.lib.db import pgDbClection

'''运程服务器日志'''
class View_I_Amazon_Keyword_Category(peewee.Model):
    keyword = peewee.CharField()
    category = peewee.CharField()
    keyword_id = peewee.IntegerField()
    category_id = peewee.IntegerField()


    class Meta:
        database = pgDbClection().Conn()
