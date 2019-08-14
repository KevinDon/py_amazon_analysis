# @Time : 2019/6/29 11:58
# @Author : Kevin
# @File : FormCategory.py
# @Software: PyCharm
# coding:utf-8

import os, csv, datetime, re, time, xlrd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QUrl, QCoreApplication
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu, QTableWidgetItem, QFileDialog, QTableWidgetSelectionRange

from app.lib.UtilCommon import getTime, utQTableWidgetItem, logger, utStr2Float, utStr2Int, utGetStyleContent
from app.lib.UtilDb import QueryBuildToStr
from app.model.WidgetSearchField import WidgetSearchField
from app.model.dao.DbAmazonProductCategory import Amazon_Product_Category
from app.model.dao.DbProductAsin import Na_Product_Asin
from app.model.dao.DbProductAsinCategory import Pub_Product_Asin_Category_Relation
from app.model.dao.DbProductAsinAmazonCategory import Na_Product_Asin_Amazon_Category
from app.model.dao.DbProductCategory import Pub_Product_Category
from app.model.MdDlgCateHistoryLog import DlgCateHistoryLog
from app.model.dao.DbAmazonPorductCategpryModLog import  Amazon_Product_Category_Mod_Log
from app.model.vo.MdUser import User
from app.view.formCategory import Ui_CategoryForm


