# coding:utf-8

import os, csv, datetime, re
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu, QTableWidgetItem, QFileDialog, QTableWidgetSelectionRange

from app.lib.UtilCommon import utQTableWidgetItem, getTime, logger, utStr2Float, utStr2Int, utGetStyleContent
from app.lib.UtilDb import QueryBuildToStr
from app.model.WidgetSearchField import WidgetSearchField
from app.model.dao.DbProductAsin import Na_Product_Asin
from app.view.formProduct import Ui_ProductForm


class WidgetProduct(QWidget, Ui_ProductForm):
    _ = QCoreApplication.translate

    # todo 转数据字典
    # CHOICES_COMBINE_TYPE = ((0, _('Single SKU')),
    #                         (1, _('Combo SKU')),
    #                         (2, _('Variation SKU')),
    #                         (3, _('FBA SKU')),
    #                         (4, _('Parent SKU')),)
    CHOICES_COMBINE_TYPE = {
        1: 'Single SKU',
        2: 'Combo SKU',
        3: 'Variation SKU',
        4: 'FBA SKU',
        5: 'Parent SKU',
    }

    def __init__(self, mainWin):
        super(WidgetProduct, self).__init__()
        self.mainWin = mainWin
        self.myWidget = QWidget()
        self.setupUi(self.myWidget)
        self.canMoveView = False
        # 搜索窗口
        self.search_box = None
        self.searchObj = {
            "fields": [
                {'name': 'sku', 'label': 'SKU', 'type': 'string'}
                ,{ 'name': 'asin', 'label': 'ASIN', 'type': 'string'}
                ,{ 'name': 'updated_at', 'label': 'Updated At', 'type': 'date'}
                ,{ 'name': 'combine_type', 'label': 'Combine Type', 'type': 'combo'}
            ],
        }

        self.pageSize = 10000

        self.tbInputCsv.clicked.connect(self.actTbInputCsvClicked)
        self.tbRefresh.clicked.connect(self.actTbRefreshClicked)

        self.tbSelection.clicked.connect(self.actTbSelectionClicked)
        self.tbUnselection.clicked.connect(self.actTbUnselectionClicked)
        self.tbInvertSelection.clicked.connect(self.actTbInvertSelectionClicked)
        self.tbDelete.clicked.connect(self.actTbDeleteClicked)

        self.twProductList.itemSelectionChanged.connect(self.actTwProductListSelectionChanged)
        self.twProductList.horizontalHeader().sectionClicked.connect(self.actTwProductListHorSectionClicked)
        self.tbSearch.clicked.connect(self.actTbSearchClicked)

        # 初始化布局
        self.initLayout()
        self.initData()
        self.setLayout(self.myWidget.layout())



    def initLayout(self):
        self.twProductList.setColumnWidth(0,80)
        self.twProductList.setColumnWidth(1,260)
        self.twProductList.setColumnWidth(2,150)
        self.twProductList.setColumnWidth(3,140)
        self.twProductList.setColumnWidth(4,140)
        self.twProductList.setColumnHidden(0, True)
        pass

    '''高级搜索数据'''
    def goSearch(self, conditions, method=None):
        _table_ent = 'Na_Product_Asin'

        for condition in  conditions:
            if condition[-1] == 'combo':
                for  index in  self.CHOICES_COMBINE_TYPE:
                    if  self.CHOICES_COMBINE_TYPE[index] == condition[2]:
                        condition[2] = index
                        print(self.CHOICES_COMBINE_TYPE[index])

        _where = QueryBuildToStr(_table_ent, conditions)
        self.initData(_where)
        pass

    def initData(self, _where = ''):
        try:
            # 初始加载第一页最新数据
            rows = Na_Product_Asin.select().paginate(1, self.pageSize)
            if(_where != ''): rows = eval('rows.where({0})'.format(_where))

            self.twProductList.setRowCount(0)

            _rowCount = len(rows)
            self.lbPagerInfo.setText(' R:{0}'.format(_rowCount))
            nowTime = datetime.datetime.now()
            self.mainWin.progressBarShow(_rowCount)
            self.mainWin.statusMsg('开始加载 {0}...'.format(nowTime.strftime('%H:%M:%S')))
            if (_rowCount > 0):
                # logger.info('加载了 %s 条, 每页 %s 条' %(_rowCount, self.pageSize))
                self.twProductList.setRowCount(_rowCount)
                for i in range(_rowCount):
                    row = Na_Product_Asin(**(rows[i].__data__))
                    self.mainWin.progressBarContinue()

                    item = utQTableWidgetItem(row.id)
                    # item.setCheckState(Qt.Unchecked)
                    self.twProductList.setItem(i, 0, item)
                    self.twProductList.setItem(i, 1, utQTableWidgetItem(row.sku))
                    self.twProductList.setItem(i, 2, utQTableWidgetItem(row.asin))
                    self.twProductList.setItem(i, 3, utQTableWidgetItem(self.CHOICES_COMBINE_TYPE[row.combine_type]))
                    self.twProductList.setItem(i, 4, utQTableWidgetItem(row.updated_at))
                    self.twProductList.setItem(i, 5, utQTableWidgetItem(row.created_at))

                endTime = datetime.datetime.now()
                self.mainWin.statusMsg('加载 {0}条数据，用时{1}'.format(_rowCount, (endTime - nowTime)))
                self.mainWin.progressBarHide()
                logger.info('加载了 %s 条, 每页 %s 条' % (i, self.pageSize))
        except Exception as e:
            logger.info(e)
        pass

    def actTbRefreshClicked(self):
        self.initData()
        pass

    '''导入功能'''
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

                    i = 0
                    for row in reader:
                        if (i > 0):
                            self.actTbSve(row)
                            # Na_Product_Asin.create(
                            #     sku = row[0]
                            #     ,asin = row[1]
                            # )
                        i = i + 1
                        self.mainWin.progressBarContinue()

                    csvFile.close()

                    endTime = datetime.datetime.now()
                    self.mainWin.statusMsg('完成导出 {0}条数据，用时{1}'.format(importLines, (endTime - nowTime)))
                    self.mainWin.progressBarHide()
                    self.actTbRefreshClicked()

                except Exception as e:
                    logger.info(e)
        pass

    '''报表列表全选'''
    def actTbSelectionClicked(self):
        self.twProductList.setFocus()
        selectedCount = self.twProductList.rowCount()
        qtwsr = QTableWidgetSelectionRange(0,0,selectedCount-1, self.twProductList.columnCount()-1)
        self.twProductList.setRangeSelected(qtwsr, True)
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''报表列表取消选择'''
    def actTbUnselectionClicked(self):
        self.twProductList.setFocus()
        selectedCount = self.twProductList.rowCount()
        qtwsr = QTableWidgetSelectionRange(0, 0, selectedCount-1, self.twProductList.columnCount()-1)
        self.twProductList.setRangeSelected(qtwsr, False)
        self.mainWin.statusMsg('您选中了{0}行'.format(0))

    '''报表列表反选'''
    def actTbInvertSelectionClicked(self):
        self.twProductList.setFocus()
        row_num = self.twProductList.rowCount()
        column_num = self.twProductList.columnCount()-1
        selectedCount = 0
        if (row_num > 0):
            listRows = set(self.getTwProductListSelectionChangedRowsNum())
            for i in range(row_num):
                qtwsr = QTableWidgetSelectionRange(i, 0, i, column_num)
                if(i in listRows):
                    self.twProductList.setRangeSelected(qtwsr, False)
                else:
                    self.twProductList.setRangeSelected(qtwsr, True)
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
        if self.search_box is None :
            self.search_box = WidgetSearchField(self, self.searchObj, self.CHOICES_COMBINE_TYPE)
            self.vlProductForm.insertWidget(1, self.search_box, 1)
            self.vlProductForm.setStretch(2, 100)
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
            ranges = self.twProductList.selectedRanges()
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
        rowIndex = self.getTwProductListSelectionChangedRowsNum()
        selectedCount = 0
        if rowIndex.__len__()>0:
            if QMessageBox.information(None, '操作提示', '您确定要删除选中的记录吗？', QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes :
                for i in rowIndex:
                    id = self.twProductList.item(i, 0).text()
                    Na_Product_Asin.delete_by_id(id)
                    selectedCount += 1

                self.actTbRefreshClicked()
            self.mainWin.statusMsg('您删除了{0}行'.format(selectedCount))
        else:
            QMessageBox.information(None, '操作提示', '请先选择要删除的记录', QMessageBox.Yes)
            pass

    '''保存到数据库'''
    def actTbSve(self, row):
        nowTime = datetime.datetime.now()
        cur_time = getTime()
        print(row[0])
        selectResult = Na_Product_Asin.select().where(Na_Product_Asin.sku == row[0]).execute()
        if  len(selectResult) > 0:
            result = Na_Product_Asin.update({Na_Product_Asin.updated_at: cur_time}).where(Na_Product_Asin.sku == row[0]).execute()
        else :
            try:
                result = (Na_Product_Asin.insert(
                    sku = row[0],
                    asin = row[1],
                    platform= 'amazon',
                    platform_id=1,
                    sort=0,
                ).execute())
            except Exception as e:
                import traceback
                traceback.print_exc()
                print(e)

    pass

