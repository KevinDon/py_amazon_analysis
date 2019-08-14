# @Time : 2019/8/8 17:10 
# @Author : Kevin
# @File : FormDashboard.py 
# @Software: PyCharm
# coding:utf-8

import os, csv, datetime, re
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu, QTableWidgetItem, QFileDialog, QTableWidgetSelectionRange

from app.lib.UtilCommon import utQTableWidgetItem, getTime, logger, utStr2Float, utStr2Int, utGetStyleContent
from app.lib.UtilDb import QueryBuildToStr
from app.model.WidgetSearchField import WidgetSearchField
from app.model.dao.DbProductAsin import Na_Product_Asin
from app.model.dao.DbProductLine import Na_Product_Line
from app.model.dao.DbProductCategory import Pub_Product_Category
from app.model.dao.DbAmazonProductCategory import Amazon_Product_Category
from app.model.dao.DbSkuKeyword import Pub_Sku_Keyword
from app.view.formDashboard import Ui_twDashboard


class WidgetDashboard(QWidget, Ui_twDashboard):
    _ = QCoreApplication.translate

    productsCount = ''
    productLineCount = ''
    categoryCount = ''
    amazonKeywordCount = ''
    amazonProductsCount= ''
    def __init__(self, mainWin):
        super(WidgetDashboard, self).__init__()
        self.mainWin = mainWin
        self.myWidget = QWidget()
        self.setupUi(self.myWidget)



        # 初始化布局
        self.initData()
        self.init()
        self.setLayout(self.myWidget.layout())



    def initData(self, _where = ''):
        try:
            # 初始加载第一页最新数据
            self.productsCount = Na_Product_Asin.select().count()
            self.amazonProductsCount = Na_Product_Asin.select().where(Na_Product_Asin.asin != '').count()
            self.productLineCount = Na_Product_Line.select().count()
            self.categoryCount = Pub_Product_Category.select().count()
            self.amazonCategory = Amazon_Product_Category.select().count()
            self.amazonKeywordCount = Pub_Sku_Keyword.select().count()
        except Exception as e:
            logger.info(e)
        pass

    def init(self):
        self.na_product_value.setText(str(self.productsCount))
        self.na_productLine_value.setText(str(self.productLineCount))
        self.na_Category_value.setText(str(self.categoryCount))
        self.amazon_produts.setText(str(self.amazonProductsCount))
        self.amazon_category.setText(str(self.amazonCategory))
        self.amazon_keywords.setText(str(self.amazonKeywordCount))

        pass
