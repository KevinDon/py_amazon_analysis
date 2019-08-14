# coding:utf-8
import os

from PyQt5.QtWidgets import QDialog, QMessageBox

from app.lib.logger import Log
from app.view.dlgSetting import Ui_DlgSetting


class DlgSetting(QDialog, Ui_DlgSetting):
    def __init__(self, mainWin):
        super(DlgSetting, self).__init__()
        self.mainWin = mainWin
        self.dlg = QDialog()
        self.setupUi(self.dlg)
        self.log = Log('info')

        self.init()
        self.pbSave.clicked.connect(self.actionSave)

        self.dlg.exec_()

    def init(self):

        if (not self.mainWin.configs.leDbHost.value): self.mainWin.configs.leDbHost.value = '127.0.0.1'
        self.leDbHost.setText(self.mainWin.configs.leDbHost.value)

        if (not self.mainWin.configs.leDbUsername.value): self.mainWin.configs.leDbUsername.value = 'postgres'
        self.leDbUsername.setText(self.mainWin.configs.leDbUsername.value)

        if (not self.mainWin.configs.leDbPassword.value): self.mainWin.configs.leDbPassword.value = ''
        self.leDbPassword.setText(self.mainWin.configs.leDbPassword.value)

        if (not self.mainWin.configs.leServiceUrl.value): self.mainWin.configs.leServiceUrl.value = ''
        self.leServiceUrl.setText(self.mainWin.configs.leServiceUrl.value)


        pass

    def actionSave(self):
        try:

            self.mainWin.configs.leDbHost.value = self.leDbHost.text()
            self.mainWin.configs.leDbHost.save()

            self.mainWin.configs.leDbUsername.value = self.leDbUsername.text()
            self.mainWin.configs.leDbUsername.save()

            self.mainWin.configs.leDbPassword.value = self.leDbPassword.text()
            self.mainWin.configs.leDbPassword.save()

            self.mainWin.configs.leServiceUrl.value = self.leServiceUrl.text()
            self.mainWin.configs.leServiceUrl.save()

        except Exception as e:
            print(e)

        if(QMessageBox.information(self, '操作提示', ' 保存完成，要关闭配置窗口吗', QMessageBox.Yes| QMessageBox.No) == QMessageBox.Yes):
            self.dlg.close()

    '''删除指定路径及文件'''
    def del_file(self, path):
        if os.path.isdir(path):
            ls = os.listdir(path)
            for i in ls:
                c_path = os.path.join(path, i)
                if os.path.isdir(c_path):
                    try:
                        os.removedirs(c_path)
                    except Exception as e:
                        self.del_file(c_path)
                else:
                    os.remove(c_path)
        else:
            if os.path.exists(path):
                os.remove(path)
