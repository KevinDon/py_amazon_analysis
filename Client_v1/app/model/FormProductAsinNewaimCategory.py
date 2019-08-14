# @Time : 2019/7/19 14:58 
# @Author : Kevin
# @File : FormProductAsinNewaimCategory.py 
# @Software: PyCharm
# coding:utf-8

import os, csv, datetime, re, time, xlrd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu, QTableWidgetItem, QFileDialog, QTableWidgetSelectionRange
from app.lib.db import pgDbClection
from app.lib.UtilCommon import getTime, utQTableWidgetItem, logger, utStr2Float, utStr2Int, utGetStyleContent
from app.lib.UtilDb import QueryBuildToStr
from app.model.WidgetSearchField import WidgetSearchField

'''导入对应的表'''
from app.model.dao.DbProductAsin import Na_Product_Asin
from app.model.dao.DbProductCategory import Pub_Product_Category
from app.model.dao.DbProductAsinCategory import Pub_Product_Asin_Category_Relation
from app.model.dao.ViewSkuAsinCategory import View_I_Amazon_Sku_Asin_Category
from app.model.dao.VIewSkuAsinCategoryNormal import View_I_Amazon_Sku_Asin_Category_Normal
from app.model.vo.MdUser import User
from app.view.formProductAsinNewaimCategory import Ui_ProductAsinNewaimCategoryForm


