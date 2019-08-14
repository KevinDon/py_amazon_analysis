# coding:utf-8

import os
import sys
from PyQt5 import QtGui

from PyQt5.QtCore import Qt, QTranslator
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QProgressBar, QLabel
from qtpy import QtCore

from app.lib.UtilCommon import utGetStyleContent
from app.lib.logger import Log
from app.model.WinMain import WinMain
from app.model.dao.DbBusinessReport import Na_Business_Report
from app.model.vo.MdConfig import Config
from app.model.DlgLoginWin import DlgLogin
from app.model.vo.MdUser import User

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.curPath, curFilename = os.path.split(os.path.abspath(sys.argv[0]))
        self.rootPath = self.curPath.replace("\\", "/")
        # 全局日志对象
        self.logger = Log()
        # 布局窗口切分对象组
        self.layoutFormScale = {'obj':None, 'offset':0}
        # 监听对象表
        self.listeners = {}
        # 服务端通讯参数
        self.token = r''
        # 检查数据库链接
        try:
            # 本地配置
            self.configs = Config()
            # 远程配置
            Na_Business_Report.select().limit(1).count()
        except Exception as e:
            self.logger.info(e)
            if(QMessageBox.question(None, "系统提示", " 数据库链接异常，请与管理员联系！", QMessageBox.Yes) == QMessageBox.Yes):
                self.closeMain(True)

        # 语言对象
        self.trans = QTranslator(self)
        self.changeLanguage(self.configs.language.value)


    '''
    用户登录
    '''
    def login(self, relogin=False):
        if not relogin : self.user = User()
        if(not self.user.account):
            try:
               _dlg = DlgLogin(self)
            except Exception as e:
                print(e)
        if self.user.account:
            return True
        else:
            sys.exit(0)
            return False


    '''语言切换'''
    def changeLanguage(self, _lang):
        if (_lang == '简体中文'):
            self.trans.load(self.rootPath + '/en_ZH')
            app.installTranslator(self.trans)
        else:
            app.removeTranslator(self.trans)

        self.configs = Config()
        pass


    '''
    初始设置
    '''
    def initMain(self):
        # 设置主窗体样式
        self.setStyleSheet(utGetStyleContent(self.curPath, 'app_style'))

        # 启动提示
        self.statusBar().showMessage('可以开始了...')

        # 初始化进度条
        self.progressBar = QProgressBar()
        self.progressLabel = QLabel()
        self.progressLabel.setText("进度：")

        self.statusBar().addPermanentWidget(self.progressLabel)
        self.statusBar().addPermanentWidget(self.progressBar)
        self.progressBar.setGeometry(0, 0, 100, 5)
        self.progressBar.setRange(0, 100)  # 设置进度条的范围
        self.progressBar.setValue(0)
        self.progressBar.setFixedHeight(10)
        self.progressBar.setFixedWidth(200)
        self.progressBar.hide()
        self.progressLabel.hide()

        self.setWindowIcon(QtGui.QIcon(':icons/images/winlogo.png'))
        pass

    '''
    初始化自适应调整布局
    '''
    def resizeEvent(self, event):
        innerHeight = event.size().height() - 75

    '''
    按下退出键提示是否退出系统
    '''
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.closeMain()

    '''
    关闭主窗口提示
    '''
    def closeEvent(self, event):
        if (not self.closeMain()):
            event.ignore()

    '''关闭主程序'''
    def closeMain(self, skipInquiry = False):
        if skipInquiry == False:
            req = QMessageBox.question(None, "系统提示", "您确认要退出程序吗？ \n如果配置未保存，请先保存再退出！", QMessageBox.Yes | QMessageBox.No)
            if (req == QMessageBox.Yes):
                try:
                    # TODO 需要优化退出时杀死所有 QtWebEngineProcess 进程问题
                    # 查看浏览器进程
                    # self.logger.info(os.popen('tasklist /FI "IMAGENAME eq QtWebEngineProcess.exe"').read())
                    # 杀浏览器进程
                    os.system('TASKKILL /F /IM QtWebEngineProcess.exe')

                    App.mainFrame.webview.close()
                    if (App.mainFrame.twLogs):
                        App.mainFrame.twLogs.webview.close()
                except Exception as e:
                    pass

                sys.exit(0)
            else:
                return False
        else:
            sys.exit(0)


    '''状态信息 ============================'''
    def statusMsg(self, message):
        if message is not None:
            self.statusBar().showMessage(message)

    '''刷新运行日志事件'''
    def actListenersRunLogs(self, title=''):
        if(self.listeners['RunLogsTab'] is not None):
            self.listeners['RunLogsTab']()
        pass

if __name__ == '__main__':
    curPath, curFilename = os.path.split(os.path.abspath(sys.argv[0]))
    rootPath = curPath.replace("\\", "/")

    app = QApplication(sys.argv)
    App = Main()
    App.mainFrame = WinMain(App)
    App.initMain()

    app.setWindowIcon(QtGui.QIcon(':icons/images/winlogo.png'))

    try:
        if (App.login()):
            App.show()
            sys.exit(app.exec_())
    except Exception as e:
        App.closeMain()


