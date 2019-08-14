# coding:utf-8
import time
import types
import os, sys
import win32api
from PyQt5 import QtWidgets, QtGui, QtCore

from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtWidgets import QTableWidgetItem, QTreeWidgetItem, QMessageBox, QMenu, QWidget, QHBoxLayout, QDialog

from app.lib.logger import Log
from app.model.DlgSettingWin import DlgSetting
from app.model.FormBusinessReport import WidgetBusinessReport
from app.model.FormProduct import WidgetProduct
from app.model.FormCategory import WidgetCategory
from app.model.FormNewaimCategory import WidgetNewaimCategory
from app.model.FormProductLine import WidgetProductLine
from app.model.FormSkuKeyword import WidgetSkuKeyword
from app.model.FormProductAsinNewaimCategory import WidgetProductNewaimCategory
from app.model.FormProductAsinAmazonCategory import WidgetProductAmazonCategory
from app.model.FormAmazonSkuKeyowrdRelation import  WidgetAmazonSkuKeywordRelation
from app.model.FormDashboard import  WidgetDashboard
from app.model.FormAmazonCategoryKeywordRelation import  WidgetAmazonCategoryKeywordRelation
from app.model.WidgetWeb import WidgetWeb
from app.model.dao.DbPlusin import DbPlusIn
from app.view.mainWindow import Ui_mainWindow

