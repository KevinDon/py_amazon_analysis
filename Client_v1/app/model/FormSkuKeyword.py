# @Time : 2019/7/18 17:46 
# @Author : Kevin
# @File : FormSkuKeyword.py
# @Software: PyCharm
# coding:utf-8


import os, csv, datetime, re
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu, QTableWidgetItem, QFileDialog, QTableWidgetSelectionRange

from app.lib.UtilCommon import getTime, utQTableWidgetItem, logger, utStr2Float, utStr2Int, utGetStyleContent, qt5TableLoadDatas, qt5TableRowAppendField, qt5TableSetHiddenHeaders
from app.lib.UtilDb import QueryBuildToStr
from app.lib.db import pbConn
from app.model.WidgetSearchField import WidgetSearchField
from app.model.DlgCategoryList import DlgCateList

from app.model.dao.DbSkuKeyword import Pub_Sku_Keyword
from app.view.formSkuKeyword import Ui_AmazonKeywordForm


class WidgetSkuKeyword(QWidget, Ui_AmazonKeywordForm):
    _ = QCoreApplication.translate

    fwin = None
    searchText = ''
    searchItems = []
    curDisplayIndex = -1
    is_ready = False  # 初始化标志位
    is_edit_lock = True  # 编辑标志位
    is_after_edit = False  # 已编辑标志位

    table_is_has_edit_col = True  # 表格是否编辑标志列
    # 表格标题字段配置
    table_fields = {
        'id': 'ID', 'title': 'Title', 'platform': 'Platform', 'updated_at': 'Updated At', 'created_at': 'Created At', 'keyword_type' : 'Keyword Type'
    }

    # 表格隐藏列设置
    table_fields_hidden = ['id', 'has_edit', 'keyword_type']
    # 表格隐藏列id - 初始化自动根据table_fields_hidden转化
    table_fields_hidden_index = []
    # 表格标题字段配置


    def __init__(self, mainWin):
        super(WidgetSkuKeyword, self).__init__()
        self.mainWin = mainWin
        self.myWidget = QWidget()
        self.setupUi(self.myWidget)
        self.canMoveView = False
        # 搜索窗口
        self.search_box = None
        self.searchObj = {
            "fields": [
                {'name': 'title', 'label': 'Title', 'type': 'string'},
                {'name': 'platform', 'label': 'Platform', 'type': 'string'}
                ,{ 'name': 'updated_at', 'label': 'Updated At', 'type': 'date'}
                , {'name': 'created_at', 'label': 'Created At', 'type': 'date'}
                # , {'name': 'keyword_type', 'label': 'Keyword Type', 'type': 'number'}
                # , {'name': 'is_edit', 'label': 'Edited', 'type': 'number'}
            ],
        }
        self.table_fields_hidden_index = [i for i, x in enumerate(self.table_fields) if x in self.table_fields_hidden]

        self.twAmazonKeyword.setColumnCount(len(self.table_fields))
        self.twAmazonKeyword.setHorizontalHeaderLabels(self.table_fields.values())
        self.twAmazonKeyword.setSortingEnabled(False)


        self.pageSize = 10000

        self.tbSave.clicked.connect(self.actTbSave)

        self.tbInputCsv.clicked.connect(self.actTbInputCsvClicked)
        self.tbRefresh.clicked.connect(self.actTbRefreshClicked)

        self.tbSelection.clicked.connect(self.actTbSelectionClicked)
        self.tbUnselection.clicked.connect(self.actTbUnselectionClicked)
        self.tbInvertSelection.clicked.connect(self.actTbInvertSelectionClicked)
        self.tbDelete.clicked.connect(self.actTbDeleteClicked)
        self.tbSearch.clicked.connect(self.actTbSearchClicked)

        self.twAmazonKeyword.cellChanged.connect(self.tableCellChanged)
        self.twAmazonKeyword.doubleClicked.connect(self.tableCellClicked)
        self.twAmazonKeyword.itemSelectionChanged.connect(self.acttwAmazonKeywordSelectionChanged)
        self.twAmazonKeyword.horizontalHeader().sectionClicked.connect(self.acttwAmazonKeywordHorSectionClicked)
        # self.twAmazonKeyword.doubleClicked.connect(self.dlgCategory)
        self.tbAssociate.clicked.connect(self.actTbStbAssociateClicked)
        #
        datas = Pub_Sku_Keyword.keywordListAll(self)

        qt5TableLoadDatas(self.twAmazonKeyword, datas, self.table_fields, has_edit_flag=self.table_is_has_edit_col, process_bar=False, is_can_sort=False)



        qt5TableSetHiddenHeaders(self.twAmazonKeyword, self.table_fields_hidden, self.table_fields, has_edit_flag=self.table_is_has_edit_col)

        self.twAmazonKeyword.setColumnWidth(len(self.table_fields), 0) if self.table_is_has_edit_col else None

        self.is_ready = True

        # 初始化布局
        self.initLayout()
        #self.initData()
        self.setLayout(self.myWidget.layout())
        self.is_ready = True

    def initLayout(self):
        self.twAmazonKeyword.setColumnWidth(0,80)
        self.twAmazonKeyword.setColumnWidth(1,220)
        self.twAmazonKeyword.setColumnWidth(2,150)
        self.twAmazonKeyword.setColumnWidth(3,140)
        self.twAmazonKeyword.setColumnHidden(0, True)
        pass

    '''高级搜索数据'''
    def goSearch(self, conditions, method=None):
        _table_ent = 'Pub_Sku_Keyword'
        _where = QueryBuildToStr(_table_ent, conditions)
        self.initData(_where)
        pass

    def initData(self, _where = ''):
        try:
            # 初始加载第一页最新数据
            rows = Pub_Sku_Keyword.select().paginate(1, self.pageSize)
            if(_where != ''): rows = eval('rows.where({0})'.format(_where))

            self.twAmazonKeyword.setRowCount(0)

            _rowCount = len(rows)
            nowTime = datetime.datetime.now()
            self.mainWin.progressBarShow(_rowCount)
            self.mainWin.statusMsg('开始加载 {0}...'.format(nowTime.strftime('%H:%M:%S')))
            self.lbPagerInfo.setText(' R:{0}'.format(_rowCount))

            if (_rowCount > 0):
                # logger.info('加载了 %s 条, 每页 %s 条' %(_rowCount, self.pageSize))
                self.twAmazonKeyword.setRowCount(_rowCount)
                for i in range(_rowCount):
                    row = Pub_Sku_Keyword(**(rows[i].__data__))
                    self.mainWin.progressBarContinue()

                    item = utQTableWidgetItem(row.id)
                    # item.setCheckState(Qt.Unchecked)
                    self.twAmazonKeyword.setItem(i, 0, item)
                    self.twAmazonKeyword.setItem(i, 1, utQTableWidgetItem(row.title))
                    self.twAmazonKeyword.setItem(i, 2, utQTableWidgetItem(row.platform))
                    self.twAmazonKeyword.setItem(i, 3, utQTableWidgetItem(row.updated_at))
                    self.twAmazonKeyword.setItem(i, 4, utQTableWidgetItem(row.created_at))
                    self.twAmazonKeyword.setItem(i, 5, utQTableWidgetItem(1))

                endTime = datetime.datetime.now()
                self.mainWin.statusMsg('加载 {0}条数据，用时{1}'.format(_rowCount, (endTime - nowTime)))
                self.mainWin.progressBarHide()

        except Exception as e:
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
                    tempfile = open(file, "r")
                    importLines = len(tempfile.readlines()) - 1
                    tempfile.close()

                    nowTime = datetime.datetime.now()
                    self.mainWin.progressBarShow(importLines)
                    self.mainWin.statusMsg('开始导入 {0}...'.format(nowTime.strftime('%H:%M:%S')))

                    # 读取csv文件方式
                    csvFile = open(file, "r")
                    reader = csv.reader(csvFile)  # 返回的是迭代类型
                    nowTime = datetime.datetime.now()
                    cur_time = getTime()
                    cur_user = self.mainWin.app.user.id

                    i = 0
                    for row in reader:
                        if (i > 0):
                            Pub_Sku_Keyword.insert(
                                title=row[2],
                                platform='amazon',
                                platform_id=1,
                                sort=0,
                                status=1,
                                creator_id=cur_user,
                                created_at=cur_time,
                                updated_at=cur_time,
                            ).on_conflict_ignore(
                                conflict_target=(Pub_Sku_Keyword.title,),
                                preserve=(Pub_Sku_Keyword.title),
                                update={
                                'updator': cur_user,
                                'update_at': cur_time,
                             }
                            ).execute()
                        i = i + 1
                        self.mainWin.progressBarContinue()

                    csvFile.close()

                    endTime = datetime.datetime.now()
                    self.mainWin.statusMsg('完成导出 {0}条数据，用时{1}'.format(importLines, (endTime - nowTime)))
                    self.mainWin.progressBarHide()
                    self.actTbRefreshClicked()

                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    logger.info(e)
        pass

    '''报表列表全选'''
    def actTbSelectionClicked(self):
        self.twAmazonKeyword.setFocus()
        selectedCount = self.twAmazonKeyword.rowCount()
        qtwsr = QTableWidgetSelectionRange(0,0,selectedCount-1, self.twAmazonKeyword.columnCount()-1)
        self.twAmazonKeyword.setRangeSelected(qtwsr, True)
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''报表列表取消选择'''
    def actTbUnselectionClicked(self):
        self.twAmazonKeyword.setFocus()
        selectedCount = self.twAmazonKeyword.rowCount()
        qtwsr = QTableWidgetSelectionRange(0, 0, selectedCount-1, self.twAmazonKeyword.columnCount()-1)
        self.twAmazonKeyword.setRangeSelected(qtwsr, False)
        self.mainWin.statusMsg('您选中了{0}行'.format(0))

    '''报表列表反选'''
    def actTbInvertSelectionClicked(self):
        self.twAmazonKeyword.setFocus()
        row_num = self.twAmazonKeyword.rowCount()
        column_num = self.twAmazonKeyword.columnCount()-1
        selectedCount = 0
        if (row_num > 0):
            listRows = set(self.gettwAmazonKeywordSelectionChangedRowsNum())
            for i in range(row_num):
                qtwsr = QTableWidgetSelectionRange(i, 0, i, column_num)
                if(i in listRows):
                    self.twAmazonKeyword.setRangeSelected(qtwsr, False)
                else:
                    self.twAmazonKeyword.setRangeSelected(qtwsr, True)
                    selectedCount += 1
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''行选中时提示'''
    def acttwAmazonKeywordSelectionChanged(self):
        row = self.gettwAmazonKeywordSelectionChangedRowsNum()
        self.mainWin.statusMsg('您选中了{0}行'.format(row.__len__()))
        pass

    def acttwAmazonKeywordHorSectionClicked(self, index):
        print(index)
        pass

    '''打开高级搜索'''
    def actTbSearchClicked(self):
        if self.search_box is None :
            self.search_box = WidgetSearchField(self, self.searchObj)
            self.vlAmazonKeywordForm.insertWidget(1, self.search_box, 1)
            self.vlAmazonKeywordForm.setStretch(2, 100)
        elif self.search_box.isHidden():
            self.search_box.setHidden(False)
            self.search_box.myWidget.close()
        else:
            self.search_box.setHidden(True)
        pass

    '''返回选中行'''
    def gettwAmazonKeywordSelectionChangedRowsNum(self):
        result = []
        try:
            ranges = self.twAmazonKeyword.selectedRanges()
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
            rowIndex = self.gettwAmazonKeywordSelectionChangedRowsNum()
            selectedCount = 0
            if rowIndex.__len__()>0:
                if QMessageBox.information(None, '操作提示', '您确定要删除选中的记录吗？', QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes :
                    for i in rowIndex:
                        id = self.twAmazonKeyword.item(i, 0).text()
                        Pub_Sku_Keyword.delete_by_id(id)
                        selectedCount += 1

                    self.actTbRefreshClicked()
                self.mainWin.statusMsg('您删除了{0}行'.format(selectedCount))
            else:
                QMessageBox.information(None, '操作提示', '请先选择要删除的记录', QMessageBox.Yes)


    def actTbSave(self):
            rowCount = self.twAmazonKeyword.rowCount()
            if (not rowCount):
                QMessageBox.information(None, "操作提示", "没有数据，不用保存", QMessageBox.Yes)
                return

            nowTime = datetime.datetime.now()
            # self.mainWin.progressBar.setRange(0, rowCount + 10)
            # self.mainWin.progressBar.show()
            # self.mainWin.progressText.setText('开始保存 {0}...'.format(nowTime.strftime('%H:%M:%S')))
            # self.mainWin.progressText.show()
            rows = []
            try:
                #   远端
                cur_time = getTime()
                cur_user = self.mainWin.app.user.id

                self.is_ready = True
                # 保存验证
                valid_flag = True
                for i in range(rowCount):
                    try:
                        # 检查导入数据类型
                        if (self.twAmazonKeyword.item(i, 1) is None or
                                self.twAmazonKeyword.item(i, 2) is None or
                                self.twAmazonKeyword.item(i, 3) is None or
                                self.twAmazonKeyword.item(i, 4) is None):
                            raise Exception('第 %s 行的数据填写不全' % i)

                        # 检查Title是否为空
                        if len(self.twAmazonKeyword.item(i, 2).text().strip()) < 1:
                            raise Exception('第 %s 行的Title不能为空' % (i + 1))

                    except Exception as e:
                        QMessageBox.information(None, '错误', str(e), QMessageBox.Yes)
                        valid_flag = False
                        break

                if valid_flag is False:
                    return

                self.mainWin.progressBarShow(rowCount)
                with pbConn.atomic() as transaction:
                    for i in range(rowCount):

                        if (self.twAmazonKeyword.item(i, 1) is not None and
                                self.twAmazonKeyword.item(i, 2) is not None and
                                self.twAmazonKeyword.item(i, 3) is not None and
                                self.twAmazonKeyword.item(i,  len(self.table_fields)).text() == '1'):
                            #   非空而且已修改的记录
                            try:
                                row_before_edit = Pub_Sku_Keyword().get(Pub_Sku_Keyword.title == self.twAmazonKeyword.item(i, 1).text())
                                is_added = False
                            except Exception as e:
                                # 新增操作
                                is_added = True

                            if is_added:

                                result = (Pub_Sku_Keyword.insert(
                                    title=self.twAmazonKeyword.item(i, 1).text(),
                                    created_at=cur_time,
                                    creator_id=cur_user,
                                    updated_at=cur_time,
                                    status=1,
                                    sort=0,
                                    platform='amazon',
                                    platform_id=1,
                                    keyword_type=1,
                                ).execute())
                                # self.fwin.fwin.send_msg('lock')
                                row_after_edit = Pub_Sku_Keyword.get_by_id(result)



                            '''TODO'''
                            # if is_added:
                            #     Pub_Sku_Keyword.insert({
                            #         'sku': self.twData.item(i, 2).text(),
                            #         'modify_fields': 'Add New SKU',
                            #         'new_val': str(row_after_edit.__data__),
                            #         'create_at': cur_time,
                            #         'creator_id': cur_user.id
                            #     }).execute()
                            # else:
                            #     edit_logs = []
                            #
                            #     fields_need_log = list_filter(self.table_fields.keys(),
                            #                                   ['last_ver', 'creator', 'creator_id', 'create_at',
                            #                                    'updator',
                            #                                    'updator_id', 'update_at'])
                            #
                            #     fields_need_log.append('is_delete')
                            #     # 轮询被修改的字段
                            #     for field in fields_need_log:
                            #         if field and str(row_after_edit.__data__[field]) != str(
                            #                 row_before_edit.__data__[field]):
                            #             edit_logs.append({
                            #                 'sku': self.twData.item(i, 2).text(),
                            #                 'modify_fields': field,
                            #                 'old_val': row_before_edit.__data__[field],
                            #                 'new_val': row_after_edit.__data__[field],
                            #                 'create_at': cur_time,
                            #                 'creator_id': cur_user.id
                            #             })
                            #     if len(edit_logs) > 0:
                            #         for x in range(0, len(edit_logs), 100):
                            #             AppProductImageLogModel.insert_many(edit_logs[x:x + 100]).execute()
                            #         # 清内存
                            #         edit_logs = []

                        self.mainWin.progressBarContinue()
                #     self.progressBar.setValue(self.progressBar.value() + 1)
                # self.progressBar.setValue(self.progressBar.value() + 10)
                self.mainWin.progressBarShow(rowCount)
                endTime = datetime.datetime.now()
                self.mainWin.statusMsg('完成保存，用时{0}'.format((endTime - nowTime)))
                self.mainWin.progressBarHide()
                # self.fwin.fwin.send_msg('lock')
                # self.is_after_edit = False
                req = QMessageBox.information(None, '系统提示', '关键词保存成功', QMessageBox.Yes)
                if req == QMessageBox.Yes:
                    self.actTbRefresh()

                    #self.initData()

            except Exception as e:
                import traceback
                traceback.print_exc()
                req = QMessageBox.information(None, '保存失败', '保存操作失败,请检查数据或联系系统管理员', QMessageBox.Yes)
            # saveCount = MyDb.imageHistorySaveAll(self, rows=rows)

    def tableCellChanged(self, row_id, col_id):

        """
        单元格编辑事件
        :param row_id:
        :param col_id:
        """
        print(row_id)
        if self.is_ready == False or col_id == len(self.table_fields):
            return None
        if self.is_ready and col_id != len(self.table_fields) and self.table_is_has_edit_col:
            print('row:%s,col:%s' % (row_id, col_id))
            self.is_after_edit = True
            qt5TableRowAppendField(self.twAmazonKeyword, row_id, len(self.table_fields), 1)
            # 设置编辑行的背景为浅蓝色
            self.is_ready = False
            for i in range(len(self.table_fields)):
                item = self.twAmazonKeyword.item(row_id, i)
                if type(item) is QTableWidgetItem:
                    item.setBackground(QColor(229, 255, 255))
            self.is_ready = True



    '''
    从数据库中载入
    '''

    def actTbRefresh(self):
        self.is_ready = False
        datas = Pub_Sku_Keyword.keywordListAll(self)

        nowTime = datetime.datetime.now()
        # self.progressBar.setRange(0, datas.__len__())
        # self.progressBar.setValue(0)
        # self.progressBar.show()
        # self.progressText.setText('开始重载 {0}...'.format(nowTime.strftime('%H:%M:%S')))
        # self.progressText.show()

        qt5TableLoadDatas(self.twAmazonKeyword, datas, self.table_fields,
                          has_edit_flag=self.table_is_has_edit_col,
                          process_bar=False, is_can_sort=False)
        qt5TableSetHiddenHeaders(self.twAmazonKeyword, self.table_fields_hidden, self.table_fields,
                                 has_edit_flag=self.table_is_has_edit_col)
        self.twAmazonKeyword.setColumnWidth(len(self.table_fields), 0) if self.table_is_has_edit_col else None
        # self.actTbAdd()

        endTime = datetime.datetime.now()
        # self.progressText.setText('完成重载，用时{0}'.format((endTime - nowTime)))
        # self.is_ready = True
        # self.signal_received_update(False)
        if self.table_is_has_edit_col:
            qt5TableRowAppendField(self.twAmazonKeyword, self.twAmazonKeyword.rowCount() - 1, len(self.table_fields))

        pass

    def dlgCategory(self):
        print('dlgCategory')
        pass

    def actTbStbAssociateClicked(self):
        """
            弹出Category列表
        """
        # self.progressBar.hide()
        # self.progressText.hide()

        select_items = self.twAmazonKeyword.selectedItems()
        select_titles = [x.text() for x in select_items if x.column() == 1]
        select_cats = [x.text() for x in select_items if x.column() == 2]

        if len(select_cats) > 1:
            QMessageBox.information(None, '警告', '请选择一个关键词', QMessageBox.Yes)
        elif len(select_cats) < 1:
            QMessageBox.information(None, '警告', '没有选择关键词', QMessageBox.Yes)
        else:
            DlgCateList(self, select_cats, select_titles)
        pass

    def tableCellClicked(self):
        select_items = self.twAmazonKeyword.selectedItems()


        print(select_items)

    pass