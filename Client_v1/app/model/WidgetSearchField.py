# coding:utf-8

import os, csv, datetime, re

from PyQt5.QtCore import QCoreApplication, QDateTime
from PyQt5.QtWidgets import QWidget

from app.lib.UtilCommon import logger, utQTableWidgetItem
from app.view.widgetSearchField import Ui_SearchFieldForm


class WidgetSearchField(QWidget, Ui_SearchFieldForm):
    _ = QCoreApplication.translate

    def __init__(self, mainWin, searchObj, comboObj = None):
        super(WidgetSearchField, self).__init__()
        self.mainWin = mainWin
        self.myWidget = QWidget()
        self.setupUi(self.myWidget)

        self.searchObj = searchObj if searchObj is not None else None
        if comboObj is not None :
            self.comboObj = list(comboObj.values())
            self.comboValue.addItems(self.comboObj)


        self.cbField.currentIndexChanged.connect(self.actCbFieldTextChanged)
        self.tbAdd.clicked.connect(self.actTbAddClicked)
        self.tbSub.clicked.connect(self.actTbSubClicked)
        self.tbUpdate.clicked.connect(self.actTbUpdateClicked)
        self.tbSearch.clicked.connect(self.actTbSearchClicked)

        self.twOperators.cellClicked.connect(self.actTwOperatorsClicked)

        self.initData()
        self.initLayout()

        self.setLayout(self.myWidget.layout())

    def initLayout(self):
        self.twOperators.setColumnWidth(0, 50)
        self.twOperators.setColumnWidth(1, 180)
        self.twOperators.setColumnWidth(2, 80)
        self.twOperators.setColumnWidth(3, 150)
        self.twOperators.setColumnWidth(4, 60)
        self.twOperators.setColumnHidden(0, True)

    def initData(self):
        try:
            if (len(self.searchObj['fields'])):
                for field in self.searchObj['fields']:
                    self.cbField.addItem(field['label'])
        except Exception as e:
            logger.info(e)
        pass

    '''字段选择'''
    def actCbFieldTextChanged(self, index):
        try:
            if (len(self.searchObj['fields'])):
                for field in self.searchObj['fields']:
                    if(field['label'] == self.cbField.currentText()) :
                        self.showValueByType(field['type'])
                        break
        except Exception as e:
            logger.info(e)

    def actTbAddClicked(self):
        rows = self.twOperators.rowCount()
        if rows>0:
            pass
        new_row = rows
        self.twOperators.setRowCount(new_row+1)
        self.twOperators.setItem(new_row, 1, utQTableWidgetItem(self.cbField.currentText()))
        self.twOperators.setItem(new_row, 2, utQTableWidgetItem(self.cbOperator.currentText()))
        for field in self.searchObj['fields']:
            if (field['label'] == self.cbField.currentText()):
                self.twOperators.setItem(new_row, 0, utQTableWidgetItem(field['name']))
                self.twOperators.setItem(new_row, 5, utQTableWidgetItem(field['type']))
                self.twOperators.setItem(new_row, 3, utQTableWidgetItem(self.getValueByType(field['type'])))

        self.twOperators.setItem(new_row, 4, utQTableWidgetItem(self.cbUnion.currentText()))

        pass

    def actTbSubClicked(self):
        row_num = -1
        for i in self.twOperators.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num>-1: self.twOperators.removeRow(row_num)
        pass

    def actTbUpdateClicked(self):
        row_num = -1
        for i in self.twOperators.selectionModel().selection().indexes():
            row_num = i.row()

        if row_num > -1:
            self.twOperators.setItem(row_num, 1, utQTableWidgetItem(self.cbField.currentText()))
            self.twOperators.setItem(row_num, 2, utQTableWidgetItem(self.cbOperator.currentText()))
            for field in self.searchObj['fields']:
                if (field['label'] == self.cbField.currentText()):
                    self.twOperators.setItem(row_num, 0, utQTableWidgetItem(field['name']))
                    self.twOperators.setItem(row_num, 5, utQTableWidgetItem(field['type']))
                    self.twOperators.setItem(row_num, 3, utQTableWidgetItem(self.getValueByType(field['type'])))
            self.twOperators.setItem(row_num, 4, utQTableWidgetItem(self.cbUnion.currentText()))

    def actTbSearchClicked(self):
        # 拼装查询参数
        num = self.twOperators.rowCount()
        try:
            try:
                method = self.searchObj['method'] if self.searchObj['method'] is not None else None
            except Exception as e:
                method = None

            if( num > 0):
                params = []
                for i in range(num):
                    params.append(
                        [self.twOperators.item(i,0).text(), self.twOperators.item(i,2).text(), self.twOperators.item(i,3).text(), self.twOperators.item(i,4).text(), self.twOperators.item(i,5).text()]
                    )

                self.mainWin.goSearch(conditions=params, method=method)
        except Exception as e:
            import traceback
            traceback.print_exc()
            logger.info(e)
        pass

    def actTwOperatorsClicked(self, row, col):
        self.cbField.setCurrentText(self.twOperators.item(row, 1).text())
        self.cbOperator.setCurrentText(self.twOperators.item(row, 2).text())
        for field in self.searchObj['fields']:
            if (field['label'] == self.twOperators.item(row, 1).text()):
                self.setValueByType(field['type'], self.twOperators.item(row, 3).text())
        self.cbUnion.setCurrentText(self.twOperators.item(row, 4).text())
        pass

    '''根据值类型显示内容'''
    def showValueByType(self, type):
        try:
            self.leValue.setHidden(True)
            self.floatValue.setHidden(True)
            self.intValue.setHidden(True)
            self.dteValue.setHidden(True)
            self.comboValue.setHidden(True)
            if(type == 'date'): self.dteValue.setHidden(False)
            elif(type == 'int'): self.intValue.setHidden(False)
            elif(type == 'float'): self.floatValue.setHidden(False)
            elif(type == 'combo'): self.comboValue.setHidden(False)
            else: self.leValue.setHidden(False)
        except Exception as e:
            logger.info(e)


    '''根据值类型获取值内容'''
    def getValueByType(self, type):
        try:
            if(type == 'date'): return self.dteValue.text()
            elif(type == 'int'): return self.intValue.text()
            elif(type == 'float'): return self.floatValue.text()
            elif(type == 'combo'): return self.comboValue.currentText()
            else: return self.leValue.text()
        except Exception as e:
            logger.info(e)

    '''根据值类型获取值内容'''
    def setValueByType(self, type, value):
        try:
            # self.showValueByType(type)
            # self.dateTimeEdit.setDateTime(QDateTime.fromString(now_time, 'yyyy-MM-dd hh:mm:ss'))
            if(type == 'date'): self.dteValue.setDateTime(QDateTime.fromString(value, 'yyyy-MM-dd hh:mm:ss'))
            elif(type == 'int'): self.intValue.setValue(int(value))
            elif(type == 'float'): self.floatValue.setValue(float(value))
            elif(type == 'combo'): self.comboValue.setCurrentText(self.comboObj[1])
            else: self.leValue.setText(value)
        except Exception as e:
            logger.info(e)