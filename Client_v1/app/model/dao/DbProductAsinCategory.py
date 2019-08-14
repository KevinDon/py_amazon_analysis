# @Time : 2019/7/11 13:19 
# @Author : Kevin
# @File : DbProductAsinCategory.py 
# @Software: PyCharm
# -*- coding: utf-8 -*-
import sys,os
import time, socket
import peewee
from app.lib.db import pgDbClection

'''运程服务器日志'''
class Pub_Product_Asin_Category_Relation(peewee.Model):
    id = peewee.IntegerField()
    product_id = peewee.IntegerField()
    category_id = peewee.IntegerField()



    class Meta:
        database = pgDbClection().Conn()