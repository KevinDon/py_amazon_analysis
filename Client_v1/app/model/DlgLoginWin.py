# coding:utf-8
import sys, os
import requests as req
from PyQt5.QtWidgets import QDialog, QApplication
from app.lib.ServiceApi import ServiceApi
from app.lib.logger import Log
from app.model.dao.DbConfig import DbConfig
from app.model.DlgSettingWin import DlgSetting
from app.view.dlgLogin import Ui_DlgLogin


class DlgLogin(QDialog, Ui_DlgLogin):
    def __init__(self, mainWin):

        # qssStyle = self.load_qss('app/resource/css/app_style.css')

        super(DlgLogin, self).__init__()

        self.mainWin = mainWin
        self.dlg = self
        self.setupUi(self.dlg)
        #self.setStyleSheet(qssStyle)

        self.log = Log('info')
        self.tbSetting.clicked.connect(self.actionSetting)
        self.pbOk.clicked.connect(self.actionOk)
        self.pbCancel.clicked.connect(self.actionCancel)



       # self.setStyleSheet('QWidget{background-color:rgb(0,0,0)}')  # 增加的代码

        T = DbConfig().get(main_key='user', minor_key='account')
        self.leAccount.setText(T.value)
        T = DbConfig().get(main_key='user', minor_key='password')
        self.lePassword.setText(T.value)
        T = DbConfig().get(main_key='user', minor_key='language')
        self.cbLanguage.setCurrentText(T.value)
        # 语言切换
        self.cbLanguage.currentTextChanged.connect(self.changeLanguage)


        self.dlg.exec_()


    '''语言切换'''
    def changeLanguage(self):

        if (self.cbLanguage.currentText() == '简体中文'):
            self.mainWin.trans.load(self.mainWin.rootPath + '/en_ZH')
            _app = QApplication.instance()
            _app.installTranslator(self.mainWin.trans)

        else:
            _app = QApplication.instance()
            _app.removeTranslator(self.mainWin.trans)

        self.retranslateUi(self)
        self.mainWin.mainFrame.retranslateUi(self)

    '''打开设置窗口'''
    def actionSetting(self):
        try:
            DlgSetting(self.mainWin)
        except Exception as e:
            print(e)
        pass

    '''登录服务器动作'''
    def actionOk(self):
        canLogin = True
        self.pbOk.setDisabled(True)
        self.leMessage.setStyleSheet("color:red");

        if not self.leAccount.text():
            self.leMessage.setText('Account is required')
            canLogin = False

        if not self.lePassword.text():
            self.leMessage.setText('Password is required')
            canLogin = False

        if canLogin:
            try:
                url = "{0}/api/v1/apitokenauth".format(self.mainWin.configs.leServiceUrl.value)
                params = {
                    'username': self.leAccount.text(),
                    'password': self.lePassword.text()
                }
                response = req.api.post(url, json=params, timeout=100)
                if response.status_code == 200:

                    if response.json()['status'] == 200 and response.json()['data']['token'] != "":
                        self.mainWin.token = response.json()['data']['token']
                        self.mainWin.user = ServiceApi.getUser(self.mainWin, self.mainWin.token)

                        T = DbConfig().get(main_key='user', minor_key='account')
                        T.value = self.leAccount.text()
                        T.save()
                        T = DbConfig().get(main_key='user', minor_key='password')
                        T.value = self.lePassword.text()
                        T.save()
                        T = DbConfig().get(main_key='user', minor_key='language')
                        T.value = self.cbLanguage.currentText()
                        T.save()
                    else:
                        self.leMessage.setText('Failed login: {0}'.format('Account or Password is error'))
                else:
                    self.leMessage.setText('Failed login {0}'.format(response.json()['error']))

                self.pbOk.setDisabled(False)

            except Exception as e:
                self.leMessage.setText('Failed login {0}'.format(e))

        if self.mainWin.user.account:
            self.dlg.close()

    def actionCancel(self):
        self.dlg.close()

    #加载txt后缀的qss样式，如qss.txt，输入参数为qss.txt的路径(str)，返回stylesheet(str)
    def load_qss(self, qss_path):
        stylesheet = ''
        try:
            if os.path.exists(qss_path):
                file = open(qss_path,'r', encoding='UTF-8')
                for line in file:
                    stylesheet+=line
        except:
            import traceback
            traceback.print_exc()
            print('qss import error')

        return stylesheet
