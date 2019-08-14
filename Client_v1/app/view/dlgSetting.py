# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgSetting.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DlgSetting(object):
    def setupUi(self, DlgSetting):
        DlgSetting.setObjectName("DlgSetting")
        DlgSetting.resize(780, 313)
        self.groupBox = QtWidgets.QGroupBox(DlgSetting)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 351, 211))
        self.groupBox.setObjectName("groupBox")
        self.leDbHost = QtWidgets.QLineEdit(self.groupBox)
        self.leDbHost.setGeometry(QtCore.QRect(30, 50, 301, 20))
        self.leDbHost.setObjectName("leDbHost")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 121, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 121, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.leDbUsername = QtWidgets.QLineEdit(self.groupBox)
        self.leDbUsername.setGeometry(QtCore.QRect(30, 110, 301, 20))
        self.leDbUsername.setObjectName("leDbUsername")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 150, 121, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.leDbPassword = QtWidgets.QLineEdit(self.groupBox)
        self.leDbPassword.setGeometry(QtCore.QRect(30, 170, 301, 20))
        self.leDbPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leDbPassword.setObjectName("leDbPassword")
        self.pbSave = QtWidgets.QPushButton(DlgSetting)
        self.pbSave.setGeometry(QtCore.QRect(320, 270, 161, 23))
        self.pbSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/button/images/button/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbSave.setIcon(icon)
        self.pbSave.setIconSize(QtCore.QSize(16, 16))
        self.pbSave.setObjectName("pbSave")
        self.groupBox_2 = QtWidgets.QGroupBox(DlgSetting)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 30, 341, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.leServiceUrl = QtWidgets.QLineEdit(self.groupBox_2)
        self.leServiceUrl.setGeometry(QtCore.QRect(20, 50, 301, 20))
        self.leServiceUrl.setObjectName("leServiceUrl")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(20, 30, 121, 16))
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")

        self.retranslateUi(DlgSetting)
        QtCore.QMetaObject.connectSlotsByName(DlgSetting)

    def retranslateUi(self, DlgSetting):
        _translate = QtCore.QCoreApplication.translate
        DlgSetting.setWindowTitle(_translate("DlgSetting", "System Setting"))
        self.groupBox.setTitle(_translate("DlgSetting", "Server Configuration"))
        self.leDbHost.setText(_translate("DlgSetting", "Host"))
        self.label_2.setText(_translate("DlgSetting", "Server"))
        self.label_5.setText(_translate("DlgSetting", "Username"))
        self.label_6.setText(_translate("DlgSetting", "Password"))
        self.pbSave.setText(_translate("DlgSetting", "Save Configuration"))
        self.pbSave.setShortcut(_translate("DlgSetting", "Ctrl+S"))
        self.groupBox_2.setTitle(_translate("DlgSetting", "Api Configuration"))
        self.leServiceUrl.setText(_translate("DlgSetting", "127.0.0.1"))
        self.label_19.setText(_translate("DlgSetting", "Api Server"))


import icons_rc
