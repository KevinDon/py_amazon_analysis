# -*- coding: utf-8 -*-

import time
# import peewee
from app.lib.db import *

'''运程服务器日志'''
class Na_Business_Report(BasePgDbModel):
    id = peewee.IntegerField()
    asin_parent = peewee.CharField()
    asin_child = peewee.CharField()
    title = peewee.CharField()
    sessions = peewee.IntegerField()
    sessions_percentage = peewee.FloatField()
    page_view = peewee.IntegerField()
    page_view_percentage = peewee.FloatField()
    buy_box_percentage = peewee.FloatField()
    units_ordered = peewee.IntegerField()
    unit_session_percentage = peewee.FloatField()
    ordered_product_sales = peewee.FloatField()
    total_order_items = peewee.IntegerField()
    report_date = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))
    created_at = peewee.DateField(default=time.strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        order_by = ('created_at',)

    '''从TW行转换到对象'''
    def fromTableWidget(self, tw, row):
        self.id = tw.item(row, 0).text()
        self.asin_parent = tw.item(row, 1).text()
        self.asin_child = tw.item(row, 2).text()
        self.title = tw.item(row, 3).text()
        self.sessions = tw.item(row, 4).text()
        self.sessions_percentage = tw.item(row, 5).text()
        self.page_view = tw.item(row, 6).text()
        self.page_view_percentage = tw.item(row, 7).text()
        self.buy_box_percentage = tw.item(row, 8).text()
        self.units_ordered = tw.item(row, 9).text()
        self.unit_session_percentage = tw.item(row, 10).text()
        self.ordered_product_sales = tw.item(row, 11).text()
        self.total_order_items = tw.item(row, 12).text()
        self.report_date = tw.item(row, 13).text()

    def add(self, **entries):
        try:
            naScriptResult = Na_Business_Report()
            naScriptResult.__dict__.update(entries)
            naScriptResult.save();
        except Exception as e:
            print(e)