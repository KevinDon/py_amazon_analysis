# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_twDashboard(object):
    def setupUi(self, twDashboard):
        twDashboard.setObjectName("twDashboard")
        twDashboard.resize(908, 678)
        self.vlDashboard = QtWidgets.QVBoxLayout(twDashboard)
        self.vlDashboard.setContentsMargins(2, 6, 2, 2)
        self.vlDashboard.setSpacing(3)
        self.vlDashboard.setObjectName("vlDashboard")
        self.groupBox = QtWidgets.QGroupBox(twDashboard)
        self.groupBox.setObjectName("groupBox")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(20, 40, 108, 12))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.na_product_value = QtWidgets.QLabel(self.splitter)
        self.na_product_value.setObjectName("na_product_value")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_2.setGeometry(QtCore.QRect(20, 70, 132, 12))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.na_productLine_value = QtWidgets.QLabel(self.splitter_2)
        self.na_productLine_value.setObjectName("na_productLine_value")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_3.setGeometry(QtCore.QRect(20, 100, 108, 12))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        self.label_3.setObjectName("label_3")
        self.na_Category_value = QtWidgets.QLabel(self.splitter_3)
        self.na_Category_value.setObjectName("na_Category_value")
        self.vlDashboard.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(twDashboard)
        self.groupBox_2.setObjectName("groupBox_2")
        self.splitter_6 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_6.setGeometry(QtCore.QRect(20, 40, 108, 12))
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_4 = QtWidgets.QLabel(self.splitter_6)
        self.label_4.setObjectName("label_4")
        self.amazon_produts = QtWidgets.QLabel(self.splitter_6)
        self.amazon_produts.setObjectName("amazon_produts")
        self.splitter_5 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_5.setGeometry(QtCore.QRect(20, 70, 120, 12))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_5 = QtWidgets.QLabel(self.splitter_5)
        self.label_5.setObjectName("label_5")
        self.amazon_category = QtWidgets.QLabel(self.splitter_5)
        self.amazon_category.setObjectName("amazon_category")
        self.splitter_4 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_4.setGeometry(QtCore.QRect(20, 100, 108, 12))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_6 = QtWidgets.QLabel(self.splitter_4)
        self.label_6.setObjectName("label_6")
        self.amazon_keywords = QtWidgets.QLabel(self.splitter_4)
        self.amazon_keywords.setObjectName("amazon_keywords")
        self.vlDashboard.addWidget(self.groupBox_2)

        self.retranslateUi(twDashboard)
        QtCore.QMetaObject.connectSlotsByName(twDashboard)

    def retranslateUi(self, twDashboard):
        _translate = QtCore.QCoreApplication.translate
        twDashboard.setWindowTitle(_translate("twDashboard", "Dashboard"))
        self.groupBox.setTitle(_translate("twDashboard", "Newaim Information"))
        self.label.setText(_translate("twDashboard", "Products:"))
        self.na_product_value.setText(_translate("twDashboard", "TextLabel"))
        self.label_2.setText(_translate("twDashboard", "Product Line:"))
        self.na_productLine_value.setText(_translate("twDashboard", "TextLabel"))
        self.label_3.setText(_translate("twDashboard", "Category:"))
        self.na_Category_value.setText(_translate("twDashboard", "TextLabel"))
        self.groupBox_2.setTitle(_translate("twDashboard", "Amazon Information"))
        self.label_4.setText(_translate("twDashboard", "Products:"))
        self.amazon_produts.setText(_translate("twDashboard", "TextLabel"))
        self.label_5.setText(_translate("twDashboard", "Categories:"))
        self.amazon_category.setText(_translate("twDashboard", "TextLabel"))
        self.label_6.setText(_translate("twDashboard", "Keywords:"))
        self.amazon_keywords.setText(_translate("twDashboard", "TextLabel"))


import icons_rc