class WidgetCategory(QWidget, Ui_CategoryForm):
    _ = QCoreApplication.translate

    def __init__(self, mainWin):
        super(WidgetCategory, self).__init__()
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
                # ,{ 'name': 'level', 'label': 'Level', 'type': 'int'}
                # ,{ 'name': 'parent_id', 'label': 'Parent Id', 'type': 'int'}
            ],
        }

        self.pageSize = 10000

        self.tbInputCsv.clicked.connect(self.actTbInputCsvClicked)
        self.tbRefresh.clicked.connect(self.actTbRefreshClicked)

        #隐藏导入SKU与分类关系按钮
        self.pushButton.clicked.connect(self.actTbInputSkuAndCategoryClicked)
        self.pushButton.setHidden(True)

        self.tbActionLog.clicked.connect(self.actTbCatLog)

        self.tbSelection.clicked.connect(self.actTbSelectionClicked)
        self.tbUnselection.clicked.connect(self.actTbUnselectionClicked)
        self.tbInvertSelection.clicked.connect(self.actTbInvertSelectionClicked)
        self.tbDelete.clicked.connect(self.actTbDeleteClicked)

        self.twProductCategoryList.itemSelectionChanged.connect(self.actTwProductListSelectionChanged)
        self.twProductCategoryList.horizontalHeader().sectionClicked.connect(self.actTwProductListHorSectionClicked)
        self.tbSearch.clicked.connect(self.actTbSearchClicked)

        # 初始化布局
        self.initLayout()
        self.initData()
        self.setLayout(self.myWidget.layout())

    def initLayout(self):
        self.twProductCategoryList.setColumnHidden(0, True),
        self.twProductCategoryList.setColumnWidth(1,280)
        self.twProductCategoryList.setColumnWidth(2,150)
        self.twProductCategoryList.setColumnWidth(3,140)
        self.twProductCategoryList.setColumnWidth(4,140)
        self.twProductCategoryList.setColumnWidth(5,80)
        self.twProductCategoryList.setColumnWidth(6,80)
        self.twProductCategoryList.setColumnHidden(5, True),
        self.twProductCategoryList.setColumnHidden(6, True),
        pass

    '''高级搜索数据'''
    def goSearch(self, conditions, method=None):
        _table_ent = 'Amazon_Product_Category'
        _where = QueryBuildToStr(_table_ent, conditions)
        self.initData(_where)
        pass

    def initData(self, _where = ''):
        try:
            # 初始加载第一页最新数据，过滤Status为3的记录
            rows = Amazon_Product_Category.select().paginate(1, self.pageSize).where(Amazon_Product_Category.status != 3)
            if(_where != ''): rows = eval('rows.where({0})'.format(_where))

            self.twProductCategoryList.setRowCount(0)

            _rowCount = len(rows)
            self.lbPagerInfo.setText(' R:{0}'.format(_rowCount))
            nowTime = datetime.datetime.now()
            self.mainWin.progressBarShow(_rowCount)
            self.mainWin.statusMsg('开始加载 {0}...'.format(nowTime.strftime('%H:%M:%S')))
            if (_rowCount > 0):
                # logger.info('加载了 %s 条, 每页 %s 条' %(_rowCount, self.pageSize))
                self.twProductCategoryList.setRowCount(_rowCount)
                for i in range(_rowCount):
                    row = Amazon_Product_Category(**(rows[i].__data__))
                    self.mainWin.progressBarContinue()

                    item = utQTableWidgetItem(row.id)
                    # item.setCheckState(Qt.Unchecked)
                    self.twProductCategoryList.setItem(i, 0, item)
                    self.twProductCategoryList.setItem(i, 1, utQTableWidgetItem(row.title))
                    self.twProductCategoryList.setItem(i, 2, utQTableWidgetItem(row.code))
                    self.twProductCategoryList.setItem(i, 3, utQTableWidgetItem(row.updated_at))
                    self.twProductCategoryList.setItem(i, 4, utQTableWidgetItem(row.created_at))
                    self.twProductCategoryList.setItem(i, 5, utQTableWidgetItem(row.level))
                    self.twProductCategoryList.setItem(i, 6, utQTableWidgetItem(row.parent_id))

                nowTime = datetime.datetime.now()
                self.mainWin.progressBarShow(_rowCount)
                self.mainWin.statusMsg('开始加载 {0}...'.format(nowTime.strftime('%H:%M:%S')))
        except Exception as e:
            logger.info(e)
        pass

    def actTbRefreshClicked(self):
        self.initData()
        pass

    '''导入功能'''
    def actTbInputCsvClicked(self):
        dlg = QMessageBox.question(None, "操作提示", "您“确定”从XLS导入数据吗?", QMessageBox.Yes | QMessageBox.No)
        if (dlg == QMessageBox.Yes):
            file, ok1 = QFileDialog.getOpenFileNames(None, "请选择Xls文件打开", "", "Xls File (*.xls)")
            if (file.__len__() > 0):
                #self.twProductCategoryList.clear()
                #self.twProductCategoryList.setRowCount(0)
                #self.twProductCategoryList.setHorizontalHeaderLabels(['ID', 'Title', 'Code', 'Updated At', 'Created At', 'Level', 'Parent Id', ])
                # 读取文件总行数
                try:
                    nowTime = datetime.datetime.now()
                    #tempfile = open(file, "r")
                    #打开XLS文件
                    data = xlrd.open_workbook(file[0])
                    #获取XLS文件里的第二个表格
                    table = data.sheet_by_index(1)

                    importLines = table.nrows - 1
                    #self.twProductCategoryList.setRowCount(importLines or 2)

                    self.mainWin.progressBarShow(importLines)

                    self.mainWin.statusMsg('处理数据中...')
                    #检查数据库与上传文件内容配对
                    '''优化导入检查'''
                    differenceRecords = {}
                    categories = Amazon_Product_Category.select(Amazon_Product_Category.title, Amazon_Product_Category.code).order_by(Amazon_Product_Category.code.desc()).execute()
                    rowCount = self.twProductCategoryList.rowCount()

                    stratTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    print("开始时间：" + stratTime)

                    for i in range(importLines):
                        title_list = table.row_values(i)[1].split('/')
                        if (i > 0):
                            for index in range(rowCount):
                               # print(self.twProductCategoryList.item(i, 1).text())
                                if str(self.twProductCategoryList.item(index, 2).text()) == str(table.row_values(i)[0]) and str(title_list[-1]) != self.twProductCategoryList.item(index, 2).text():
                                    differenceRecords[self.twProductCategoryList.item(index, 2)] = self.twProductCategoryList.item(index, 2)


                    endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    print("结束时间：" + endTime)
                    self.mainWin.statusMsg('开始导入 {0}...'.format(nowTime.strftime('%H:%M:%S')))

                    msg = ",".join(str(i) for i in differenceRecords.keys())
                    if(len(differenceRecords) > 0):
                        dlg = QMessageBox.question(None, "操作提示", 'Node ID为' + msg + '的已修改，您“确定”要更新修改记录吗' , QMessageBox.Yes | QMessageBox.No)
                        if (dlg == QMessageBox.Yes):
                            skipRecords = {}
                        else:
                            skipRecords = differenceRecords
                    else:
                        skipRecords = {}
                    for i in range(importLines):
                        if (i > 0):
                            self.actTbSve(table.row_values(i), i, skipRecords)
                        #csvFile.close()

                    self.mainWin.progressBarContinue()
                    endTime = datetime.datetime.now()
                    self.mainWin.statusMsg('完成导入 {0}条数据，用时{1}'.format(importLines, (endTime - nowTime)))
                    self.mainWin.progressBarHide()
                    self.actTbRefreshClicked()

                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    logger.info(e)
        pass

    '''报表列表全选'''
    def actTbSelectionClicked(self):
        self.twProductCategoryList.setFocus()
        selectedCount = self.twProductCategoryList.rowCount()
        qtwsr = QTableWidgetSelectionRange(0,0,selectedCount-1, self.twProductCategoryList.columnCount()-1)
        self.twProductCategoryList.setRangeSelected(qtwsr, True)
        self.mainWin.statusMsg('您选中了{0}行'.format(selectedCount))

    '''报表列表取消选择'''
    def actTbUnselectionClicked(self):
        self.twProductCategoryList.setFocus()
        selectedCount = self.twProductCategoryList.rowCount()
        qtwsr = QTableWidgetSelectionRange(0, 0, selectedCount-1, self.twProductCategoryList.columnCount()-1)
        self.twProductCategoryList.setRangeSelected(qtwsr, False)
        self.mainWin.statusMsg('您选中了{0}行'.format(0))

    '''报表列表反选'''
    def actTbInvertSelectionClicked(self):
        self.twProductCategoryList.setFocus()
        row_num = self.twProductCategoryList.rowCount()
        column_num = self.twProductCategoryList.columnCount()-1
        selectedCount = 0
        if (row_num > 0):
            listRows = set(self.getTwProductListSelectionChangedRowsNum())
            for i in range(row_num):
                qtwsr = QTableWidgetSelectionRange(i, 0, i, column_num)
                if(i in listRows):
                    self.twProductCategoryList.setRangeSelected(qtwsr, False)
                else:
                    self.twProductCategoryList.setRangeSelected(qtwsr, True)
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
        try:
            if self.search_box is None :
                self.search_box = WidgetSearchField(self, self.searchObj)
                self.vlCategoryForm.insertWidget(1, self.search_box, 1)
                self.vlCategoryForm.setStretch(2, 100)
            elif self.search_box.isHidden():
                self.search_box.setHidden(False)
                self.search_box.myWidget.close()
            else:
                self.search_box.setHidden(True)
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)
        pass

    '''返回选中行'''
    def getTwProductListSelectionChangedRowsNum(self):
        result = []
        try:
            ranges = self.twProductCategoryList.selectedRanges()
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
                    id = self.twProductCategoryList.item(i, 0).text()

                    #将Status设置为3（删除）
                    Amazon_Product_Category.update(status=3).where(Amazon_Product_Category.id == id).execute()

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
    def actTbSve(self, row, index,  skipRecords):

        nowTime = datetime.datetime.now()
        cur_time = getTime()
        cur_user = self.mainWin.app.user.id
        title_list = row[1].split('/')

        if len(title_list) > 1:
            parentTitle = title_list[-2]
            parentId = Amazon_Product_Category.getIdByTitle(self, parentTitle)
        else:
            parentId = 1

        #print(skipRecords[str(int(row[0]))])

        if len(skipRecords) > 0 and str(int(row[0])) in skipRecords:
            print('test')
        else :

            try:
                # 非空而且已修改的记录
                try:
                    row_before_edit = Amazon_Product_Category.get(Amazon_Product_Category.code == str(int(row[0])) )
                    is_added = False
                except Amazon_Product_Category.DoesNotExist:
                    # 新增操作
                    is_added = True

                result = Amazon_Product_Category.insert(
                    code=str(int(row[0])),
                    title=title_list[-1],
                    creator_id=cur_user,
                    status=1,
                    platform='amazon',
                    platform_id=1,
                    sort=0,
                    level=len(title_list) - 1,
                    #parent_id=parentId
                ).on_conflict(
                    conflict_target=(Amazon_Product_Category.code,),
                    preserve=(Amazon_Product_Category.code),
                    update={
                        'title': title_list[-1],
                        'updated_at': cur_time
                    }).execute()
                row_after_edit = Amazon_Product_Category.get_by_id(result)
                if not is_added :
                    if str(row_after_edit.__data__['title']) != str(row_before_edit.__data__['title']):
                        print(row_before_edit.__data__['title'])
                        print(is_added)
                        result = Amazon_Product_Category_Mod_Log.insert(
                            category=str(int(row[0])),
                            old_val=row_before_edit.__data__['title'],
                            new_val=title_list[-1],
                            modify_fields = 'title',
                            status=1,
                            sort=1,
                            creator_id=cur_user,
                            updated_at= cur_time,
                            created_at= cur_time,
                        ).execute()

            except Exception as e:
                import traceback
                traceback.print_exc()
                print(e)
        pass

    '''导入SKU和Category的关系表'''
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
                            nodeId = int(table.row_values(i)[1])
                            sku = table.row_values(i)[0]

                            print(sku)
                            try:
                                categoryRow = Amazon_Product_Category.select().where(Amazon_Product_Category.code == nodeId).get()
                                categoryId =  categoryRow.id
                            except Amazon_Product_Category.DoesNotExist:
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
                                    Na_Product_Asin_Amazon_Category.insert(
                                        productasinmodel_id=skuId,
                                        productcategorymodel_id=categoryId,
                                    ).on_conflict(
                                        conflict_target=(Na_Product_Asin_Amazon_Category.id,),
                                        preserve=(Na_Product_Asin_Amazon_Category.id),
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

    '''弹出分类修改历史 '''
    def actTbCatLog(self):
        """
        弹出SKU修改历史
        """
        # self.progressBar.hide()
        # self.progressText.hide()

        select_items = self.twProductCategoryList.selectedItems()
        select_cats = [x.text() for x in select_items if x.column() == 2]
        select_titles = [x.text() for x in select_items if x.column() == 1]

        if len(select_cats) > 20:
            QMessageBox.information(None, '警告', '查看修改历史可选择的Category不能超过20个', QMessageBox.Yes)
        elif len(select_cats) < 1:
            QMessageBox.information(None, '警告', '没有选择Category', QMessageBox.Yes)
        else:
            DlgCateHistoryLog(self, select_cats, select_titles)

        pass
