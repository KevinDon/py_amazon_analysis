# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formProductAsinAmazonCategory.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProductAsinAmazonCategoryForm(object):
    def setupUi(self, ProductAsinAmazonCategoryForm):
        ProductAsinAmazonCategoryForm.setObjectName("ProductAsinAmazonCategoryForm")
        ProductAsinAmazonCategoryForm.resize(906, 655)
        self.vlProductAsinNewaimCategoryForm = QtWidgets.QVBoxLayout(ProductAsinAmazonCategoryForm)
        self.vlProductAsinNewaimCategoryForm.setContentsMargins(2, 6, 2, 2)
        self.vlProductAsinNewaimCategoryForm.setSpacing(3)
        self.vlProductAsinNewaimCategoryForm.setObjectName("vlProductAsinNewaimCategoryForm")
        self.productToolBar = QtWidgets.QWidget(ProductAsinAmazonCategoryForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productToolBar.sizePolicy().hasHeightForWidth())
        self.productToolBar.setSizePolicy(sizePolicy)
        self.productToolBar.setMinimumSize(QtCore.QSize(0, 26))
        self.productToolBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.productToolBar.setObjectName("productToolBar")
        self.hlReportToolBar = QtWidgets.QHBoxLayout(self.productToolBar)
        self.hlReportToolBar.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.hlReportToolBar.setContentsMargins(1, 1, 1, 1)
        self.hlReportToolBar.setSpacing(2)
        self.hlReportToolBar.setObjectName("hlReportToolBar")
        self.tbRefresh = QtWidgets.QToolButton(self.productToolBar)
        self.tbRefresh.setMinimumSize(QtCore.QSize(22, 22))
        self.tbRefresh.setMaximumSize(QtCore.QSize(22, 22))
        self.tbRefresh.setStyleSheet("")
        self.tbRefresh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/button/images/svg/sync-alt-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbRefresh.setIcon(icon)
        self.tbRefresh.setAutoRaise(True)
        self.tbRefresh.setObjectName("tbRefresh")
        self.hlReportToolBar.addWidget(self.tbRefresh)
        self.tbSelection = QtWidgets.QToolButton(self.productToolBar)
        self.tbSelection.setMinimumSize(QtCore.QSize(22, 22))
        self.tbSelection.setMaximumSize(QtCore.QSize(22, 22))
        self.tbSelection.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/button/images/svg/check-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbSelection.setIcon(icon1)
        self.tbSelection.setAutoRaise(True)
        self.tbSelection.setObjectName("tbSelection")
        self.hlReportToolBar.addWidget(self.tbSelection)
        self.tbUnselection = QtWidgets.QToolButton(self.productToolBar)
        self.tbUnselection.setMinimumSize(QtCore.QSize(22, 22))
        self.tbUnselection.setMaximumSize(QtCore.QSize(22, 22))
        self.tbUnselection.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/button/images/svg/times-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbUnselection.setIcon(icon2)
        self.tbUnselection.setAutoRaise(True)
        self.tbUnselection.setObjectName("tbUnselection")
        self.hlReportToolBar.addWidget(self.tbUnselection)
        self.tbInvertSelection = QtWidgets.QToolButton(self.productToolBar)
        self.tbInvertSelection.setMinimumSize(QtCore.QSize(22, 22))
        self.tbInvertSelection.setMaximumSize(QtCore.QSize(22, 22))
        self.tbInvertSelection.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/button/images/svg/retweet-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbInvertSelection.setIcon(icon3)
        self.tbInvertSelection.setAutoRaise(True)
        self.tbInvertSelection.setObjectName("tbInvertSelection")
        self.hlReportToolBar.addWidget(self.tbInvertSelection)
        self.line_2 = QtWidgets.QFrame(self.productToolBar)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.hlReportToolBar.addWidget(self.line_2)
        self.tbSearch = QtWidgets.QToolButton(self.productToolBar)
        self.tbSearch.setMinimumSize(QtCore.QSize(22, 22))
        self.tbSearch.setMaximumSize(QtCore.QSize(50, 50))
        self.tbSearch.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/button/images/svg/search-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbSearch.setIcon(icon4)
        self.tbSearch.setAutoExclusive(False)
        self.tbSearch.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.tbSearch.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tbSearch.setAutoRaise(True)
        self.tbSearch.setArrowType(QtCore.Qt.NoArrow)
        self.tbSearch.setObjectName("tbSearch")
        self.hlReportToolBar.addWidget(self.tbSearch)
        self.tbInputCsv = QtWidgets.QToolButton(self.productToolBar)
        self.tbInputCsv.setMinimumSize(QtCore.QSize(22, 22))
        self.tbInputCsv.setMaximumSize(QtCore.QSize(22, 22))
        self.tbInputCsv.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/button/images/svg/file-import-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbInputCsv.setIcon(icon5)
        self.tbInputCsv.setAutoRaise(True)
        self.tbInputCsv.setObjectName("tbInputCsv")
        self.hlReportToolBar.addWidget(self.tbInputCsv)
        self.tbDelete = QtWidgets.QToolButton(self.productToolBar)
        self.tbDelete.setMinimumSize(QtCore.QSize(22, 22))
        self.tbDelete.setMaximumSize(QtCore.QSize(22, 22))
        self.tbDelete.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/button/images/svg/times-circle-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbDelete.setIcon(icon6)
        self.tbDelete.setAutoRaise(True)
        self.tbDelete.setObjectName("tbDelete")
        self.hlReportToolBar.addWidget(self.tbDelete)
        self.line = QtWidgets.QFrame(self.productToolBar)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hlReportToolBar.addWidget(self.line)
        self.lbPagerInfo = QtWidgets.QLabel(self.productToolBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbPagerInfo.sizePolicy().hasHeightForWidth())
        self.lbPagerInfo.setSizePolicy(sizePolicy)
        self.lbPagerInfo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbPagerInfo.setObjectName("lbPagerInfo")
        self.hlReportToolBar.addWidget(self.lbPagerInfo)
        self.widget_2 = QtWidgets.QWidget(self.productToolBar)
        self.widget_2.setObjectName("widget_2")
        self.hlReportToolBar.addWidget(self.widget_2)
        self.vlProductAsinNewaimCategoryForm.addWidget(self.productToolBar)
        self.twProductAsinAmazonCategoryList = QtWidgets.QTableWidget(ProductAsinAmazonCategoryForm)
        self.twProductAsinAmazonCategoryList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twProductAsinAmazonCategoryList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.twProductAsinAmazonCategoryList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twProductAsinAmazonCategoryList.setObjectName("twProductAsinAmazonCategoryList")
        self.twProductAsinAmazonCategoryList.setColumnCount(3)
        self.twProductAsinAmazonCategoryList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twProductAsinAmazonCategoryList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twProductAsinAmazonCategoryList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twProductAsinAmazonCategoryList.setHorizontalHeaderItem(2, item)
        self.twProductAsinAmazonCategoryList.horizontalHeader().setHighlightSections(False)
        self.vlProductAsinNewaimCategoryForm.addWidget(self.twProductAsinAmazonCategoryList)
        self.vlProductAsinNewaimCategoryForm.setStretch(1, 1)

        self.retranslateUi(ProductAsinAmazonCategoryForm)
        QtCore.QMetaObject.connectSlotsByName(ProductAsinAmazonCategoryForm)

    def retranslateUi(self, ProductAsinAmazonCategoryForm):
        _translate = QtCore.QCoreApplication.translate
        ProductAsinAmazonCategoryForm.setWindowTitle(_translate("ProductAsinAmazonCategoryForm", "Product And Category Relationship(Amazon)"))
        self.lbPagerInfo.setText(_translate("ProductAsinAmazonCategoryForm", "R:{1}"))
        self.twProductAsinAmazonCategoryList.setSortingEnabled(True)
        item = self.twProductAsinAmazonCategoryList.horizontalHeaderItem(0)
        item.setText(_translate("ProductAsinAmazonCategoryForm", "#"))
        item = self.twProductAsinAmazonCategoryList.horizontalHeaderItem(1)
        item.setText(_translate("ProductAsinAmazonCategoryForm", "SKU"))
        item = self.twProductAsinAmazonCategoryList.horizontalHeaderItem(2)
        item.setText(_translate("ProductAsinAmazonCategoryForm", "Category"))


import icons_rc
