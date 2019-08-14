# coding=utf-8

import sys, subprocess, pytz, datetime
from django.db.backends.utils import logger
from django.conf import settings
from cronjob.model import CronjobLogsModel

#内部引用调用时用到
import cronjob, appfront, api, task

'''job 实例'''
class JobInstance (object):
    def __init__(self, job):
        self.job = job
        self.id = job.id
        self.code = job.code
        self.title = job.title
        self.type = job.type
        self.command = job.command
        self.command_type = job.command_type

    '''执行Job'''
    def runJob(self):
        self._begin_time = datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE))
        _status = 2
        _msg = ''
        logger.info('Run Begin Cronjob: {0} ==========='.format(self.title))
        try:
            # 系统内部程序调用
            if self.command_type == 1 or self.command_type == 3:
                if self.command is not None and self.command != '':
                    try:
                        _content = eval(self.command)
                        _status = 1
                        _msg = 'Complated Cronjob {0}: {1}'.format(self.title, _content)
                    except Exception as e:
                        _status = 3
                        _msg = 'Error Cronjob {0} : {1}'.format(self.title, e)
                else:
                    _status = 2
                    _msg ='Error Cronjob {0}: Command is null'.format(self.title)

            # 操作系统程序调用
            else:
                if self.command is not None and self.command != '':
                    try:
                        _result = self.execcmdCommand(self.command)
                        _status = 1
                        _msg = 'Complated Cronjob {0}: {1}'.format(self.title, _result)
                    except Exception as e:
                        _status = 3
                        _msg = 'Error Cronjob {0} : {1}'.format(self.title, e)
                else:
                    _status = 2
                    _msg ='Error Cronjob {0}: Command is null'.format(self.title)


            self._end_time = datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE))
            self.addCronjobLogs(job=self.job, status=_status, content=_msg, date_begin=self._begin_time, date_end=self._end_time)

            logger.info(_msg)

        except Exception as e:
            self._end_time = datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE))
            self.addCronjobLogs(job=self.job, status=3, content=e, date_begin=self._begin_time, date_end=self._end_time)
            logger.error('Error Cronjob {0}: {1}'.format(self.title, e))


    '''加入JOB执行记录'''
    def addCronjobLogs(self, job, status=1, content='', time_long= 0, process=None, thread=None, date_begin=None, date_end=None):
        _log = {
            'cronjob': job,
            'status': status,
            'task_type': job.task_type,
            'content': content,
            'process': process,
            'thread': thread,
            'time_long': (date_end - date_begin).seconds,
            'date_begin': date_begin ,
            'date_end': date_end,
        }
        CronjobLogsModel.objects.create(**_log)


    '''执行系统命令'''
    def execcmdCommand(self, command):
        stderrinfo = ''
        is_windows = (sys.platform == "win32")  # learning from 'subprocess' module
        is_linux = (sys.platform == "linux2")
        try:
            if(is_windows):
                output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,universal_newlines=True)
                stderrinfo, stdoutinfo = output.communicate()
            else:
                output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
                stderrinfo, stdoutinfo = output.communicate()

        except Exception as e:
            stderrinfo = e

        return stderrinfo