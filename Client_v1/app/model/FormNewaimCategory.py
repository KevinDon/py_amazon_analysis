# @Time : 2019/7/17 15:43 
# @Author : Kevin
# @File : FormNewaimCategory.py 
# @Software: PyCharm
# coding:utf-8

import os, csv, datetime, re, time, xlrd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu, QTableWidgetItem, QFileDialog, QTableWidgetSelectionRange

from app.lib.UtilCommon import getTime, utQTableWidgetItem, logger, utStr2Float, utStr2Int, utGetStyleContent
from app.lib.UtilDb import QueryBuildToStr
from app.model.WidgetSearchField import WidgetSearchField
from app.model.dao.DbProductAsin import Na_Product_Asin
from app.model.dao.DbProductAsinCategory import Pub_Product_Asin_Category_Relation
from app.model.dao.DbProductCategory import Pub_Product_Category
from app.model.MdDlgCateHistoryLog import DlgCateHistoryLog
from app.model.dao.DbProductCategoryModLog import Pub_Product_Category_Mod_Log
from app.model.vo.MdUser import User
from app.view.formNewaimCategory import Ui_NewaimCategoryForm


class WidgetNewaimCategory(QWidget, Ui_NewaimCategoryForm):
    _ = QCoreApplication.translate

    def __init__(self, mainWin):
        super(WidgetNewaimCategory, self).__init__()
        self.mainWin = mainWin
        self.myWidget = QWidget()
        self.setupUi(self.myWidget)
        self.canMoveView = False
        # 搜索窗口
        self.search_box = None
        self.searchObj = {
            "fields": [
                 {'name': 'title', 'label': 'Title', 'type': 'string'}
                ,{ 'name': 'code', 'label': 'Code', 'type': 'string'}
                ,{ 'name': 'updated_at', 'label': 'Updated At', 'type': 'date'}
                ,{ 'name': 'created_at', 'label': 'Created At', 'type': 'date'}
                ,{ 'name': 'level', 'label': 'Level', 'type': 'int'}
                ,{ 'name': 'parent_id', 'label': 'Parent Id', 'type': 'int'}
            ],
        }

        self.pageSize = 10000

        self.tbInputCsv.clicked.connect(self.actTbInputCsvClicked)

        self.tbRefresh.clicked.connect(self.actTbRefreshClicked)

        #隐藏导入SKU与分类关系按钮
        self.pushButton.clicked.connect(self.actTbInputSkuAndCategoryClicked)


        self.tbActionLog.clicked.connect(self.actTbCatLog)

        self.tbSelection.clicked.connect(self.actTbSelectionClicked)
        self.tbUnselection.clicked.connect(self.actTbUnselectionClicked)
        self.tbInvertSelection.clicked.connect(self.actTbInvertSelectionClicked)
        self.tbDelete.clicked.connect(self.actTbDeleteClicked)

        self.tbInputCsv.setHidden(True)
        self.pushButton.setHidden(True)
        self.tbDelete.setHidden(True)
        self.tbActionLog.setHidden(True)

        self.twNewaimProductCategoryList.itemSelectionChanged.connect(self.actTwProductListSelectionChanged)
        self.twNewaimProductCategoryList.horizontalHeader().sectionClicked.connect(self.actTwProductListHorSectionClicked)
        self.tbSearch.clicked.connect(self.actTbSearchClicked)

        # 初始化布局
        self.initLayout()
        self.initData()
        self.setLayout(self.myWidget.layout())

    def initLayout(self):
        self.twNewaimProductCategoryList.setColumnHidden(0, True),
        self.twNewaimProductCategoryList.setColumnWidth(1,260)
        self.twNewaimProductCategoryList.setColumnWidth(2,180)
        self.twNewaimProductCategoryList.setColumnWidth(3,140)
        self.twNewaimProductCategoryList.setColumnWidth(4,140)
        self.twNewaimProductCategoryList.setColumnWidth(5,80)
        self.twNewaimProductCategoryList.setColumnWidth(6,80)
        self.twNewaimProductCategoryList.setColumnHidden(5, True),
        self.twNewaimProductCategoryList.setColumnHidden(6, True),
        pass

    '''高级搜索数据'''
    def goSearch(self, conditions, method=None):
        _table_ent = 'Pub_Product_Category'
        _where = QueryBuildToStr(_table_ent, conditions)
        self.initData(_where)
        pass

    def initData(self, _where = ''):
        try:
            # 初始加载第一页最新数据，过滤Status为3的记录
            try:
                rows = Pub_Product_Category.select().paginate(1, self.pageSize).where(Pub_Product_Category.status != 3)
                dataType = True
            except Pub_Product_Category.DoesNotExist:
                # 新增操作
                dataType = False

            if(_where != ''): rows = eval('rows.where({0})'.format(_where))

            self.twNewaimProductCategoryList.setRowCount(0)
            if dataType :
                _rowCount = len(rows)
                self.lbPagerInfo.setText(' R:{0}'.format(_rowCount))
                nowTime = datetime.datetime.now()
                self.mainWin.progressBarShow(_rowCount)
                self.mainWin.statusMsg('开始加载 {0}...'.format(nowTime.strftime('%H:%M:%S')))
                if (_rowCount > 0):
                    # logger.info('加载了 %s 条, 每页 %s 条' %(_rowCount, self.pageSize))
                    self.twNewaimProductCategoryList.setRowCount(_rowCount)
                    for i in range(_rowCount):
                        self.mainWin.progressBarContinue()

                        row = Pub_Product_Category(**(rows[i].__data__))

                        item = utQTableWidgetItem(row.id)
                        # item.setCheckState(Qt.Unchecked)
                        self.twNewaimProductCategoryList.setItem(i, 0, item)
                        self.twNewaimProductCategoryList.setItem(i, 1, utQTableWidgetItem(row.title))
                        self.twNewaimProductCategoryList.setItem(i, 2, utQTableWidgetItem(row.code))
                        self.twNewaimProductCategoryList.setItem(i, 3, utQTableWidgetItem(row.updated_at))
                        self.twNewaimProductCategoryList.setItem(i, 4, utQTableWidgetItem(row.created_at))
                        self.twNewaimProductCategoryList.setItem(i, 5, utQTableWidgetItem(row.level))
                        self.twNewaimProductCategoryList.setItem(i, 6, utQTableWidgetItem(row.parent_id))


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

    def actTbInputCsvClicked(self):
        dlg = QMessageBox.question(None, "操作提示", "您“确定”从CSV导入数据吗?", QMessageBox.Yes | QMessageBox.No)
        if (dlg == QMessageBox.Yes):
            file, ok1 = QFileDialog.getOpenFileName(None, "请选择CSV文件打开", "", "Csv File (*.csv)")
            if (file.__len__() > 0):
                self.twNewaimProductCategoryList.clear()
                #self.twNewaimProductCategoryList.setRowCount(0)
                self.twNewaimProductCategoryList.setHorizontalHeaderLabels(['ID', 'Name', 'Code', 'Updated At', 'Created At', 'Level', 'Parent Id', ])
                # 读取文件总行数
                try:
                    nowTime = datetime.datetime.now()
                    tempfile = open(file, "rb")
                    importLines = len(tempfile.readlines()) - 1
                    tempfile.close()

                    # 读取csv文件方式
                    csvFile = open(file, "r", encoding= 'UTF-8')
                    reader = csv.reader(csvFile)  # 返回的是迭代类型

                    self.twNewaimProductCategoryList.setRowCount(importLines or 2)
                    self.mainWin.progressBarShow(importLines)
                    self.mainWin.statusMsg('开始导入 {0}...'.format(nowTime.strftime('%H:%M:%S')))
                    #tempfile.close()
                    i = 0
                    for row in reader:
                        if (i > 0):
                            self.actTbSve(row, i)
                        #csvFile.close()
                        i = i + 1

                    self.mainWin.progressBarContinue()
                    csvFile.close()
                    endTime = datetime.datetime.now()
                    self.mainWin.statusMsg('完成导入 {0}条数据，用时{1}'.format(importLines, (endTime - nowTime)))
                    self.mainWin.progressBarHide()
                    # self.actTbRefreshClicked()

                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    logger.info(e)
        pass

    '''报表列表全选'''
    def actTbSelectionClicked(self):
        self.twNewaimProductCategoryList.setFocus()
        selectedCount = self.twNewaimProductCategoryList.rowCount()
        qtwsr = QTableWidgetSelectionRange(0,0,selectedCount-1, self.twNewaimProductCategoryList.columnCount()-1)
        self.twNewaimProductCategoryList.setRangeSelected(qtwsr, True)
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''报表列表取消选择'''
    def actTbUnselectionClicked(self):
        self.twNewaimProductCategoryList.setFocus()
        selectedCount = self.twNewaimProductCategoryList.rowCount()
        qtwsr = QTableWidgetSelectionRange(0, 0, selectedCount-1, self.twNewaimProductCategoryList.columnCount()-1)
        self.twNewaimProductCategoryList.setRangeSelected(qtwsr, False)
        self.mainWin.statusMsg('您选中了{0}行'.format(0))

    '''报表列表反选'''
    def actTbInvertSelectionClicked(self):
        self.twNewaimProductCategoryList.setFocus()
        row_num = self.twNewaimProductCategoryList.rowCount()
        column_num = self.twNewaimProductCategoryList.columnCount()-1
        selectedCount = 0
        if (row_num > 0):
            listRows = set(self.getTwProductListSelectionChangedRowsNum())
            for i in range(row_num):
                qtwsr = QTableWidgetSelectionRange(i, 0, i, column_num)
                if(i in listRows):
                    self.twNewaimProductCategoryList.setRangeSelected(qtwsr, False)
                else:
                    self.twNewaimProductCategoryList.setRangeSelected(qtwsr, True)
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
            self.search_box = WidgetSearchField(self, self.searchObj)
            self.vlCategoryForm.insertWidget(1, self.search_box, 1)
            self.vlCategoryForm.setStretch(2, 100)
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
            ranges = self.twNewaimProductCategoryList.selectedRanges()
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
                    id = self.twNewaimProductCategoryList.item(i, 0).text()

                    #将Status设置为3（删除）
                    Pub_Product_Category.update(status=3).where(Pub_Product_Category.id == id).execute()

                    #删除与SKU关系表下的记录
                    try:
                        row = Pub_Product_Asin_Category_Relation.get(Pub_Product_Asin_Category_Relation.productcategorymodel_id == id)
                        row.delete_instance()
                    except Pub_Product_Asin_Category_Relation.DoesNotExist:
                        print('Categories are not associated with SKU')

                    selectedCount += 1
                self.actTbRefreshClicked()
            self.mainWin.statusMsg('您删除了{0}行'.format(selectedCount))
        else:
            QMessageBox.information(None, '操作提示', '请先选择要删除的记录', QMessageBox.Yes)
            pass

    '''保存到数据库'''
    def actTbSve(self, row, index):

        nowTime = datetime.datetime.now()
        cur_time = getTime()
        cur_user = self.mainWin.app.user.id

        newItem = QTableWidgetItem(str(row[3]))
        self.twNewaimProductCategoryList.setItem(index - 1, 1, newItem)
        newItem = QTableWidgetItem(str(row[0]))
        self.twNewaimProductCategoryList.setItem(index - 1, 2, newItem)
        newItem = QTableWidgetItem(str(nowTime))
        self.twNewaimProductCategoryList.setItem(index - 1, 3, newItem)
        newItem = QTableWidgetItem(str(nowTime))
        self.twNewaimProductCategoryList.setItem(index - 1, 4, newItem)
        newItem = QTableWidgetItem(str(row[5]))
        self.twNewaimProductCategoryList.setItem(index - 1, 5, newItem)
        newItem = QTableWidgetItem(str(row[2]))
        self.twNewaimProductCategoryList.setItem(index - 1, 6, newItem)

        try:

            # 非空而且已修改的记录
            try:
                row_before_edit = Pub_Product_Category.get(Pub_Product_Category.code == str(row[0]))
                is_added = False
            except Exception as e:
                # 新增操作
                is_added = True

            result = Pub_Product_Category.insert(
                code=row[0],
                title=row[3],
                creator_id=cur_user,
                status=1,
                sort=0,
                level=row[5] ,
                #parent_id=int(row[2])
            ).on_conflict(
                conflict_target=(Pub_Product_Category.code,),
                preserve=(Pub_Product_Category.code),
                update={
                    'title': row[3],
                    'updated_at': cur_time
                }).execute()

            row_after_edit = Pub_Product_Category.get_by_id(result)

            print(row[3])
            if not is_added :
                if str(row_after_edit.__data__['name']) != str(row_before_edit.__data__['name']):
                    print(row_before_edit.__data__['name'])
                    print(is_added)
                    result = DlgCateHistoryLog.insert(
                        category=str(row[0]),
                        old_val=row_before_edit.__data__['name'],
                        new_val=str(row[3]),
                        modify_fields = 'name',
                        status=1,
                        sort=0,
                        creator_id=cur_user,
                        updated_at= cur_time,
                        created_at= cur_time,
                    ).execute()
                else:
                    DlgCateHistoryLog.insert({
                        'category':str(row[0]),
                        'modify_fields': 'Add New Category',
                        'new_val': str(row_after_edit.__data__),
                        'create_at': cur_time,
                        'creator_id': cur_user
                    }).execute()

        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)
        pass

    '''导入SKU和Categeroy的关系表'''
    def actTbInputSkuAndCategoryClicked(self):
        dlg = QMessageBox.question(None, "操作提示", "您“确定”从CSV导入数据吗?", QMessageBox.Yes | QMessageBox.No)
        if (dlg == QMessageBox.Yes):
            file, ok1 = QFileDialog.getOpenFileNames(None, "请选择XLS文件打开", "", "Xls File (*.xls)")
            if (file.__len__() > 0):

                try:

                    # 打开XLS文件
                    data = xlrd.open_workbook(file[0])
                    # 获取XLS文件里的第二个表格
                    table = data.sheet_by_index(0)
                    importLines = table.nrows - 1
                    for i in range(importLines):
                        if (i > 0):
                            #根据NodeID查询对应分类表ID
                            nodeId = table.row_values(i)[2]
                            sku = table.row_values(i)[0]


                            try:
                                categoryRow = Pub_Product_Category.select().where(Pub_Product_Category.title == nodeId).get()
                                categoryId =  categoryRow.id
                            except Pub_Product_Category.DoesNotExist:
                                categoryId =  0
                            try:
                                skuRow = Na_Product_Asin.select().where(Na_Product_Asin.sku == sku).get()
                                skuId =  skuRow.id
                            except Na_Product_Asin.DoesNotExist:
                                skuId =  0

                            print(categoryId)
                            print(skuId)
                            #return
                            try:
                                if  int(categoryId) > 0 and int(skuId) > 0:
                                    #掺入到NA PRODUCT ASIN CATEGORYB表中
                                    Pub_Product_Asin_Category_Relation.insert(
                                        productasinmodel_id=skuId,
                                        productcategorymodel_id=categoryId,
                                    ).on_conflict(
                                        conflict_target=(Pub_Product_Asin_Category_Relation.id,),
                                        preserve=(Pub_Product_Asin_Category_Relation.id),
                                        update={
                                            'productasinmodel_id': skuId,
                                            'productcategorymodel_id': categoryId
                                        }).execute()
                            except Exception as e:
                                import traceback
                                traceback.print_exc()
                                logger.info(e)

                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    logger.info(e)

        pass

    '''
    弹出分类修改历史
    '''
    def actTbCatLog(self):
        """
        弹出SKU修改历史
        """
        # self.progressBar.hide()
        # self.progressText.hide()

        select_items = self.twNewaimProductCategoryList.selectedItems()
        select_cats = [x.text() for x in select_items if x.column() == 2]
        select_titles = [x.text() for x in select_items if x.column() == 1]

        if len(select_cats) > 20:
            QMessageBox.information(None, '警告', '查看修改历史可选择的Category不能超过20个', QMessageBox.Yes)
        elif len(select_cats) < 1:
            QMessageBox.information(None, '警告', '没有选择Category', QMessageBox.Yes)
        else:
            DlgCateHistoryLog(self, select_cats, select_titles)

        pass
