# @Time : 2019/8/5 14:18 
# @Author : Kevin
# @File : DlgCategoryList.py 
# @Software: PyCharm
# coding:utf-8

from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from app.model.dao.DbAmazonProductCategory import Amazon_Product_Category
from app.model.dao.DbSkuKeyword import Pub_Sku_Keyword
from app.model.dao.DbAmazonCategoryKeywordRelation import Amazon_Product_Category_Keyword_Relation
from app.lib.UtilCommon import getModelFields, qt5TableLoadDatas
from app.view.dlgCategoryList import Ui_DlgCategoryList


class DlgCateList(QDialog, Ui_DlgCategoryList):
    sku_list = []
    table_fields = {
        'code': 'Code',
        'title': 'Title',
      }

    def __init__(self, parent, item_list=[],title_list=[]):
        super(DlgCateList, self).__init__()
        self.fWin = parent
        self.item_list = item_list
        self.title_list = title_list


        self.dlg = QDialog()
        self.setupUi(self.dlg)

        self.twCategoryList.setColumnWidth(0, 120)
        self.twCategoryList.setColumnWidth(1, 260)
        self.tbSave.clicked.connect(self.actTbSaveClicked)


        self.loadData()
        self.dlg.exec_()

    def loadData(self):
        if len(self.item_list) > 0:
            try:
                keywordResult = (Pub_Sku_Keyword.select().where(Pub_Sku_Keyword.title == self.title_list[0]).get())
                results = (Amazon_Product_Category_Keyword_Relation.select().where(Amazon_Product_Category_Keyword_Relation.amazon_keyword_id == keywordResult.id).dicts())
                categoryTitle = []
                if len(results) > 0:
                    for result in results:
                        categoryRow = Amazon_Product_Category.select().where(Amazon_Product_Category.id == result['amazon_category_id']).get()
                        categoryTitle.append(categoryRow.title)

                if len(categoryTitle) > 0:
                    msg = '该关键词 {} 关联了 {} 个分类'.format(
                        ','.join(self.title_list) if len(self.title_list) < 15 else '%个Keyword' % len(self.title_list),
                        ','.join(categoryTitle) if len(categoryTitle) < 5 else '%s个Category' % len(categoryTitle))
                    self.lbCategoryList.setText(msg)
                else:
                    self.lbCategoryList.setText(','.join(self.title_list) if len(','.join(self.title_list)) < 100 else '%s个Keyword' % len(self.title_list))

                rows = Amazon_Product_Category\
                    .select()\
                    .where(Amazon_Product_Category.code != 1)\
                    .order_by(Amazon_Product_Category.created_at.desc())\
                    .dicts()
                #print(rows)
                if len(rows) > 0:
                    qt5TableLoadDatas(self.twCategoryList, rows, self.table_fields,False, False, False,  False, False, True)

            except Exception as e:
                import traceback
                traceback.print_exc()
                print(e)

        else:
            QMessageBox.information(None, '提示', '该Category没有修改记录')

    def actTbSaveClicked(self):
        """
        根据选中分类保存记录
        """
        select_items = self.twCategoryList.selectedItems()
        select_code = [x.text() for x in select_items if x.column() == 0]
        select_titles = [x.text() for x in select_items if x.column() == 1]

        if self.title_list != '':
            after_title = []
            if len(select_titles) > 20:
                QMessageBox.information(None, '警告', '可选择的Category不能超过20个', QMessageBox.Yes)
            elif len(select_titles) < 1:
                QMessageBox.information(None, '警告', '请选择Category', QMessageBox.Yes)
            else:
                keywordResult = (Pub_Sku_Keyword.select().where(Pub_Sku_Keyword.title == self.title_list[0]).get())
                categoryResult = Amazon_Product_Category.select().where(Amazon_Product_Category.code << select_code).dicts()


                print(keywordResult.id)
                print(categoryResult)

                if len(categoryResult) > 0:
                    for category in categoryResult:
                        after_title.append(category['title'])
                        try:
                            result = (Amazon_Product_Category_Keyword_Relation.insert(
                                amazon_category_id=category['id'],
                                amazon_keyword_id=keywordResult.id
                            ).execute())
                            print(result)
                        except Exception as e:
                            import traceback
                            traceback.print_exc()
                            print(e)

                    req = QMessageBox.information(None, '系统提示', '关键词与分类关联完毕', QMessageBox.Yes)
                    if req == QMessageBox.Yes:
                        print(','.join(self.title_list) if len(self.title_list) < 15 else '%s个Category' % len(self.title_list))
                        print(','.join(after_title) if len(after_title) < 100 else '%s个Keyword' % len(after_title))
                        msg = '该关键词 {} 关联了 {} 个分类'.format(','.join(self.title_list) if len(self.title_list) < 15 else '%个Keyword' % len(self.title_list), ','.join(after_title) if len(after_title) < 5 else '%s个Category' % len(after_title))
                        self.lbCategoryList.setText(msg)
        pass