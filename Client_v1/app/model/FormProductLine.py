# @Time : 2019/7/16 13:55 
# @Author : Kevin
# @File : FormProductLine.py 
# @Software: PyCharm

# coding:utf-8
import os, csv, datetime, re, xlrd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu, QTableWidgetItem, QFileDialog, QTableWidgetSelectionRange

from app.lib.UtilCommon import getTime, utQTableWidgetItem, logger, utStr2Float, utStr2Int, utGetStyleContent
from app.lib.UtilDb import QueryBuildToStr
from app.model.WidgetSearchField import WidgetSearchField
from app.model.dao.DbProductLine import Na_Product_Line
from app.view.formProductLine import Ui_ProductLineForm


class WidgetProductLine(QWidget, Ui_ProductLineForm):
    _ = QCoreApplication.translate

    def __init__(self, mainWin):
        super(WidgetProductLine, self).__init__()
        self.mainWin = mainWin
        self.myWidget = QWidget()
        self.setupUi(self.myWidget)
        self.canMoveView = False
        # 搜索窗口
        self.search_box = None
        self.searchObj = {
            "fields": [
                {'name': 'code', 'label': 'Code', 'type': 'string'}
                ,{'name': 'title', 'label': 'Title', 'type': 'string'}
                ,{ 'name': 'updated_at', 'label': 'Updated At', 'type': 'date'}
                ,{ 'name': 'created_at', 'label': 'Created At', 'type': 'date'}
            ],
        }

        self.pageSize = 10000

        self.tbRefresh.clicked.connect(self.actTbRefreshClicked)

        self.tbSelection.clicked.connect(self.actTbSelectionClicked)
        self.tbUnselection.clicked.connect(self.actTbUnselectionClicked)

        self.tbInvertSelection.clicked.connect(self.actTbInvertSelectionClicked)

        self.twProductLine.itemSelectionChanged.connect(self.acttwProductLineSelectionChanged)
        self.twProductLine.horizontalHeader().sectionClicked.connect(self.acttwProductLineHorSectionClicked)
        self.tbSearch.clicked.connect(self.actTbSearchClicked)

        # 初始化布局
        self.initLayout()
        self.initData()
        self.setLayout(self.myWidget.layout())



    def initLayout(self):
        self.twProductLine.setColumnWidth(0,80)
        self.twProductLine.setColumnWidth(1,240)
        self.twProductLine.setColumnWidth(2,280)
        self.twProductLine.setColumnWidth(3,140)
        self.twProductLine.setColumnWidth(4,140)
        self.twProductLine.setColumnHidden(0, True)
        pass

    '''高级搜索数据'''
    def goSearch(self, conditions, method=None):
        _table_ent = 'Na_Product_Line'
        _where = QueryBuildToStr(_table_ent, conditions)
        self.initData(_where)
        pass

    def initData(self, _where = ''):
        try:
            # 初始加载第一页最新数据
            rows = Na_Product_Line.select().paginate(1, self.pageSize)
            if(_where != ''): rows = eval('rows.where({0})'.format(_where))

            self.twProductLine.setRowCount(0)

            _rowCount = len(rows)
            self.lbPagerInfo.setText(' R:{0}'.format(_rowCount))
            nowTime = datetime.datetime.now()
            self.mainWin.progressBarShow(_rowCount)
            self.mainWin.statusMsg('开始加载 {0}...'.format(nowTime.strftime('%H:%M:%S')))
            if (_rowCount > 0):
                # logger.info('加载了 %s 条, 每页 %s 条' %(_rowCount, self.pageSize))
                self.twProductLine.setRowCount(_rowCount)
                for i in range(_rowCount):
                    row = Na_Product_Line(**(rows[i].__data__))
                    self.mainWin.progressBarContinue()
                    item = utQTableWidgetItem(row.id)
                    # item.setCheckState(Qt.Unchecked)
                    self.twProductLine.setItem(i, 0, item)
                    self.twProductLine.setItem(i, 1, utQTableWidgetItem(row.code))
                    self.twProductLine.setItem(i, 2, utQTableWidgetItem(row.title))
                    self.twProductLine.setItem(i, 3, utQTableWidgetItem(row.updated_at))
                    self.twProductLine.setItem(i, 4, utQTableWidgetItem(row.created_at))

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


    '''报表列表全选'''
    def actTbSelectionClicked(self):
        self.twProductLine.setFocus()
        selectedCount = self.twProductLine.rowCount()
        qtwsr = QTableWidgetSelectionRange(0,0,selectedCount-1, self.twProductLine.columnCount()-1)
        self.twProductLine.setRangeSelected(qtwsr, True)
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''报表列表取消选择'''
    def actTbUnselectionClicked(self):
        self.twProductLine.setFocus()
        selectedCount = self.twProductLine.rowCount()
        qtwsr = QTableWidgetSelectionRange(0, 0, selectedCount-1, self.twProductLine.columnCount()-1)
        self.twProductLine.setRangeSelected(qtwsr, False)
        self.mainWin.statusMsg('您选中了{0}行'.format(0))

    '''报表列表反选'''
    def actTbInvertSelectionClicked(self):
        self.twProductLine.setFocus()
        row_num = self.twProductLine.rowCount()
        column_num = self.twProductLine.columnCount()-1
        selectedCount = 0
        if (row_num > 0):
            listRows = set(self.gettwProductLineSelectionChangedRowsNum())
            for i in range(row_num):
                qtwsr = QTableWidgetSelectionRange(i, 0, i, column_num)
                if(i in listRows):
                    self.twProductLine.setRangeSelected(qtwsr, False)
                else:
                    self.twProductLine.setRangeSelected(qtwsr, True)
                    selectedCount += 1
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''行选中时提示'''
    def acttwProductLineSelectionChanged(self):
        row = self.gettwProductLineSelectionChangedRowsNum()
        self.mainWin.statusMsg('您选中了{0}行'.format(row.__len__()))
        pass

    def acttwProductLineHorSectionClicked(self, index):
        print(index)
        pass

    '''打开高级搜索'''
    def actTbSearchClicked(self):
        if self.search_box is None :
            self.search_box = WidgetSearchField(self, self.searchObj)
            self.vlProductLineForm.insertWidget(1, self.search_box, 1)
            self.vlProductLineForm.setStretch(2, 100)
        elif self.search_box.isHidden():
            self.search_box.setHidden(False)
            self.search_box.myWidget.close()
        else:
            self.search_box.setHidden(True)
        pass

    '''返回选中行'''
    def gettwProductLineSelectionChangedRowsNum(self):
        result = []
        try:
            ranges = self.twProductLine.selectedRanges()
            for i in range(len(ranges)):
                for row in range(ranges[i].topRow(), ranges[i].bottomRow()+1):
                    result.append(row)

        except Exception as e:
            print(e)

        # 去重返回
        return list(set(result))
        pass

