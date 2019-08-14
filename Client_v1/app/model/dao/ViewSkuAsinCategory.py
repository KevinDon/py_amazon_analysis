# @Time : 2019/8/9 13:06 
# @Author : Kevin
# @File : ViewSkuAsinCategory.py 
# @Software: PyCharm
# coding:utf-8


import sys,os
import time, socket
import peewee
from app.lib.db import pgDbClection

'''运程服务器日志'''
class View_I_Amazon_Sku_Asin_Category(peewee.Model):
    sku_id = peewee.IntegerField()
    sku = peewee.CharField()
    asin = peewee.CharField()
    amazon_category = peewee.CharField()
    amazon_category_id = peewee.CharField()
    category = peewee.CharField()
    category_id = peewee.IntegerField()
    line = peewee.CharField()
    line_id = peewee.IntegerField()


    class Meta:
        database = pgDbClection().Conn()
