# @Time : 2019/7/17 14:29 
# @Author : Kevin
# @File : DbProductAsinAmazonCategory.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import sys,os
import time, socket
import peewee
from app.lib.db import pgDbClection

'''运程服务器日志'''
class Na_Product_Asin_Amazon_Category(peewee.Model):
    id = peewee.IntegerField()
    productasinmodel_id = peewee.IntegerField()
    amazonproductcategorymodel_id = peewee.IntegerField()


    class Meta:
        database = pgDbClection().Conn()