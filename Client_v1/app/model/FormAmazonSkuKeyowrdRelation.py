# @Time : 2019/7/20 12:27 
# @Author : Kevin
# @File : FormAmazonSkuKeyowrdRelation.py
# @Software: PyCharm
# coding:utf-8
import os, csv, datetime, re
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu, QTableWidgetItem, QFileDialog, QTableWidgetSelectionRange

from app.lib.UtilCommon import getTime, utQTableWidgetItem, logger, utStr2Float, utStr2Int, utGetStyleContent
from app.lib.UtilDb import QueryBuildToStr
from app.lib.db import pgDbClection
from app.model.WidgetSearchField import WidgetSearchField
from app.model.dao.DbSkuKeyword import Pub_Sku_Keyword
from app.model.dao.DbProductAsin import  Na_Product_Asin
from app.model.dao.DbPorductAsinKeywordRelation import Pub_Product_Asin_Keyword_Relation
from app.view.formAmazonSkuKeywordRelation import Ui_AmazonSkuKeywordRelationForm


class WidgetAmazonSkuKeywordRelation(QWidget, Ui_AmazonSkuKeywordRelationForm):
    _ = QCoreApplication.translate

    def __init__(self, mainWin):
        super(WidgetAmazonSkuKeywordRelation, self).__init__()
        self.mainWin = mainWin
        self.myWidget = QWidget()
        self.setupUi(self.myWidget)
        self.canMoveView = False
        # 搜索窗口
        self.search_box = None
        self.searchObj = {
            "fields": [
                {'name': 'sku', 'label': 'SKU', 'type': 'string'},
                {'name': 'title', 'label': 'Title', 'type': 'string'},
            ],
        }

        self.pageSize = 10000

        self.tbInputCsv.clicked.connect(self.actTbInputCsvClicked)
        self.tbRefresh.clicked.connect(self.actTbRefreshClicked)

        self.tbSelection.clicked.connect(self.actTbSelectionClicked)
        self.tbUnselection.clicked.connect(self.actTbUnselectionClicked)
        self.tbInvertSelection.clicked.connect(self.actTbInvertSelectionClicked)
        self.tbDelete.clicked.connect(self.actTbDeleteClicked)

        self.twAmazonSKuKeywordRelation.itemSelectionChanged.connect(self.acttwAmazonSKuKeywordRelationSelectionChanged)
        self.twAmazonSKuKeywordRelation.horizontalHeader().sectionClicked.connect(self.acttwAmazonSKuKeywordRelationHorSectionClicked)
        self.tbSearch.clicked.connect(self.actTbSearchClicked)

        # 初始化布局
        self.initLayout()
        self.initData()
        self.setLayout(self.myWidget.layout())



    def initLayout(self):
        self.twAmazonSKuKeywordRelation.setColumnWidth(0,80)
        self.twAmazonSKuKeywordRelation.setColumnWidth(1,150)
        self.twAmazonSKuKeywordRelation.setColumnWidth(2,150)
        self.twAmazonSKuKeywordRelation.setColumnWidth(3,140)
        self.twAmazonSKuKeywordRelation.setColumnHidden(0, True)
        pass

    '''高级搜索数据'''
    def goSearch(self, conditions, method=None):
        _product_table_ent = 'Na_Product_Asin'
        _keyword_table_ent = 'Pub_Sku_Keyword'
        _where = []
        print(conditions)
        if (len(conditions) > 0):
            for condition in conditions:
                if condition[0] == 'sku':
                    _productWhere = QueryBuildToStr(_product_table_ent, [condition])
                    _where.append(_productWhere)
                elif condition[0] == 'keyword':
                    _keywordWhere = QueryBuildToStr(_keyword_table_ent, [condition])
                    _where.append(_keywordWhere)
        print(_where)
        self.initData(_where)
        pass

    def initData(self, _where = ''):
        try:

            # 初始加载第一页最新数据，过滤Status为3的记录
            rows = Pub_Product_Asin_Keyword_Relation.select().paginate(1, self.pageSize)
            products = True
            keywords = True

            if (len(_where) > 0):
               # products = eval(_where[0])
                #categories = eval(_where(1).format(_where[1])) if len(_where) > 1 else categories
                products = eval(_where[0])
                keywords = eval(_where[1]) if len(_where) > 1 else keywords

            self.twAmazonSKuKeywordRelation.setRowCount(0)

            _rowCount = len(rows)
            nowTime = datetime.datetime.now()
            self.mainWin.progressBarShow(_rowCount)
            self.mainWin.statusMsg('开始加载 {0}...'.format(nowTime.strftime('%H:%M:%S')))
            self.lbPagerInfo.setText(' R:{0}'.format(_rowCount))
            if (_rowCount > 0):
                for i in range(_rowCount):
                    #   去掉第一行
                    self.twAmazonSKuKeywordRelation.removeRow(_rowCount - i - 1)

                #self.twAmazonSKuKeywordRelation.setRowCount(_rowCount)
                rowIndex = 0
                for i in range(_rowCount):
                    # 获取关系表数据
                    row = Pub_Product_Asin_Keyword_Relation(**(rows[i].__data__))

                    if  rows[i].__data__['product_id']  ==None or rows[i].__data__['keyword_id'] == None:
                        continue
                    self.twAmazonSKuKeywordRelation.setRowCount(rowIndex + 1)
                    #获取SKU
                    #skuData = (Na_Product_Asin.select(Pub_Product_Category.title, Na_Product_Asin.sku).join(Pub_Product_Category, on=(Pub_Product_Category.id==rows[i].__data__['category_id'])).where(Na_Product_Asin.id==rows[i].__data__['product_id']).get())
                    # sql = 'SELECT keyword.title, product.sku FROM Pub_Sku_Keyword keyword JOIN Na_Product_Asin product ON product.id = {} WHERE category.id={}'.format(rows[i].__data__['product_id'] , rows[i].__data__['keyword_id'])
                    #
                    # row = pgDbClection.Conn(self).execute_sql(sql).fetchall()

                    try:
                        skuData = Na_Product_Asin.select().where((Na_Product_Asin.id == rows[i].__data__['product_id']) , products).get()
                    except Na_Product_Asin.DoesNotExist:
                        continue

                    try:
                        keywordData = Pub_Sku_Keyword.select().where((Pub_Sku_Keyword.id == rows[i].__data__['keyword_id']) , keywords).get()
                    except Pub_Sku_Keyword.DoesNotExist:
                        continue



                    # print(skuData.sku)
                    self.mainWin.progressBarContinue()
                    item = utQTableWidgetItem(rowIndex)
                    # item.setCheckState(Qt.Unchecked)
                    self.twAmazonSKuKeywordRelation.setItem(rowIndex,0 ,item)
                    self.twAmazonSKuKeywordRelation.setItem(rowIndex, 1, utQTableWidgetItem(skuData.sku))
                    self.twAmazonSKuKeywordRelation.setItem(rowIndex, 2, utQTableWidgetItem(keywordData.title))
                    rowIndex = rowIndex + 1

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

    def actTbInputCsvClicked(self):
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
                    cur_time = getTime()
                    i = 0
                    for row in reader:
                        if (i > 0):
                            # 根据NodeID查询对应分类表ID
                            keyword = row[2]
                            sku = row[0]

                            try:
                                keywordRow = Pub_Sku_Keyword.select().where(Pub_Sku_Keyword.title == keyword).get()
                                keywordId = keywordRow.id
                            except Pub_Sku_Keyword.DoesNotExist:
                                keywordId = 0
                            try:
                                skuRow = Na_Product_Asin.select().where(Na_Product_Asin.sku == sku).get()
                                skuId = skuRow.id
                            except Na_Product_Asin.DoesNotExist:
                                skuId = 0

                            print(keywordId)
                            print(skuId)
                            # return
                            try:
                                if int(keywordId) > 0 and int(skuId) > 0:
                                    # 掺入到NA PRODUCT ASIN CATEGORY表中
                                    Pub_Product_Asin_Keyword_Relation.insert(
                                        product_id=skuId,
                                        keyword_id=keywordId,
                                        update_at=cur_time
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

    '''报表列表全选'''
    def actTbSelectionClicked(self):
        self.twAmazonSKuKeywordRelation.setFocus()
        selectedCount = self.twAmazonSKuKeywordRelation.rowCount()
        qtwsr = QTableWidgetSelectionRange(0,0,selectedCount-1, self.twAmazonSKuKeywordRelation.columnCount()-1)
        self.twAmazonSKuKeywordRelation.setRangeSelected(qtwsr, True)
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''报表列表取消选择'''
    def actTbUnselectionClicked(self):
        self.twAmazonSKuKeywordRelation.setFocus()
        selectedCount = self.twAmazonSKuKeywordRelation.rowCount()
        qtwsr = QTableWidgetSelectionRange(0, 0, selectedCount-1, self.twAmazonSKuKeywordRelation.columnCount()-1)
        self.twAmazonSKuKeywordRelation.setRangeSelected(qtwsr, False)
        self.mainWin.statusMsg('您选中了{0}行'.format(0))

    '''报表列表反选'''
    def actTbInvertSelectionClicked(self):
        self.twAmazonSKuKeywordRelation.setFocus()
        row_num = self.twAmazonSKuKeywordRelation.rowCount()
        column_num = self.twAmazonSKuKeywordRelation.columnCount()-1
        selectedCount = 0
        if (row_num > 0):
            listRows = set(self.gettwAmazonSKuKeywordRelationSelectionChangedRowsNum())
            for i in range(row_num):
                qtwsr = QTableWidgetSelectionRange(i, 0, i, column_num)
                if(i in listRows):
                    self.twAmazonSKuKeywordRelation.setRangeSelected(qtwsr, False)
                else:
                    self.twAmazonSKuKeywordRelation.setRangeSelected(qtwsr, True)
                    selectedCount += 1
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''行选中时提示'''
    def acttwAmazonSKuKeywordRelationSelectionChanged(self):
        row = self.gettwAmazonSKuKeywordRelationSelectionChangedRowsNum()
        self.mainWin.statusMsg('您选中了{0}行'.format(row.__len__()))
        pass

    def acttwAmazonSKuKeywordRelationHorSectionClicked(self, index):
        print(index)
        pass

    '''打开高级搜索'''
    def actTbSearchClicked(self):
        if self.search_box is None :
            self.search_box = WidgetSearchField(self, self.searchObj)
            self.vlAmazonSkuKeywordRelationForm.insertWidget(1, self.search_box, 1)
            self.vlAmazonSkuKeywordRelationForm.setStretch(2, 100)
        elif self.search_box.isHidden():
            self.search_box.setHidden(False)
            self.search_box.myWidget.close()
        else:
            self.search_box.setHidden(True)
        pass

    '''返回选中行'''
    def gettwAmazonSKuKeywordRelationSelectionChangedRowsNum(self):
        result = []
        try:
            ranges = self.twAmazonSKuKeywordRelation.selectedRanges()
            for i in range(len(ranges)):
                for row in range(ranges[i].topRow(), ranges[i].bottomRow()+1):
                    result.append(row)

        except Exception as e:
            print(e)

        # 去重返回
        return list(set(result))
        pass

    '''删除选择行'''
    def actTbDeleteClicked(self):
        rowIndex = self.gettwAmazonSKuKeywordRelationSelectionChangedRowsNum()
        selectedCount = 0
        if rowIndex.__len__()>0:
            if QMessageBox.information(None, '操作提示', '您确定要删除选中的记录吗？', QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes :
                for i in rowIndex:
                    id = self.twAmazonSKuKeywordRelation.item(i, 0).text()
                    Pub_Product_Asin_Keyword_Relation.delete_by_id(id)
                    selectedCount += 1

                self.actTbRefreshClicked()
            self.mainWin.statusMsg('您删除了{0}行'.format(selectedCount))
        else:
            QMessageBox.information(None, '操作提示', '请先选择要删除的记录', QMessageBox.Yes)
            pass
