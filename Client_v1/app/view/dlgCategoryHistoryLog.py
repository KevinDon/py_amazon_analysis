# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgCategoryHistoryLog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DlgCategoryHistoryLog(object):
    def setupUi(self, DlgCategoryHistoryLog):
        DlgCategoryHistoryLog.setObjectName("DlgCategoryHistoryLog")
        DlgCategoryHistoryLog.resize(899, 611)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgCategoryHistoryLog)
        self.buttonBox.setGeometry(QtCore.QRect(550, 580, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.twCategoryLogs = QtWidgets.QTableWidget(DlgCategoryHistoryLog)
        self.twCategoryLogs.setGeometry(QtCore.QRect(10, 40, 881, 541))
        self.twCategoryLogs.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.twCategoryLogs.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twCategoryLogs.setColumnCount(0)
        self.twCategoryLogs.setObjectName("twCategoryLogs")
        self.twCategoryLogs.setRowCount(0)
        self.twCategoryLogs.horizontalHeader().setMinimumSectionSize(0)
        self.lbCategory = QtWidgets.QLabel(DlgCategoryHistoryLog)
        self.lbCategory.setGeometry(QtCore.QRect(10, 10, 1381, 20))
        self.lbCategory.setText("")
        self.lbCategory.setObjectName("lbCategory")

        self.retranslateUi(DlgCategoryHistoryLog)
        self.buttonBox.accepted.connect(DlgCategoryHistoryLog.accept)
        self.buttonBox.rejected.connect(DlgCategoryHistoryLog.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgCategoryHistoryLog)

    def retranslateUi(self, DlgCategoryHistoryLog):
        _translate = QtCore.QCoreApplication.translate
        DlgCategoryHistoryLog.setWindowTitle(_translate("DlgCategoryHistoryLog", "Dialog"))
        self.twCategoryLogs.setSortingEnabled(True)


