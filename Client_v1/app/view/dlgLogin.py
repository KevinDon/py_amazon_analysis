# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgLogin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgLogin(object):
    def setupUi(self, DlgLogin):
        DlgLogin.setObjectName("DlgLogin")
        DlgLogin.resize(664, 500)
        DlgLogin.setMinimumSize(QtCore.QSize(660, 500))
        DlgLogin.setMaximumSize(QtCore.QSize(664, 500))

        self.groupBox = QtWidgets.QGroupBox(DlgLogin)
        self.groupBox.setGeometry(QtCore.QRect(120, 110, 441, 221))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(13, 70, 121, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.leAccount = QtWidgets.QLineEdit(self.groupBox)
        self.leAccount.setGeometry(QtCore.QRect(150, 70, 241, 20))
        self.leAccount.setObjectName("leAccount")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 121, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lePassword = QtWidgets.QLineEdit(self.groupBox)
        self.lePassword.setGeometry(QtCore.QRect(150, 110, 241, 20))
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassword.setObjectName("lePassword")
        self.pbOk = QtWidgets.QPushButton(self.groupBox)
        self.pbOk.setGeometry(QtCore.QRect(150, 170, 111, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/button/images/button/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbOk.setIcon(icon)
        self.pbOk.setObjectName("pbOk")
        self.pbCancel = QtWidgets.QPushButton(self.groupBox)
        self.pbCancel.setGeometry(QtCore.QRect(280, 170, 111, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/button/images/button/quit.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancel.setIcon(icon1)
        self.pbCancel.setObjectName("pbCancel")
        self.tbSetting = QtWidgets.QToolButton(self.groupBox)
        self.tbSetting.setGeometry(QtCore.QRect(10, 180, 31, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/button/images/button/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbSetting.setIcon(icon2)
        self.tbSetting.setObjectName("tbSetting")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 121, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.cbLanguage = QtWidgets.QComboBox(self.groupBox)
        self.cbLanguage.setGeometry(QtCore.QRect(150, 30, 241, 22))
        self.cbLanguage.setObjectName("cbLanguage")
        self.cbLanguage.addItem("")
        self.cbLanguage.addItem("")
        self.leMessage = QtWidgets.QLabel(DlgLogin)
        self.leMessage.setGeometry(QtCore.QRect(70, 340, 531, 81))
        self.leMessage.setText("")
        self.leMessage.setTextFormat(QtCore.Qt.PlainText)
        self.leMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.leMessage.setWordWrap(True)
        self.leMessage.setObjectName("leMessage")

        self.retranslateUi(DlgLogin)
        QtCore.QMetaObject.connectSlotsByName(DlgLogin)

    def retranslateUi(self, DlgLogin):
        _translate = QtCore.QCoreApplication.translate
        DlgLogin.setWindowTitle(_translate("DlgLogin", "Login Window"))
        self.groupBox.setTitle(_translate("DlgLogin", "User Login"))
        self.label.setText(_translate("DlgLogin", "User Account"))
        self.label_2.setText(_translate("DlgLogin", "Password"))
        self.pbOk.setText(_translate("DlgLogin", "Ok"))
        self.pbOk.setShortcut(_translate("DlgLogin", "Return"))
        self.pbCancel.setText(_translate("DlgLogin", "Exit"))
        self.pbCancel.setShortcut(_translate("DlgLogin", "Esc"))
        self.tbSetting.setText(_translate("DlgLogin", "..."))
        self.label_3.setText(_translate("DlgLogin", "Language"))
        self.cbLanguage.setItemText(0, _translate("DlgLogin", "简体中文"))
        self.cbLanguage.setItemText(1, _translate("DlgLogin", "English"))

import icons_rc
