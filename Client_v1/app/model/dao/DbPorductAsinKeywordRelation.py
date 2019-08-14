# @Time : 2019/7/25 17:54 
# @Author : Kevin
# @File : DbPorductAsinKeywordRelation.py 
# @Software: PyCharm
# coding:utf-8

import sys,os
import time, socket
import peewee
from app.lib.db import pgDbClection

'''运程服务器日志'''
class Pub_Product_Asin_Keyword_Relation(peewee.Model):
    id = peewee.IntegerField()
    keyword_id = peewee.IntegerField()
    product_id = peewee.IntegerField()
    update_at = peewee.DateField()


    class Meta:
        database = pgDbClection().Conn()