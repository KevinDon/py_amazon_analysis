# coding:utf-8
from app.lib.db import *


class Config(object):
    def __init__(self):
        try:
            self.version = DbConfig().get(main_key='system', minor_key='version')
        except Exception as e:
            self.version = DbConfig()
            self.version.name='System Version'
            self.version.main_key='system'
            self.version.minor_key='version'
            self.version.type=1
            self.version.sort=0

        try:
            self.leDbHost = DbConfig().get(main_key='setting', minor_key='leDbHost')
        except Exception as e:
            self.leDbHost = DbConfig()
            self.leDbHost.name = 'Database Host'
            self.leDbHost.main_key = 'setting'
            self.leDbHost.minor_key = 'leDbHost'
            self.leDbHost.type = 1
            self.leDbHost.sort = 2

        try:
            self.leDbPort = DbConfig().get(main_key='setting', minor_key='leDbPort')
        except Exception as e:
            self.leDbPort = DbConfig()
            self.leDbPort.name = 'Database Port'
            self.leDbPort.main_key = 'setting'
            self.leDbPort.minor_key = 'leDbPort'
            self.leDbPort.type = 1
            self.leDbPort.sort = 3

        try:
            self.leDbName = DbConfig().get(main_key='setting', minor_key='leDbName')
        except Exception as e:
            self.leDbName = DbConfig()
            self.leDbName.name = 'Database Name'
            self.leDbName.main_key = 'setting'
            self.leDbName.minor_key = 'leDbName'
            self.leDbName.type = 1
            self.leDbName.sort = 4

        try:
            self.leDbUsername = DbConfig().get(main_key='setting', minor_key='leDbUsername')
        except Exception as e:
            self.leDbUsername = DbConfig()
            self.leDbUsername.name = 'Database Username'
            self.leDbUsername.main_key = 'setting'
            self.leDbUsername.minor_key = 'leDbUsername'
            self.leDbUsername.type = 1
            self.leDbUsername.sort = 5

        try:
            self.leDbPassword = DbConfig().get(main_key='setting', minor_key='leDbPassword')
        except Exception as e:
            self.leDbPassword = DbConfig()
            self.leDbPassword.name = 'Database Password'
            self.leDbPassword.main_key = 'setting'
            self.leDbPassword.minor_key = 'leDbPassword'
            self.leDbPassword.type = 1
            self.leDbPassword.sort = 6

        try:
            self.language = DbConfig().get(main_key='user', minor_key='language')
        except Exception as e:
            self.language = DbConfig()
            self.language.name = 'User Language'
            self.language.main_key = 'user'
            self.language.minor_key = 'language'
            self.language.type = 2
            self.language.sort = 2

        try:
            self.leServiceUrl = DbConfig().get(main_key='setting', minor_key='leServiceUrl')
        except Exception as e:
            self.leServiceUrl = DbConfig()
            self.leServiceUrl.name='Service URL'
            self.leServiceUrl.main_key='setting'
            self.leServiceUrl.minor_key='leServiceUrl'
            self.leServiceUrl.type=1
            self.leServiceUrl.sort=1