class WidgetProductNewaimCategory(QWidget, Ui_ProductAsinNewaimCategoryForm):

    def __init__(self, mainWin):
        super(WidgetProductNewaimCategory, self).__init__()
        self.mainWin = mainWin
        self.myWidget = QWidget()
        self.setupUi(self.myWidget)
        self.canMoveView = False
        # 搜索窗口
        self.search_box = None
        self.searchObj = {
            "fields": [
                {'name': 'sku', 'label': 'SKU', 'type': 'string'}
                ,{'name': 'category', 'label': 'Category', 'type': 'string'}
            ],
        }

        self.pageSize = 10000

        self.tbInputCsv.clicked.connect(self.actTbInputSkuAndCategoryClicked)
        self.tbRefresh.clicked.connect(self.actTbRefreshClicked)

        # 隐藏导入SKU与分类关系按钮
        #self.pushButton.clicked.connect(self.actTbInputSkuAndCategoryClicked)
        self.pushButton.setHidden(True)

        #self.tbActionLog.clicked.connect(self.actTbCatLog)
        self.tbActionLog.setHidden(True)

        self.tbSelection.clicked.connect(self.actTbSelectionClicked)
        self.tbUnselection.clicked.connect(self.actTbUnselectionClicked)
        self.tbInvertSelection.clicked.connect(self.actTbInvertSelectionClicked)
        self.tbDelete.clicked.connect(self.actTbDeleteClicked)

        self.tbDelete.setHidden(True)
        self.tbInputCsv.setHidden(True)

        self.twProductAsinNewaimCategoryList.itemSelectionChanged.connect(self.actTwProductListSelectionChanged)
        # self.twProductAsinNewaimCategoryList.horizontalHeader().sectionClicked.connect(self.actTwProductListHorSectionClicked)
        self.tbSearch.clicked.connect(self.actTbSearchClicked)

        # 初始化布局
        self.initLayout()
        self.initData()
        self.setLayout(self.myWidget.layout())

    def initLayout(self):
        self.twProductAsinNewaimCategoryList.setColumnHidden(0, True),
        self.twProductAsinNewaimCategoryList.setColumnWidth(1, 250)
        self.twProductAsinNewaimCategoryList.setColumnWidth(2, 260)
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
            rows = View_I_Amazon_Sku_Asin_Category_Normal.select(View_I_Amazon_Sku_Asin_Category_Normal.sku,View_I_Amazon_Sku_Asin_Category_Normal.category).where(View_I_Amazon_Sku_Asin_Category_Normal.category != None).paginate(1, self.pageSize)

            # print(rows)
            if (_where != ''): rows = eval('rows.where({0})'.format(_where))

            # print(productRows)
            self.twProductAsinNewaimCategoryList.setRowCount(0)

            _rowCount = len(rows)
            self.lbPagerInfo.setText(' R:{0}'.format(_rowCount))

            nowTime = datetime.datetime.now()
            self.mainWin.progressBarShow(_rowCount)
            self.mainWin.statusMsg('开始加载 {0}...'.format(nowTime.strftime('%H:%M:%S')))

            if (_rowCount > 0):
                for i in range(_rowCount):
                    #   去掉第一行
                    self.twProductAsinNewaimCategoryList.removeRow(_rowCount - i - 1)

                self.twProductAsinNewaimCategoryList.setRowCount(_rowCount)
                rowIndex = 0
                for i in range(_rowCount):
                    # 获取关系表数据
                    row = View_I_Amazon_Sku_Asin_Category_Normal(**(rows[i].__data__))


                    self.mainWin.progressBarContinue()
                    item = utQTableWidgetItem(rowIndex)
                    # item.setCheckState(Qt.Unchecked)
                    # print(skuData.sku)
                    self.twProductAsinNewaimCategoryList.setItem(rowIndex, 0, item)
                    self.twProductAsinNewaimCategoryList.setItem(rowIndex, 1, utQTableWidgetItem(row.sku))
                    self.twProductAsinNewaimCategoryList.setItem(rowIndex, 2, utQTableWidgetItem(row.category))
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
        self.twProductAsinNewaimCategoryList.setFocus()
        selectedCount = self.twProductAsinNewaimCategoryList.rowCount()
        qtwsr = QTableWidgetSelectionRange(0, 0, selectedCount - 1, self.twProductAsinNewaimCategoryList.columnCount() - 1)
        self.twProductAsinNewaimCategoryList.setRangeSelected(qtwsr, True)
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''报表列表取消选择'''
    def actTbUnselectionClicked(self):
        self.twProductAsinNewaimCategoryList.setFocus()
        selectedCount = self.twProductAsinNewaimCategoryList.rowCount()
        qtwsr = QTableWidgetSelectionRange(0, 0, selectedCount - 1, self.twProductAsinNewaimCategoryList.columnCount() - 1)
        self.twProductAsinNewaimCategoryList.setRangeSelected(qtwsr, False)
        self.mainWin.statusMsg('您选中了{0}行'.format(0))

    '''报表列表反选'''
    def actTbInvertSelectionClicked(self):
        self.twProductAsinNewaimCategoryList.setFocus()
        row_num = self.twProductAsinNewaimCategoryList.rowCount()
        column_num = self.twProductAsinNewaimCategoryList.columnCount() - 1
        selectedCount = 0
        if (row_num > 0):
            listRows = set(self.getTwProductListSelectionChangedRowsNum())
            for i in range(row_num):
                qtwsr = QTableWidgetSelectionRange(i, 0, i, column_num)
                if (i in listRows):
                    self.twProductAsinNewaimCategoryList.setRangeSelected(qtwsr, False)
                else:
                    self.twProductAsinNewaimCategoryList.setRangeSelected(qtwsr, True)
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
            ranges = self.twProductAsinNewaimCategoryList.selectedRanges()
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
                    id = self.twProductAsinNewaimCategoryList.item(i, 0).text()

                    # 将Status设置为3（删除）
                    Pub_Product_Category.update(status=3).where(Pub_Product_Category.id == id).execute()

                    # 删除与SKU关系表下的记录
                    try:
                        row = Pub_Product_Asin_Category_Relation.get(Pub_Product_Asin_Category_Relation.category_id == id)
                        row.delete_instance()
                    except Pub_Product_Asin_Category_Relation.DoesNotExist:
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
                            # 根据分类名查询对应分类表ID
                            nodeId = row[2]
                            sku =  row[0]

                            try:
                                categoryRow = Pub_Product_Category.select().where(
                                    Pub_Product_Category.title == nodeId).get()
                                categoryId = categoryRow.id
                            except Pub_Product_Category.DoesNotExist:
                                categoryId = 0
                            try:
                                skuRow = Na_Product_Asin.select().where(Na_Product_Asin.sku == sku).get()
                                skuId = skuRow.id
                            except Na_Product_Asin.DoesNotExist:
                                skuId = 0
                            #
                            # print(categoryId)
                            # print(skuId)
                            # return
                            try:
                                if int(categoryId) > 0 and int(skuId) > 0:
                                    # 掺入到NA PRODUCT ASIN CATEGORY表中
                                    Pub_Product_Asin_Category_Relation.insert(
                                        product_id=skuId,
                                        category_id=categoryId,
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

