# @Time : 2019/7/20 10:11 
# @Author : Kevin
# @File : FormProductAsinAmazonCategory.py 
# @Software: PyCharm
# coding:utf-8

import os, csv, datetime, re, time, xlrd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu, QTableWidgetItem, QFileDialog, QTableWidgetSelectionRange

from app.lib.UtilCommon import getTime, utQTableWidgetItem, logger, utStr2Float, utStr2Int, utGetStyleContent
from app.lib.UtilDb import QueryBuildToStr
from app.model.WidgetSearchField import WidgetSearchField

'''导入对应的表'''
from app.model.dao.DbProductAsin import Na_Product_Asin
from app.model.dao.DbAmazonProductCategory import Amazon_Product_Category
from app.model.dao.DbProductAsinAmazonCategory import Na_Product_Asin_Amazon_Category
from app.model.dao.ViewSkuAsinCategory import View_I_Amazon_Sku_Asin_Category
from app.model.dao.VIewSkuAsinCategoryNormal import View_I_Amazon_Sku_Asin_Category_Normal

from app.model.vo.MdUser import User
from app.view.formProductAsinAmazonCategory import  Ui_ProductAsinAmazonCategoryForm


class WidgetProductAmazonCategory(QWidget, Ui_ProductAsinAmazonCategoryForm):

    def __init__(self, mainWin):
        super(WidgetProductAmazonCategory, self).__init__()
        self.mainWin = mainWin
        self.myWidget = QWidget()
        self.setupUi(self.myWidget)
        self.canMoveView = False
        # 搜索窗口
        self.search_box = None
        self.searchObj = {
            "fields": [
                {'name': 'sku', 'label': 'SKU', 'type': 'string'}
                , {'name': 'category', 'label': 'Category', 'type': 'string'}
            ],
        }

        self.pageSize = 10000

        self.tbInputCsv.clicked.connect(self.actTbInputSkuAndCategoryClicked)
        self.tbRefresh.clicked.connect(self.actTbRefreshClicked)

        # 隐藏导入SKU与分类关系按钮
        # self.pushButton.clicked.connect(self.actTbInputSkuAndCategoryClicked)
        #self.pushButton.setHidden(True)

        # self.tbActionLog.clicked.connect(self.actTbCatLog)
       # self.tbActionLog.setHidden(True)

        self.tbSelection.clicked.connect(self.actTbSelectionClicked)
        self.tbUnselection.clicked.connect(self.actTbUnselectionClicked)
        self.tbInvertSelection.clicked.connect(self.actTbInvertSelectionClicked)
        self.tbDelete.clicked.connect(self.actTbDeleteClicked)
        self.twProductAsinAmazonCategoryList.itemSelectionChanged.connect(self.actTwProductListSelectionChanged)

        self.tbSearch.clicked.connect(self.actTbSearchClicked)

        # 初始化布局
        self.initLayout()
        self.setLayout(self.myWidget.layout())
        self.initData()

    def initLayout(self):
        self.twProductAsinAmazonCategoryList.setColumnHidden(0, True),
        self.twProductAsinAmazonCategoryList.setColumnWidth(1, 280)
        self.twProductAsinAmazonCategoryList.setColumnWidth(2, 280)
        pass

    '''高级搜索数据'''

    def goSearch(self, conditions, method=None):
        _table_ent = 'View_I_Amazon_Sku_Asin_Category_Normal'
        _where = QueryBuildToStr(_table_ent, conditions)
        print(conditions)
        self.initData(_where)
        pass

    def initData(self, _where=''):
        try:

            # 初始加载第一页最新数据，过滤Status为3的记录
            rows = View_I_Amazon_Sku_Asin_Category_Normal.select(View_I_Amazon_Sku_Asin_Category_Normal.sku,View_I_Amazon_Sku_Asin_Category_Normal.amazon_category).where(View_I_Amazon_Sku_Asin_Category_Normal.amazon_category != None).paginate(1, self.pageSize)


            #print(rows)
            if (_where != ''): rows = eval('rows.where({0})'.format(_where))



            self.twProductAsinAmazonCategoryList.setRowCount(0)

            _rowCount = len(rows)

            self.lbPagerInfo.setText(' R:{0}'.format(_rowCount))
            rowIndex = 0
            if (_rowCount > 0):
                for i in range(_rowCount):
                    #   去掉第一行
                    self.twProductAsinAmazonCategoryList.removeRow(_rowCount - i - 1)
                # logger.info('加载了 %s 条, 每页 %s 条' %(_rowCount, self.pageSize))
                self.twProductAsinAmazonCategoryList.setRowCount(_rowCount)

                nowTime = datetime.datetime.now()
                self.mainWin.progressBarShow(_rowCount)
                self.mainWin.statusMsg('开始加载 {0}...'.format(nowTime.strftime('%H:%M:%S')))

                for i in range(_rowCount):
                    # 获取关系表数据
                    row = View_I_Amazon_Sku_Asin_Category_Normal(**(rows[i].__data__))

                    self.mainWin.progressBarContinue()

                    item = utQTableWidgetItem(rowIndex)

                    self.twProductAsinAmazonCategoryList.setItem(rowIndex, 0, item)
                    self.twProductAsinAmazonCategoryList.setItem(rowIndex, 1, utQTableWidgetItem(row.sku))
                    self.twProductAsinAmazonCategoryList.setItem(rowIndex, 2, utQTableWidgetItem(row.amazon_category))
                    rowIndex = rowIndex + 1
                    #break

                endTime = datetime.datetime.now()
                self.mainWin.statusMsg('加载 {0}条数据，用时{1}'.format(_rowCount, (endTime - nowTime)))
                self.mainWin.progressBarHide()
                logger.info('加载了 %s 条, 每页 %s 条' % (rowIndex, self.pageSize))
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)
            logger.info(e)
        pass

    def actTbRefreshClicked(self):
        self.initData()
        pass

    '''报表列表全选'''

    def actTbSelectionClicked(self):
        self.twProductAsinAmazonCategoryList.setFocus()
        selectedCount = self.twProductAsinAmazonCategoryList.rowCount()
        qtwsr = QTableWidgetSelectionRange(0, 0, selectedCount - 1,
                                           self.twProductAsinAmazonCategoryList.columnCount() - 1)
        self.twProductAsinAmazonCategoryList.setRangeSelected(qtwsr, True)
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''报表列表取消选择'''

    def actTbUnselectionClicked(self):
        self.twProductAsinAmazonCategoryList.setFocus()
        selectedCount = self.twProductAsinAmazonCategoryList.rowCount()
        qtwsr = QTableWidgetSelectionRange(0, 0, selectedCount - 1,
                                           self.twProductAsinAmazonCategoryList.columnCount() - 1)
        self.twProductAsinAmazonCategoryList.setRangeSelected(qtwsr, False)
        self.mainWin.statusMsg('您选中了{0}行'.format(0))

    '''报表列表反选'''

    def actTbInvertSelectionClicked(self):
        self.twProductAsinAmazonCategoryList.setFocus()
        row_num = self.twProductAsinAmazonCategoryList.rowCount()
        column_num = self.twProductAsinAmazonCategoryList.columnCount() - 1
        selectedCount = 0
        if (row_num > 0):
            listRows = set(self.getTwProductListSelectionChangedRowsNum())
            for i in range(row_num):
                qtwsr = QTableWidgetSelectionRange(i, 0, i, column_num)
                if (i in listRows):
                    self.twProductAsinAmazonCategoryList.setRangeSelected(qtwsr, False)
                else:
                    self.twProductAsinAmazonCategoryList.setRangeSelected(qtwsr, True)
                    selectedCount += 1
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''行选中时提示'''

    def actTwProductListSelectionChanged(self):
        row = self.getTwProductListSelectionChangedRowsNum()
        self.mainWin.statusMsg('您选中了{0}行'.format(row.__len__()))
        pass

    def actTwProductListHorSectionClicked(self, index):
        print(index)
        pass

    '''打开高级搜索'''

    def actTbSearchClicked(self):
        if self.search_box is None:
            self.search_box = WidgetSearchField(self, self.searchObj)
            self.vlProductAsinNewaimCategoryForm.insertWidget(1, self.search_box, 1)
            self.vlProductAsinNewaimCategoryForm.setStretch(2, 100)
        elif self.search_box.isHidden():
            self.search_box.setHidden(False)
            self.search_box.myWidget.close()
        else:
            self.search_box.setHidden(True)
        pass

    '''返回选中行'''

    def getTwProductListSelectionChangedRowsNum(self):
        result = []
        try:
            ranges = self.twProductAsinAmazonCategoryList.selectedRanges()
            for i in range(len(ranges)):
                for row in range(ranges[i].topRow(), ranges[i].bottomRow() + 1):
                    result.append(row)

        except Exception as e:
            print(e)

        # 去重返回
        return list(set(result))
        pass

    '''删除选择行'''

    def actTbDeleteClicked(self):
        rowIndex = self.getTwProductListSelectionChangedRowsNum()
        selectedCount = 0
        if rowIndex.__len__() > 0:
            if QMessageBox.information(None, '操作提示', '您确定要删除选中的记录吗？',
                                       QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                for i in rowIndex:
                    id = self.twProductAsinAmazonCategoryList.item(i, 0).text()
                    sku = self.twProductAsinAmazonCategoryList.item(i, 1).text()
                    category = self.twProductAsinAmazonCategoryList.item(i, 2).text()
                    skuRow = Na_Product_Asin.get(Na_Product_Asin.sku == sku)
                    catRow = Amazon_Product_Category.get(Amazon_Product_Category.title == category)
                    # 将Status设置为3（删除）
                    # Amazon_Product_Category.update(status=3).where(Amazon_Product_Category.id == id).execute()
                    # 删除与SKU关系表下的记录
                    try:
                        row = Na_Product_Asin_Amazon_Category.select().where(Na_Product_Asin_Amazon_Category.productasinmodel_id == skuRow.id and Na_Product_Asin_Amazon_Category.amazonproductcategorymodel_id == catRow.id).get()
                        row.delete_instance()
                    except Na_Product_Asin_Amazon_Category.DoesNotExist:
                        print('Categories are not associated with SKU')

                    selectedCount += 1
                self.actTbRefreshClicked()
            self.mainWin.statusMsg('您删除了{0}行'.format(selectedCount))
        else:
            QMessageBox.information(None, '操作提示', '请先选择要删除的记录', QMessageBox.Yes)
            pass

    '''导入SKU和Categeroy的关系表'''

    def actTbInputSkuAndCategoryClicked(self):
        dlg = QMessageBox.question(None, "操作提示", "您“确定”从CSV导入数据吗?", QMessageBox.Yes | QMessageBox.No)
        if (dlg == QMessageBox.Yes):
            file, ok1 = QFileDialog.getOpenFileName(None, "请选择CSV文件打开", "", "Csv File (*.csv)")
            if (file.__len__() > 0):
                # 读取文件总行数
                try:
                    tempfile = open(file, "r", encoding='utf-8')
                    importLines = len(tempfile.readlines()) - 1
                    tempfile.close()

                    nowTime = datetime.datetime.now()
                    self.mainWin.progressBarShow(importLines)
                    self.mainWin.statusMsg('开始导入 {0}...'.format(nowTime.strftime('%H:%M:%S')))

                    # 读取csv文件方式
                    csvFile = open(file, "r", encoding='utf-8')
                    reader = csv.reader(csvFile)  # 返回的是迭代类型

                    i = 0
                    for row in reader:
                        if (i > 0):
                            # 根据NodeID查询对应分类表ID
                            nodeId = row[1]
                            sku = row[0]

                            try:
                                categoryRow = Amazon_Product_Category.select().where(
                                    Amazon_Product_Category.code == nodeId).get()
                                categoryId = categoryRow.id
                            except Amazon_Product_Category.DoesNotExist:
                                categoryId = 0
                            try:
                                skuRow = Na_Product_Asin.select().where(Na_Product_Asin.sku == sku).get()
                                skuId = skuRow.id
                            except Na_Product_Asin.DoesNotExist:
                                skuId = 0

                            print(categoryId)
                            print(skuId)
                            # return
                            try:
                                if int(categoryId) > 0 and int(skuId) > 0:
                                    # 掺入到NA PRODUCT ASIN CATEGORY表中
                                    View_I_Amazon_Sku_Asin_Category.insert(
                                        productasinmodel_id=skuId,
                                        amazonproductcategorymodel_id=categoryId,
                                    ).execute()
                            except Exception as e:
                                import traceback
                                traceback.print_exc()
                                logger.info(e)
                        i = i + 1
                        self.mainWin.progressBarContinue()
                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    logger.info(e)

        self.actTbRefreshClicked()

    pass

