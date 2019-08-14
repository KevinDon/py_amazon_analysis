# coding=utf-8
import datetime
import os

from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings


class WebEngineView(QWebEngineView):
    # 子页表
    browseList = []
    # 下载项列表
    downloadList = []

    '''构造函数'''
    def __init__(self, mainwindow, parent=None):
        super(WebEngineView, self).__init__(parent)
        # 页面加载的开始时间
        self.loadBegin = datetime.datetime.now()
        # 页面加载结束的时间
        self.loadEnd = datetime.datetime.now()
        self.curTabIndex = -1
        self.newWebview = None
        # print(self)

        # 设置缓存路径
        self.webCachePath = '{0}/var/webcache'.format(mainwindow.app.curPath)
        self.webStoragePath = '{0}/var/webstorage'.format(mainwindow.app.curPath)
        self.webDownloadPath = '{0}/var/download'.format(mainwindow.app.curPath)
        if (not os.path.exists(self.webCachePath)): os.mkdir(self.webCachePath)
        if (not os.path.exists(self.webStoragePath)): os.mkdir(self.webStoragePath)
        if (not os.path.exists(self.webDownloadPath)): os.mkdir(self.webDownloadPath)
        self.page().profile().setCachePath(self.webCachePath)
        self.page().profile().setPersistentStoragePath(self.webStoragePath)
        # 清除缓存
        # self.page().profile().clearAllVisitedLinks()
        # self.page().profile().removeAllUrlSchemeHandlers()

        self.mainwindow = mainwindow

        #设置浏览器属性
        self.settings().setAttribute(QWebEngineSettings.AutoLoadImages, True)
        self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)  # 支持视频播放

        self.page().windowCloseRequested.connect(self.on_windowCloseRequested)  # 页面关闭请求

        # URL改变
        # self.urlChanged.connect(self.actUrlChanged)
        self.loadStarted.connect(self.actLoadStarted)
        self.loadProgress.connect(self.actLoadProgress)
        self.loadFinished.connect(self.actLoadFinished)

        # 绑定cookie被添加的信号槽
        # self.cookies = {}  # 存放cookie字典
        # self.page().profile().defaultProfile().cookieStore().cookieAdded.connect(self.onCookieAdd)
        pass

    '''url更换时'''
    def actUrlChanged(self, url):
        print(url)

    ''' cookie 设置'''
    def onCookieAdd(self, cookie):  # 处理cookie添加的事件
        name = cookie.name().data().decode('utf-8')  # 先获取cookie的名字，再把编码处理一下
        value = cookie.value().data().decode('utf-8')  # 先获取cookie值，再把编码处理一下
        self.cookies[name] = value  # 将cookie保存到字典里

    '''获取cookie'''
    def getCookie(self):
        cookie_str = ''
        for key, value in self.cookies.items():  # 遍历字典
            cookie_str += (key + '=' + value + ';')  # 将键值对拿出来拼接一下

        return cookie_str  # 返回拼接好的字符串

    '''设置 cookie 项'''
    def setCookie(self, name, value, expire=0):
        self.cookies[name] = value

    '''关闭浏览器'''
    def close(self):
        try:
            self.browseList.clear()
            self.destroy()
            # print(self.newWebview)
        except Exception as e:
            print(e)

    '''重写createWindow'''
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView(self.mainwindow)
        try:
            self.curTabIndex = self.mainwindow.createTab(new_webview)
            new_webview.loadStarted.connect(self.actLoadStarted)
            new_webview.loadFinished.connect(self.actLoadFinished)
            new_webview.page().profile().downloadRequested.connect(self.on_downloadRequested)  # 页面文件下载请求
            self.newWebview = new_webview
            # self.browseList.append(new_webview)
        except Exception as e:
            print(e)
        return new_webview


    '''支持页面关闭请求'''
    def on_windowCloseRequested(self):
        the_index = self.mainwindow.tabWidget.currentIndex()
        self.mainwindow.tabWidget.removeTab(the_index)

    '''支持页面下载按钮'''
    def on_downloadRequested(self, downloadItem):
        if (downloadItem.isFinished() == False and downloadItem.state() == 0):
            try:
                ###生成文件存储地址
                the_filename = downloadItem.url().fileName()
                if len(the_filename) == 0 or "." not in the_filename:
                    cur_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                    the_filename = "下载文件_" + cur_time + ".xls"
                the_sourceFile = os.path.join(self.webDownloadPath, the_filename)

                self.mainwindow.statusMsg('文件下载中... {0}'.format(the_filename))

                ###下载文件
                downloadItem.setPath(the_sourceFile)
                downloadItem.accept()
                downloadItem.downloadProgress.connect(self.on_downloadProgress)
                downloadItem.finished.connect(self.on_downloadFinished)
            except Exception as e:
                print(e)

    '''下载结束触发函数'''
    def on_downloadFinished(self):
        js_string = 'alert("下载成功，请到 {0} 查找下载文件！");'.format(self.webDownloadPath.replace('\\','/'))
        self.mainwindow.statusMsg('文件下载完成.')
        self.page().runJavaScript(js_string)

    '''文件下载进度'''
    def on_downloadProgress(self, number, totalnumber):
        try:
            self.mainwindow.statusMsg('文件下载中... {0}%'.format(round(float(number/totalnumber), 4) * 100 ))
        except Exception as e:
            print(e)
        # print('{0}/{1}'.format(number, totalnumber))

    '''开始加载'''
    def actLoadStarted(self):
        try:
            self.loadBegin = datetime.datetime.now()
            if (self.curTabIndex > -1):
                self.mainwindow.tabWidget.setTabText(self.curTabIndex, '加载中...')
            self.mainwindow.statusMsg('加载中...')

        except Exception as e:
            print(e)

    '''完成加载'''
    def actLoadFinished(self):
        try:
            self.loadEnd = datetime.datetime.now()
            if(self.curTabIndex>-1):
                _title = self.newWebview.title()
                if(len(_title)>17):
                    self.mainwindow.tabWidget.setTabToolTip(self.curTabIndex, _title)
                    _title = _title[0:15] + '...'
                self.mainwindow.tabWidget.setTabText(self.curTabIndex, _title)
                self.mainwindow.tabWidget.setTabIcon(self.curTabIndex, self.newWebview.icon())

            self.mainwindow.statusMsg("加载完成! {}".format(self.loadEnd - self.loadBegin))
            self.mainwindow.progressBarHide()

        except Exception as e:
            print(e)

    '''页面加载进度'''
    def actLoadProgress(self, number):
        try:
            self.mainwindow.progressBarShow( curNumber= number)
            self.mainwindow.statusMsg('加载中... {0}%'.format(number))
        except Exception as e:
            print(e)

