# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgCategoryList.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DlgCategoryList(object):
    def setupUi(self, DlgCategoryList):
        DlgCategoryList.setObjectName("DlgCategoryList")
        DlgCategoryList.resize(901, 612)
        self.lbCategoryList = QtWidgets.QLabel(DlgCategoryList)
        self.lbCategoryList.setGeometry(QtCore.QRect(130, 10, 761, 20))
        self.lbCategoryList.setText("")
        self.lbCategoryList.setObjectName("lbCategoryList")
        self.twCategoryList = QtWidgets.QTableWidget(DlgCategoryList)
        self.twCategoryList.setGeometry(QtCore.QRect(0, 40, 901, 571))
        self.twCategoryList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twCategoryList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.twCategoryList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twCategoryList.setObjectName("twCategoryList")
        self.twCategoryList.setColumnCount(3)
        self.twCategoryList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twCategoryList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twCategoryList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twCategoryList.setHorizontalHeaderItem(2, item)
        self.twCategoryList.horizontalHeader().setHighlightSections(False)
        self.tbInvertSelection = QtWidgets.QToolButton(DlgCategoryList)
        self.tbInvertSelection.setGeometry(QtCore.QRect(100, 10, 22, 22))
        self.tbInvertSelection.setMinimumSize(QtCore.QSize(22, 22))
        self.tbInvertSelection.setMaximumSize(QtCore.QSize(22, 22))
        self.tbInvertSelection.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/button/images/svg/retweet-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbInvertSelection.setIcon(icon)
        self.tbInvertSelection.setAutoRaise(True)
        self.tbInvertSelection.setObjectName("tbInvertSelection")
        self.tbSelection = QtWidgets.QToolButton(DlgCategoryList)
        self.tbSelection.setGeometry(QtCore.QRect(52, 10, 22, 22))
        self.tbSelection.setMinimumSize(QtCore.QSize(22, 22))
        self.tbSelection.setMaximumSize(QtCore.QSize(22, 22))
        self.tbSelection.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/button/images/svg/check-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbSelection.setIcon(icon1)
        self.tbSelection.setAutoRaise(True)
        self.tbSelection.setObjectName("tbSelection")
        self.tbUnselection = QtWidgets.QToolButton(DlgCategoryList)
        self.tbUnselection.setGeometry(QtCore.QRect(76, 10, 22, 22))
        self.tbUnselection.setMinimumSize(QtCore.QSize(22, 22))
        self.tbUnselection.setMaximumSize(QtCore.QSize(22, 22))
        self.tbUnselection.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/button/images/svg/times-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbUnselection.setIcon(icon2)
        self.tbUnselection.setAutoRaise(True)
        self.tbUnselection.setObjectName("tbUnselection")
        self.tbSave = QtWidgets.QToolButton(DlgCategoryList)
        self.tbSave.setGeometry(QtCore.QRect(27, 10, 23, 22))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/button/images/svg/save-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbSave.setIcon(icon3)
        self.tbSave.setObjectName("tbSave")
        self.tbRefresh = QtWidgets.QToolButton(DlgCategoryList)
        self.tbRefresh.setGeometry(QtCore.QRect(3, 10, 22, 22))
        self.tbRefresh.setMinimumSize(QtCore.QSize(22, 22))
        self.tbRefresh.setMaximumSize(QtCore.QSize(22, 22))
        self.tbRefresh.setStyleSheet("")
        self.tbRefresh.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/button/images/svg/sync-alt-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbRefresh.setIcon(icon4)
        self.tbRefresh.setAutoRaise(True)
        self.tbRefresh.setObjectName("tbRefresh")

        self.retranslateUi(DlgCategoryList)
        QtCore.QMetaObject.connectSlotsByName(DlgCategoryList)

    def retranslateUi(self, DlgCategoryList):
        _translate = QtCore.QCoreApplication.translate
        DlgCategoryList.setWindowTitle(_translate("DlgCategoryList", "Dialog"))
        self.twCategoryList.setSortingEnabled(True)
        item = self.twCategoryList.horizontalHeaderItem(0)
        item.setText(_translate("DlgCategoryList", "#"))
        item = self.twCategoryList.horizontalHeaderItem(1)
        item.setText(_translate("DlgCategoryList", "Title"))
        item = self.twCategoryList.horizontalHeaderItem(2)
        item.setText(_translate("DlgCategoryList", "Code"))
        self.tbSave.setText(_translate("DlgCategoryList", "..."))


import icons_rc
