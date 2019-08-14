# @Time : 2019/7/13 10:48 
# @Author : Kevin
# @File : MdDlgCateHistoryLog.py 
# @Software: PyCharm
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView, QHeaderView

from app.model.dao.DbAmazonPorductCategpryModLog import Amazon_Product_Category_Mod_Log
from app.lib.UtilCommon import getModelFields, qt5TableLoadDatas
from app.view.dlgCategoryHistoryLog import Ui_DlgCategoryHistoryLog


class DlgCateHistoryLog(QDialog, Ui_DlgCategoryHistoryLog):
    sku_list = []
    table_fields = {'category': 'Category',
                    'modify_fields': '修改字段',
                    'old_val': '修改前',
                    'new_val': '修改后',
                    'created_at': '修改时间',
                    'creator_id': '修改人',
                    }

    def __init__(self, parent, item_list=[],title_list=[]):
        super(DlgCateHistoryLog, self).__init__()
        self.fWin = parent
        self.item_list = item_list
        self.title_list = title_list

        self.dlg = QDialog()
        self.setupUi(self.dlg)
        self.loadData()
        self.dlg.exec_()

    def loadData(self):
        if len(self.item_list) > 0:
            try:
                self.lbCategory.setText(','.join(self.title_list) if len(','.join(self.title_list)) < 100 else '%s个Category' % len(self.title_list))
                rows = Amazon_Product_Category_Mod_Log\
                    .select()\
                    .where((Amazon_Product_Category_Mod_Log.category << self.item_list) & (Amazon_Product_Category_Mod_Log.creator_id == self.fWin.mainWin.app.user.id))\
                    .order_by(Amazon_Product_Category_Mod_Log.created_at.desc())\
                    .dicts()
                #print(rows)
                if len(rows) > 0:
                    qt5TableLoadDatas(self.twCategoryLogs, rows, self.table_fields)
                    self.twCategoryLogs.setEditTriggers(QAbstractItemView.NoEditTriggers)
                    self.twCategoryLogs.setSortingEnabled(True)
            except Exception as e:
                import traceback
                traceback.print_exc()
                print(e)

        else:
            QMessageBox.information(None, '提示', '该Category没有修改记录')

