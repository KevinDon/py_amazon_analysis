# coding:utf-8
import os
import types

import datetime, re
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QUrl, QCoreApplication, QByteArray
from PyQt5.QtWebEngineCore import QWebEngineHttpRequest
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu
from PyQt5.QtNetwork import QNetworkCookie

from app.lib.WebEngineView import WebEngineView
from app.lib.logger import Log
from app.model.dao.DbPlusin import DbPlusIn
from app.model.dao.DbPlusinFunction import DbPlusInFunction
from app.view.widgetWeb import Ui_WebForm


class WidgetWeb(QWidget, Ui_WebForm):
    _ = QCoreApplication.translate

    def __init__(self, mainWin, keyCode):
        super(WidgetWeb, self).__init__()
        self.mainWin = mainWin
        self.myWidget = QWidget()
        self.log = Log('info')
        self.setupUi(self.myWidget)
        self.canMoveView = False

        self.loadBegin = datetime.datetime.now()
        self.loadEnd = datetime.datetime.now()
        self.loginCount = 0

        # 定义二级对象动态元素
        self.labelFields = []
        self.leFields = []
        self.tbGos = []
        self.pbGos = []
        self.actBtDynamicClicked = []

        self.labelField.setHidden(True)
        self.leField.setHidden(True)
        self.tbGo.setHidden(True)
        self.pbGo.setHidden(True)


        # 浏览器设置WebView
        self.webview = WebEngineView(self.mainWin)
        self.widgetContentVL.addWidget(self.webview)

        # 右键菜单
        self.webview.setContextMenuPolicy(Qt.CustomContextMenu)
        self.webview.customContextMenuRequested.connect(self.webviewGenerateMenu)
        self.webview.setMouseTracking(True)
        self.webview.setTabletTracking(True)
        self.webview.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.webview.setAcceptDrops(True)
        # self.webview.createWindow(self.mainWin, QWebEnginePage.OpenLinkInThisWindow)

        self.plusin = DbPlusIn().get(code = keyCode )
        if(self.plusin.id >0 ):
            self.myWidget.setWindowTitle(self.plusin.title_en)
            self.plusinFunction = DbPlusInFunction().select().where(DbPlusInFunction.fid == self.plusin.id).order_by(DbPlusInFunction.sort.asc())
        else:
            self.plusinFunction = None

        self.initFields()

        # 公用按钮
        self.tbRefresh.clicked.connect(self.actTbRefresh)
        self.tbGoBack.clicked.connect(self.actTbGoBack)
        self.tbRedo.clicked.connect(self.actTbRedo)
        self.tbStop.clicked.connect(self.actTbStop)
        self.tbSide.clicked.connect(self.actTbSide)

        # 初始化布局
        self.setLayout(self.myWidget.layout())

    '''Webview右键菜单'''
    def webviewGenerateMenu(self, pos):
        menu = QMenu()
        refresh = menu.addAction(self._("WebForm", "Refresh"))
        refresh.setIcon(QtGui.QIcon(':/button/images/button/refresh.png'))
        goback = menu.addAction(self._("WebForm", "Go Back"))
        goback.setIcon(QtGui.QIcon(':/button/images/button/back.png'))
        redo = menu.addAction(self._("WebForm", "Forward"))
        redo.setIcon(QtGui.QIcon(':/button/images/button/redo.png'))
        stop = menu.addAction(self._("WebForm", "Stop"))
        stop.setIcon(QtGui.QIcon(':/button/images/button/clear.png'))
        if(self.widgetNav.isHidden()):
            side = menu.addAction(self._("WebForm", "Extend"))
            side.setIcon(QtGui.QIcon(':/button/images/button/right.gif'))
        else:
            side = menu.addAction(self._("WebForm", "Collapse"))
            side.setIcon(QtGui.QIcon(':/button/images/button/left.gif'))
        action = menu.exec_(self.webview.mapToGlobal(pos))
        if action == refresh:
            self.actTbRefresh()
        elif action == goback:
            self.actTbGoBack()
        elif action == redo:
            self.actTbRedo()
        elif action == stop:
            self.actTbStop()
        elif action == side:
            self.actTbSide()
        else:
            return
        pass


    '''刷新Webview'''
    def actTbRefresh(self):
        self.webview.reload()

        pass

    '''回退Webview'''
    def actTbGoBack(self):
        self.webview.back()
        pass

    '''前进Webview'''
    def actTbRedo(self):
        self.webview.forward()
        pass

    '''停止Webview'''
    def actTbStop(self):
        self.webview.stop()
        pass

    '''收缩左侧栏'''
    def actTbSide(self):
        if(self.widgetNav.isHidden()):
            self.tbSide.setToolTip(self._("WebForm", "Collapse"))
            self.widgetNav.show()
        else:
            self.tbSide.setToolTip(self._("WebForm", "Extend"))
            self.widgetNav.hide()
        pass


    '''关闭webview链接'''
    def hideEvent(self, QHideEvent):
        self.webview.close()

    '''显示webview'''
    def showEvent(self, QShowEvent):
        self.webview.show()

    '''初始化配置'''
    def initFields(self):
        # 动态动作类 BEGIN ========================
        class ActBtDynamic:
            def __init__(self, mainWin, webview):
                self.plusIn = DbPlusIn()
                self.plusInFunction = DbPlusInFunction()
                self.objValue = object
                self.app = mainWin
                self.webview = webview
                pass

            def ActMethon(self):
                if (self.plusInFunction != None):
                    try:
                        _url = ''

                        # 主路径
                        mainUrl = '{0}://{1}'.format(self.plusIn.protocol, self.plusIn.url)
                        _temp = re.search('(\{account\})+', mainUrl)
                        if (_temp != None and len(_temp.groups()) > 0): mainUrl = re.sub('(\{account\})+', self.plusIn.account, mainUrl)
                        _temp = re.search('(\{password\})+', mainUrl)
                        if (_temp != None and len(_temp.groups()) > 0): mainUrl = re.sub('(\{password\})+', self.plusIn.password, mainUrl)

                        # 子路径
                        if (self.plusInFunction.is_path == 1):
                            # 局部子路径
                            subUrl = '{0}/{1}'.format(mainUrl, self.plusInFunction.url)
                        else:
                            # 完整子路径
                            subUrl = '{0}://{1}'.format(self.plusIn.protocol, self.plusInFunction.url)

                        # 替换子路径中的账号及密码
                        _temp = re.search('(\{account\})+', subUrl)
                        if (_temp != None and len(_temp.groups()) > 0): subUrl = re.sub('(\{account\})+', self.plusIn.account, subUrl)
                        _temp = re.search('(\{password\})+', subUrl)
                        if (_temp != None and len(_temp.groups()) > 0): subUrl = re.sub('(\{password\})+', self.plusIn.password, subUrl)

                        # 如果是搜索类型路径
                        if (self.plusInFunction.field_type == 2):
                            _temp = re.search('(\{.*?\})+', subUrl)
                            if (_temp != None and len(_temp.groups()) > 0):
                                # 需要正则匹配的路径
                                _url = QUrl(re.sub('(\{'+self.plusInFunction.field+'\})+', self.objValue.text(), subUrl))

                            else:
                                _url = QUrl('{0}?{1}={2}'.format(subUrl, self.plusInFunction.field, self.objValue.text()))

                        if(_url == ''): _url = QUrl(subUrl)
                        if (_url == ''): _url = QUrl(mainUrl)

                        req = QWebEngineHttpRequest()
                        req.setUrl(_url)
                        if (self.plusInFunction.method == 'get'):
                            req.setMethod(QWebEngineHttpRequest.Get)
                        else:
                            req.setMethod(QWebEngineHttpRequest.Post)


                        self.webview.load(req)

                        # self.app.log.info(_url)
                        pass

                    except Exception as e:
                        self.app.log.info(e)
                        QMessageBox.information(None, self._("sscode", "Run Error"), e, QMessageBox.Yes)
                else:
                    QMessageBox.information(self, '操作提示', ' 动作配置有误', QMessageBox.Yes)
                # 动态动作类 END ========================

        try:

            # 首页
            mainUrl = '{0}://{1}'.format(self.plusin.protocol, self.plusin.url)
            _temp = re.search('(\{account\})+', mainUrl)
            if (_temp != None and len(_temp.groups()) > 0): mainUrl = re.sub('(\{account\})+', self.plusin.account, mainUrl)
            _temp = re.search('(\{password\})+', mainUrl)
            if (_temp != None and len(_temp.groups()) > 0): mainUrl = re.sub('(\{password\})+', self.plusin.password, mainUrl)

            req = QWebEngineHttpRequest()
            req.setUrl(QUrl(mainUrl))
            if(self.plusin.method == 'get'):
                req.setMethod(QWebEngineHttpRequest.Get)
            else:
                req.setMethod(QWebEngineHttpRequest.Post)
            self.webview.load(req)
            # cookie token
            self.webview.page().profile().defaultProfile().cookieStore().setCookie(
                QNetworkCookie(QByteArray("token".encode()), QByteArray(self.mainWin.app.token.encode())), QUrl(mainUrl))
            # auto login
            self.webview.page().loadFinished.connect(self.sendLoginInfo)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/button/images/svg/angle-right-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            if(self.plusinFunction and len(self.plusinFunction)>0):
                lineRows = 5
                for index in range(len(self.plusinFunction)):

                    # 动态方法 Begin ===============
                    def setActMethon(self, plusin, plusinFunction, objValue):
                        self.plusIn = plusin
                        self.plusInFunction = plusinFunction
                        self.objValue = objValue

                    _act = ActBtDynamic(self, self.webview)
                    _act.setActMethon = types.MethodType(setActMethon, _act)
                    # 动态方法 End ===============

                    if(self.plusinFunction[index].field_type == 2):
                        self.labelFields.append(QtWidgets.QLabel(self.widgetNav))
                        self.labelFields[index].setFrameShape(QtWidgets.QFrame.NoFrame)
                        self.labelFields[index].setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.labelFields[index].setObjectName("labelField_{0}".format(index))
                        if(self.mainWin.app.configs.language.value == '简体中文'):
                            self.labelFields[index].setText("{0}".format(self.plusinFunction[index].title_cn))
                        else:
                            self.labelFields[index].setText("{0}".format(self.plusinFunction[index].title_en))
                        self.formLayout.setWidget(lineRows, QtWidgets.QFormLayout.SpanningRole, self.labelFields[index])
                        lineRows += 1

                        self.leFields.append(QtWidgets.QLineEdit(self.widgetNav))
                        self.leFields[index].setObjectName("leField_{0}".format(index))
                        self.leFields[index].setFrame(True)
                        self.leFields[index].setClearButtonEnabled(True)
                        # 动作信号绑定
                        _act.setActMethon(self.plusin, self.plusinFunction[index], self.leFields[index])
                        self.actBtDynamicClicked.append(_act)
                        self.leFields[index].returnPressed.connect(self.actBtDynamicClicked[index].ActMethon)
                        self.formLayout.setWidget(lineRows, QtWidgets.QFormLayout.LabelRole, self.leFields[index])

                        self.tbGos.append(QtWidgets.QToolButton(self.widgetNav))
                        self.tbGos[index].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                        self.tbGos[index].setText("")
                        self.tbGos[index].setIcon(icon)
                        self.tbGos[index].setPopupMode(QtWidgets.QToolButton.InstantPopup)
                        self.tbGos[index].setAutoRaise(True)
                        self.tbGos[index].setObjectName("tbGo_{0}".format(index))
                        self.tbGos[index].setToolTip(self._("WebForm", "Go"))
                        self.formLayout.setWidget(lineRows, QtWidgets.QFormLayout.FieldRole, self.tbGos[index])
                        # 动作信号绑定
                        self.tbGos[index].clicked.connect(self.actBtDynamicClicked[index].ActMethon)
                        lineRows += 1

                        self.pbGos.append('')
                    else:
                        self.pbGos.append(QtWidgets.QPushButton(self.widgetNav))
                        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                        sizePolicy.setHorizontalStretch(0)
                        sizePolicy.setVerticalStretch(0)
                        sizePolicy.setHeightForWidth(self.pbGos[index].sizePolicy().hasHeightForWidth())
                        self.pbGos[index].setSizePolicy(sizePolicy)
                        self.pbGos[index].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                        self.pbGos[index].setIcon(icon)
                        self.pbGos[index].setAutoDefault(False)
                        self.pbGos[index].setDefault(True)
                        self.pbGos[index].setFlat(True)
                        self.pbGos[index].setObjectName("pbGo_{0}".format(index))
                        if (self.mainWin.app.configs.language.value == '简体中文'):
                            self.pbGos[index].setText("{0}".format(self.plusinFunction[index].title_cn))
                        else:
                            self.pbGos[index].setText("{0}".format(self.plusinFunction[index].title_en))
                        self.formLayout.setWidget(lineRows, QtWidgets.QFormLayout.SpanningRole, self.pbGos[index])
                        # 菜单动作信号绑定
                        _act.setActMethon(self.plusin, self.plusinFunction[index], None)
                        self.actBtDynamicClicked.append(_act)
                        self.pbGos[index].clicked.connect(self.actBtDynamicClicked[index].ActMethon)

                        lineRows += 1

                        self.labelFields.append('')
                        self.leFields.append('')
                        self.tbGos.append('')

            else:
                self.widgetNav.close()

        except Exception as e:
            print(e)

        self.widgetNav.update()

        pass

    '''发送3次登录请求'''
    def sendLoginInfo(self):
        if (self.loginCount<3 and self.plusin.javascript and self.plusin.account):
            js = self.plusin.javascript.replace('{account}', self.plusin.account)
            js = js.replace('{password}', self.plusin.password)
            self.webview.page().runJavaScript(js)
            self.loginCount += 1