# coding:utf-8

import os, csv, datetime, re
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu, QTableWidgetItem, QFileDialog, QTableWidgetSelectionRange

from app.lib.UtilCommon import utQTableWidgetItem, getTime, logger, utStr2Float, utStr2Int, utGetStyleContent
from app.lib.UtilDb import QueryBuildToStr
from app.model.WidgetSearchField import WidgetSearchField
from app.model.dao.DbBusinessReport import Na_Business_Report
from app.model.dao.DbProductAsin import Na_Product_Asin
from app.view.formBusinessReport import Ui_BusinessReportForm


class WidgetBusinessReport(QWidget, Ui_BusinessReportForm):
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
        super(WidgetBusinessReport, self).__init__()
        self.mainWin = mainWin
        self.myWidget = QWidget()
        self.setupUi(self.myWidget)
        self.canMoveView = False
        self.pageSize = 2000

        self.lineVerTabSpace.pressed.connect(self.actLineVerTabSpaceClicked)
        self.tbInputCsv.clicked.connect(self.actTbInputCsvClicked)
        self.tbRefresh.clicked.connect(self.actTbRefreshClicked)

        self.tbSelection.clicked.connect(self.actTbSelectionClicked)
        self.tbUnselection.clicked.connect(self.actTbUnselectionClicked)
        self.tbInvertSelection.clicked.connect(self.actTbInvertSelectionClicked)
        self.tbDelete.clicked.connect(self.actTbDeleteClicked)
        self.tbPreview.clicked.connect(self.actTbPreviewClicked)

        self.twSkuList.itemClicked.connect( self.actTwSkuListClicked)
        self.twSkuList.sortByColumn(0, Qt.AscendingOrder)
        self.twDateList.itemClicked.connect( self.actTwDateListClicked)
        self.twDateList.sortByColumn(0, Qt.DescendingOrder)

        self.twReportList.sortByColumn(14, Qt.DescendingOrder)

        self.twSkuList.setSortingEnabled(False)
        self.twDateList.setSortingEnabled(False)
        self.twReportList.setSortingEnabled(False)
        # 导航关键字

        self.searchNavField = []

        # SKU导航搜索窗口参数
        self.search_box = None
        self.searchObj = {
            "fields": [
                {'name': 'sku', 'label': 'SKU', 'type': 'string'}
                ,{ 'name': 'asin', 'label': 'ASIN', 'type': 'string'}
                ,{ 'name': 'asin', 'label': 'ASIN', 'type': 'string'}
                ,{ 'name': 'combine_type', 'label': 'Combine Type', 'type': 'combo'}
            ],
        }
        self.tbSearchNav.clicked.connect(self.actTbSearchNavClicked)

        # REPORT导航搜索窗口参数
        self.searchDetails_box = None
        self.searchDetailsObj = {
            "fields": [
                { 'name': 'asin_parent', 'label': 'ASIN (parent)', 'type': 'string'},
                { 'name': 'asin_child', 'label': 'ASIN (child)', 'type': 'string'},
                { 'name': 'title', 'label': 'Title', 'type': 'string'},
                { 'name': 'sessions', 'label': 'Sessions', 'type': 'int'},
                { 'name': 'sessions_percentage', 'label': 'Sessions per.', 'type': 'float'},
                { 'name': 'page_view', 'label': 'Page Views', 'type': 'int'},
                { 'name': 'page_view_percentage', 'label': 'Page Views per.', 'type': 'float'},
                { 'name': 'buy_box_percentage', 'label': 'BuyBox per.', 'type': 'int'},
                { 'name': 'units_ordered', 'label': 'Units Ordered', 'type': 'int'},
                { 'name': 'unit_session_percentage', 'label': 'Units Ordered per.', 'type': 'float'},
                { 'name': 'ordered_product_sales', 'label': 'Ordered Product Sales', 'type': 'float'},
                { 'name': 'total_order_items', 'label': 'Total Order Items', 'type': 'int'},
                { 'name': 'report_date', 'label': 'Report Date', 'type': 'date'},
            ],
            "method": 2
        }
        self.tbSearchDetails.clicked.connect(self.actTbSearchDetailsClicked)


        # 初始化布局
        self.initLayout()
        self.initData()
        self.setLayout(self.myWidget.layout())


    '''打开SKU高级搜索'''
    def actTbSearchNavClicked(self):
        if self.search_box is None :
            self.search_box = WidgetSearchField(self, self.searchObj , self.CHOICES_COMBINE_TYPE)
            self.vlDate.insertWidget(1, self.search_box, 1)
            self.vlDate.setStretch(2, 100)
        elif self.search_box.isHidden():
            self.search_box.setHidden(False)
            self.search_box.myWidget.close()
        else:
            self.search_box.setHidden(True)
        pass


    '''打开SKU高级搜索'''
    def actTbSearchDetailsClicked(self):
        if self.searchDetails_box is None :
            self.searchDetails_box = WidgetSearchField(self, self.searchDetailsObj)
            self.vlReportC.insertWidget(1, self.searchDetails_box, 1)
            self.vlReportC.setStretch(2, 100)
        elif self.searchDetails_box.isHidden():
            self.searchDetails_box.setHidden(False)
            self.searchDetails_box.myWidget.close()
        else:
            self.searchDetails_box.setHidden(True)
        pass


    '''高级搜索数据'''
    def goSearch(self, conditions, method=None):
        try:
            if method is None:
                # 搜索SKU
                _table_ent = 'Na_Product_Asin'

                for condition in conditions:
                    if condition[-1] == 'combo':
                        for index in self.CHOICES_COMBINE_TYPE:
                            if self.CHOICES_COMBINE_TYPE[index] == condition[2]:
                                condition[2] = index
                                print(self.CHOICES_COMBINE_TYPE[index])

                _where = QueryBuildToStr(_table_ent, conditions)
                self.initData(skuWhere= _where)
            else:
                # 搜索 Report
                _table_ent = 'Na_Business_Report'
                _where = QueryBuildToStr(_table_ent, conditions)
                if self.searchNavField.__len__()>0:
                    if(self.searchNavField[0][0] == 'asin'):
                        self.loadReportList(asin=self.searchNavField[0][1],  _where=_where)
                    else:
                        # todo
                        self.loadReportList(reportDate=self.searchNavField[0][1], _where=_where)
                        #self.loadReportList()
                else:
                    self.loadReportList(_where= _where)
        except Exception as e:
            import traceback
            traceback.print_exc()
            logger.info(e)

        pass


    def initLayout(self):
        self.lhBusinessReportForm.setStretch(0,20)
        self.lhBusinessReportForm.setStretch(2,100)
        self.twSubNav.setMinimumWidth(250)
        self.twDateList.setColumnWidth(0, 200)
        self.twSkuList.setColumnWidth(0, 200)
        self.twSkuList.setColumnWidth(1, 150)

        self.twReportList.setColumnWidth(1,100)
        self.twReportList.setColumnWidth(2,100)
        self.twReportList.setColumnWidth(3,100)
        self.twReportList.setColumnWidth(4,250)
        self.twReportList.setColumnWidth(5,70)
        self.twReportList.setColumnWidth(6,90)
        self.twReportList.setColumnWidth(7,90)
        self.twReportList.setColumnWidth(8,100)
        self.twReportList.setColumnWidth(9,100)
        self.twReportList.setColumnWidth(10,100)
        self.twReportList.setColumnWidth(11,105)
        self.twReportList.setColumnWidth(12,130)
        self.twReportList.setColumnWidth(13,110)

        self.twReportList.setColumnHidden(0, True)
        self.twReportList.setColumnHidden(1, True)
        pass

    def initData(self, skuWhere=''):
        try:
            # 初始加载日期Tab
            rows = Na_Business_Report.select(Na_Business_Report.report_date).group_by(Na_Business_Report.report_date).order_by(Na_Business_Report.report_date.desc())
            self.twDateList.setRowCount(0)
            _rowCount = len(rows)
            if (_rowCount > 0):
                self.twDateList.setRowCount(_rowCount)
                for i in range(_rowCount):
                    self.twDateList.setItem(i, 0, utQTableWidgetItem(rows[i].report_date))
                pass

            # 初始加载SKU Tab
            rows = Na_Product_Asin.select()
            if (skuWhere != ''): rows = eval('rows.where({0})'.format(skuWhere))
            self.twSkuList.setRowCount(0)
            _rowCount = len(rows)
            nowTime = datetime.datetime.now()
            self.mainWin.progressBarShow(_rowCount)
            self.mainWin.statusMsg('开始加载 {0}...'.format(nowTime.strftime('%H:%M:%S')))

            if (_rowCount > 0):
                self.twSkuList.setRowCount(_rowCount)
                for i in range(_rowCount):
                    self.mainWin.progressBarContinue()

                    self.twSkuList.setItem(i, 0, utQTableWidgetItem(rows[i].sku))
                    self.twSkuList.setItem(i, 1, utQTableWidgetItem(rows[i].asin))
                    self.twSkuList.setItem(i, 2, utQTableWidgetItem(self.CHOICES_COMBINE_TYPE[rows[i].combine_type]))

            endTime = datetime.datetime.now()
            self.mainWin.statusMsg('加载 {0}条数据，用时{1}'.format(_rowCount, (endTime - nowTime)))
            self.mainWin.progressBarHide()
            logger.info('加载了 %s 条, 每页 %s 条' % (i, self.pageSize))

            pass

            self.loadReportList()
        except Exception as e:
            logger.info(e)
        pass


    def loadReportList(self, pageNo=1, pageSize=0, asin=None,sku=None, reportDate=None, _where=''):
        try:
            # 初始加载最新数据
            _pageSize = pageSize if pageSize>0 else self.pageSize
            rows = Na_Business_Report.select().paginate(pageNo, _pageSize).order_by(Na_Business_Report.report_date.desc())
            if asin != None:
                if _where == '':
                    rows = rows.where(Na_Business_Report.asin_child==asin)
                else:
                    rows = eval('rows.where((Na_Business_Report.asin_child=="{0}") & {1})'.format(asin, _where))
            elif reportDate != None:
                if _where == '':
                    rows = rows.where(Na_Business_Report.report_date==reportDate)
                else:
                    rows = eval('rows.where((Na_Business_Report.report_date=="{0}") & {1})'.format(reportDate, _where))
            elif _where != '':
                rows = eval('rows.where({0})'.format(_where))

            self.twReportList.setRowCount(0)

            _rowCount = len(rows)

            nowTime = datetime.datetime.now()
            self.mainWin.progressBarShow(_rowCount)
            self.mainWin.statusMsg('开始加载 {0}...'.format(nowTime.strftime('%H:%M:%S')))

            if (_rowCount > 0):
                # logger.info('加载了 %s 条, 每页 %s 条' %(_rowCount, self.pageSize))
                self.lbPagerInfo.setText('P:{0} | R:{1}'.format(1,_rowCount))
                self.twReportList.setRowCount(_rowCount)
                for i in range(_rowCount):
                    self.mainWin.progressBarContinue()

                    row = Na_Business_Report(**(rows[i].__data__))

                    self.twReportList.setItem(i, 0, utQTableWidgetItem(row.id))
                    item = utQTableWidgetItem('')
                    self.twReportList.setItem(i, 1, item)
                    # item = QTableWidgetItem('%.4f' % row.run_time)
                    # item.setTextAlignment(Qt.AlignRight + Qt.AlignVCenter)
                    # item = QTableWidgetItem('{0}'.format( cuNone2Object(row.asin_parent) ))
                    self.twReportList.setItem(i, 2, utQTableWidgetItem(row.asin_parent))
                    self.twReportList.setItem(i, 3, utQTableWidgetItem(row.asin_child))
                    self.twReportList.setItem(i, 4, utQTableWidgetItem(row.title))
                    self.twReportList.setItem(i, 5, utQTableWidgetItem(row.sessions, 0))
                    self.twReportList.setItem(i, 6, utQTableWidgetItem(row.sessions_percentage, 0.00))
                    self.twReportList.setItem(i, 7, utQTableWidgetItem(row.page_view, 0))
                    self.twReportList.setItem(i, 8, utQTableWidgetItem(row.page_view_percentage, 0.00))
                    self.twReportList.setItem(i, 9, utQTableWidgetItem(row.buy_box_percentage, 0.00))
                    self.twReportList.setItem(i, 10, utQTableWidgetItem(row.units_ordered, 0))
                    self.twReportList.setItem(i, 11, utQTableWidgetItem(row.unit_session_percentage, 0.00))
                    self.twReportList.setItem(i, 12, utQTableWidgetItem(row.ordered_product_sales, 0.00))
                    self.twReportList.setItem(i, 13, utQTableWidgetItem(row.total_order_items, 0))
                    self.twReportList.setItem(i, 14, utQTableWidgetItem(row.report_date))
                    self.twReportList.setItem(i, 15, utQTableWidgetItem(row.created_at))

            endTime = datetime.datetime.now()
            self.mainWin.statusMsg('加载 {0}条数据，用时{1}'.format(_rowCount, (endTime - nowTime)))
            self.mainWin.progressBarHide()
            if _rowCount == 0 :
                self.mainWin.statusMsg('该SKU {0} 对应的报告数据没有记录'.format(sku))
        except Exception as e:
            import traceback
            traceback.print_exc()
            logger.info(e)


    def actTbRefreshClicked(self):
        self.searchNavField = []
        self.initData()
        pass

    '''导入功能'''
    def actTbInputCsvClicked(self):
        dataCount = self.twDateList.rowCount()
        dlg = QMessageBox.question(None, "操作提示", "您“确定”从CSV导入数据吗?", QMessageBox.Yes | QMessageBox.No)
        if (dlg == QMessageBox.Yes and dataCount > 0):
            for i in range(dataCount):
                self.twDateList.removeRow(dataCount - i - 1)

        if (dlg == QMessageBox.Yes):
            file, ok1 = QFileDialog.getOpenFileName(None, "请选择CSV文件打开", "", "Csv File (*.csv)")
            if (file.__len__() > 0):
                # 读取文件总行数
                try:
                    # 获取Report 日期
                    _fileName = os.path.basename(file)
                    reportDate = re.search('\d{4}-\d{1,2}-\d{1,2}', _fileName).group(0) if (re.search('\d{4}-\d{1,2}-\d{1,2}', _fileName) is not None) else ''

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
                           self.actTbSve(row, reportDate)
                        i = i + 1
                        self.mainWin.progressBarContinue()

                    csvFile.close()

                    endTime = datetime.datetime.now()
                    self.mainWin.statusMsg('完成导入 {0}条数据，用时{1}'.format(importLines, (endTime - nowTime)))
                    self.mainWin.progressBarHide()
                    self.actTbRefreshClicked()

                except Exception as e:
                    logger.info(e)
        pass

    '''报表列表全选'''
    def actTbSelectionClicked(self):
        self.twReportList.setFocus()
        selectedCount = self.twReportList.rowCount()
        qtwsr = QTableWidgetSelectionRange(0, 0, selectedCount - 1, self.twReportList.columnCount() - 1)
        self.twReportList.setRangeSelected(qtwsr, True)
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''报表列表取消选择'''
    def actTbUnselectionClicked(self):
        self.twReportList.setFocus()
        selectedCount = self.twReportList.rowCount()
        qtwsr = QTableWidgetSelectionRange(0, 0, selectedCount - 1, self.twReportList.columnCount() - 1)
        self.twReportList.setRangeSelected(qtwsr, False)
        self.mainWin.statusMsg('您选中了{0}行'.format(0))

    '''报表列表反选'''
    def actTbInvertSelectionClicked(self):
        self.twReportList.setFocus()
        row_num = self.twReportList.rowCount()
        column_num = self.twReportList.columnCount() - 1
        selectedCount = 0
        if (row_num > 0):
            listRows = set(self.getTwReportListSelectionChangedRowsNum())
            for i in range(row_num):
                qtwsr = QTableWidgetSelectionRange(i, 0, i, column_num)
                if (i in listRows):
                    self.twReportList.setRangeSelected(qtwsr, False)
                else:
                    self.twReportList.setRangeSelected(qtwsr, True)
                    selectedCount += 1

        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''返回选中行'''
    def getTwReportListSelectionChangedRowsNum(self):
        result = []
        try:
            ranges = self.twReportList.selectedRanges()
            for i in range(len(ranges)):
                for row in range(ranges[i].topRow(), ranges[i].bottomRow() + 1):
                    result.append(row)

        except Exception as e:
            print(e)

        # 去重返回
        return list(set(result))
        pass

    '''点击SKU列表'''
    def actTwSkuListClicked(self, rowObj):
        try:
            sku = self.twSkuList.item(rowObj.row(), 0).text()
            asin = self.twSkuList.item(rowObj.row(), 1).text()
            if(asin != None):
                self.searchNavField = [['asin', asin]]
                self.loadReportList(pageNo=1, pageSize=5000,asin=asin, sku=sku)
        except Exception as e:
            print(e)
        pass

    '''点击SKU列表'''
    def actTwDateListClicked(self, rowObj):
        try:
            report_date = self.twDateList.item(rowObj.row(), 0).text()
            if(report_date != None):
                self.searchNavField = [['report_date', report_date]]
                self.loadReportList(pageNo=1, pageSize=5000,reportDate=report_date)
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)
        pass

    '''删除选择行'''
    def actTbDeleteClicked(self):
        rowIndex = self.getTwReportListSelectionChangedRowsNum()
        selectedCount = 0
        if rowIndex.__len__() > 0:
            if QMessageBox.information(None, '操作提示', '您确定要删除选中的记录吗？', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                for i in rowIndex:
                    id = self.twReportList.item(i, 0).text()
                    Na_Business_Report.delete_by_id(id)
                    selectedCount += 1

                self.actTbRefreshClicked()
            self.mainWin.statusMsg('您删除了{0}行'.format(selectedCount))
        else:
            QMessageBox.information(None, '操作提示', '请先选择要删除的记录', QMessageBox.Yes)
            pass

    '''设置可以移动'''
    def actLineVerTabSpaceClicked(self):
        self.canMoveView = True

    '''调整切分窗口比例'''
    def mouseMoveEvent(self, event):
        # 鼠标左键
        if (event.buttons() == Qt.LeftButton and self.canMoveView == True):
            self.lhBusinessReportForm.setStretch(0, event.x())
            self.lhBusinessReportForm.setStretch(2, self.width() - event.x())
            self.lhBusinessReportForm.update()

    '''调整切分窗口比例'''
    def mouseReleaseEvent(self, event):
        # 鼠标左键
        if (event.buttons() == Qt.LeftButton and self.canMoveView == True):
            self.lhBusinessReportForm.setStretch(0, event.x())
            self.lhBusinessReportForm.setStretch(2, self.width() - event.x())
            self.lhBusinessReportForm.update()

        self.canMoveView = False


    '''保存到数据库'''
    def actTbSve(self, row, reportDate):
        title = row[2] [0:255] if len(row[2]) > 255 else row[2]
        try:
            result = (Na_Business_Report.insert(
                asin_parent=row[0]
                , asin_child=row[1]
                , title=title
                , sessions=utStr2Int(row[3])
                , sessions_percentage=utStr2Float(row[4])
                , page_view=utStr2Int(row[5])
                , page_view_percentage=utStr2Float(row[6])
                , buy_box_percentage=utStr2Float(row[7])
                , units_ordered=utStr2Int(row[8])
                , unit_session_percentage=utStr2Float(row[9])
                , ordered_product_sales=utStr2Float(row[10])
                , total_order_items=utStr2Int(row[11])
                , report_date=reportDate
            ).execute())
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)

    '''跳到Chart TAG'''
    def actTbPreviewClicked(self):
        self.mainWin.actLoadModelView('CHARTS')
        pass