class WinMain(Ui_mainWindow):
    _ = QCoreApplication.translate

    def __init__(self, mainWindow):
        super(WinMain, self).__init__()
        self.setupUi(mainWindow)
        self.app = mainWindow
        self.log = Log('info')

        #系统菜单初始化
        self.actionSetting.triggered.connect(self.actSetting)
        self.actionAbout.triggered.connect(self.actAbout)
        self.actionHelp.triggered.connect(self.help)
        self.actionExit.triggered.connect(self.actExit)
        self.actionBusinessReport.triggered.connect(lambda: self.actLoadModelView('BUSINESS-REPORT'))
        self.actionProductList.triggered.connect(lambda: self.actLoadModelView('PRODUCT-LIST'))
        self.actionChartsBusinessReport.triggered.connect(lambda: self.actLoadModelView('CHARTS'))
        # self.actionCategories.triggered.connect(lambda: self.actLoadModelView('CATEGORY-LIST'))
        # self.actionProduct_Line.triggered.connect(lambda: self.actLoadModelView('PRODUCT-LINE'))
        # self.actionCategory_List.triggered.connect(lambda: self.actLoadModelView('NEWAIM-CATEGORY'))
        self.actionKeywords_List.triggered.connect(lambda: self.actLoadModelView('KEYWORD-LIST'))
        self.actionProduct_Category_Relation.triggered.connect(lambda: self.actLoadModelView('PRODUCT-CATEGORY'))
        self.actionProduct_And_Category_Relationship.triggered.connect(lambda: self.actLoadModelView('AMAZON-PRODUCT-CATEGORY'))
        self.actionAmazon_Category_Relation.triggered.connect(lambda: self.actLoadModelView('AMAZON-CATEGORY-KEYWORD'))
        self.actionDashboard.triggered.connect(lambda: self.actLoadModelView('DASHBOARD'))

        # 设置main tab 关闭功能
        self.mainTabs.setTabsClosable(True)
        self.mainTabs.tabCloseRequested.connect(self.actMainTabsClose)
        self.mainTabs.removeTab(0)

        self.plTab = WidgetDashboard(self)
        _wgTemp = self.plTab
        tabIndex = self.mainTabs.addTab(_wgTemp, _wgTemp.myWidget.windowTitle())
        self.mainTabs.setCurrentIndex(tabIndex)


    '''关于程序'''
    def actAbout(self):
        QMessageBox.information(None, self._("sscode", "About Program"),
            " NEWAIM Analysis for Amazon\n 主要功能：AMAZON 销售分析 \n 版本：V{0} \n 发布：2019-08-09".format(self.app.configs.version.value),
            QMessageBox.Yes)

    '''退出系统'''
    def actExit(self):
        self.app.closeMain()

    '''打开help'''
    def help(self):
        try:
            rootPath,rootFile = os.path.split(os.path.abspath(sys.argv[0]))
            rootPath = rootPath.replace("\\", "/")
            win32api.ShellExecute(0, 'open', rootPath + '/app/resource/help.chm', '', '', 1)
        except Exception as e:
            print(e)
        pass

    '''系统配置'''
    def actSetting(self):
        try:
            DlgSetting(self.app)
        except Exception as e:
            print(e)
        pass

    def actMainTabsClose(self, index):
        if(index>-1):
            self.mainTabs.removeTab(index)
        else:
            self.statusMsg('不允许关闭工作区—“{0}”'.format(self.mainTabs.tabText(index)))


    '''动态加载系统模块'''
    def actLoadModelView(self, code):
        tabIndex = -1
        try:
            mdPlusin = DbPlusIn().get(code=code)
            for i in range(self.mainTabs.count()):
                if (self.mainTabs.tabText(i) == mdPlusin.title_cn or self.mainTabs.tabText(i) == mdPlusin.title_en or self.mainTabs.tabText(i) == mdPlusin.code):
                    tabIndex = i
                    pass

            if (tabIndex == -1):
                if (code == 'BUSINESS-REPORT'):
                    self.brTab = WidgetBusinessReport(self)
                    _wgTemp = self.brTab
                elif (code == 'PRODUCT-LIST'):
                    self.plTab = WidgetProduct(self)
                    _wgTemp = self.plTab
                elif (code == 'CHARTS'):
                    self.plTab = WidgetWeb(self, mdPlusin.code)
                    _wgTemp = self.plTab
                elif (code == 'CATEGORY-LIST'):
                    self.plTab = WidgetCategory(self)
                    _wgTemp = self.plTab
                elif (code == 'PRODUCT-LINE'):
                    self.plTab = WidgetProductLine(self)
                    _wgTemp = self.plTab
                elif (code == 'NEWAIM-CATEGORY'):
                    self.plTab = WidgetNewaimCategory(self)
                    _wgTemp = self.plTab
                elif (code == 'KEYWORD-LIST'):
                    self.plTab = WidgetSkuKeyword(self)
                    _wgTemp = self.plTab
                elif (code == 'PRODUCT-CATEGORY'):
                    self.plTab = WidgetProductNewaimCategory(self)
                    _wgTemp = self.plTab

                elif (code == 'AMAZON-PRODUCT-CATEGORY'):
                    self.plTab = WidgetProductAmazonCategory(self)
                    _wgTemp = self.plTab

                elif (code == 'AMAZON-SKU-KEYWORD'):
                    self.plTab = WidgetAmazonSkuKeywordRelation(self)
                    _wgTemp = self.plTabel
                if (code == 'AMAZON-CATEGORY-KEYWORD'):
                    self.plTab = WidgetAmazonCategoryKeywordRelation(self)
                    _wgTemp = self.plTab
                if (code == 'DASHBOARD'):
                    self.plTab = WidgetDashboard(self)
                    _wgTemp = self.plTab

                tabIndex = self.mainTabs.addTab(_wgTemp, _wgTemp.myWidget.windowTitle())
                self.mainTabs.setCurrentIndex(tabIndex)
            else:
                self.mainTabs.setCurrentIndex(tabIndex)

            mdPlusin = None
            pass
        except Exception as e:
            self.log.info(e)
            import traceback;
            traceback.print_exc();
            QMessageBox.information(None, self._("sscode", "Run Error"), e, QMessageBox.Yes)
        pass


    '''进度条 BEGIN ============================'''
    '''显示进度条'''
    def progressBarShow(self, totalNumber=100, curNumber=0, title=''):
        if(totalNumber is None): totalNumber = 100
        self.app.progressBar.setRange(0, totalNumber)
        self.app.progressBar.setValue(curNumber)
        self.app.progressBar.show()

    '''隐藏进累加'''
    def progressBarContinue(self):
        self.app.progressBar.setValue(self.app.progressBar.value() + 1)

    '''隐藏进度条'''
    def progressBarHide(self):
        self.app.progressBar.hide()

    '''进度条 END ============================'''

    '''状态信息 BEGIN ============================'''
    def statusMsg(self, message):
        if message is not None:
            self.app.statusBar().showMessage(message)

    '''状态信息 END ============================'''

