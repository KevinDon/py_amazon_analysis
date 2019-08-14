# coding=utf-8
import datetime, pytz, rpyc
from django.db.backends.utils import logger
from cronjob.libs.job_instance import JobInstance
from cronjob.model import CronjobModel, CronjobStateModel, CronjobConfigModel

class MySchedulers(object):
    jobs = None
    def __init__(self, parent= None):
        try:
            c_sname = CronjobConfigModel.objects.get(key='server_host').value
            c_sport = CronjobConfigModel.objects.get(key='server_port').value
            conn = rpyc.connect(c_sname if c_sname is not None else 'localhost', int(c_sport) if c_sport is not None else 12345)
            self.jobs = conn.root
            print(self.jobs)
        except Exception as e:
            logger.error('Cronjob\'s Server Error: {0}'.format(e))

    '''停止定时器'''
    def stopJob(self, job):
        result = False
        try:
            _job_id = 'ID-{0}:{1}:{2}'.format(job.id, job.code, job.title)

            if (self.jobs.get_job(_job_id)):
                self.jobs.remove_job(_job_id)
                logger.info('{0} 已经停止'.format(_job_id))
                self.addCronjobStatus(job, action=2)

                result = True
            else:
                self.addCronjobStatus(job, action=2, status=2)
                logger.error('Error Stop Cronjob {0}: {1}'.format(job.title, '任务不存在'))

        except Exception as e:
            self.addCronjobStatus(job, action=2, status=2)
            logger.error('Error Stop Cronjob {0}: {1}'.format(job.title, ''.join(e)))

        return result


    '''加入定时器'''
    def addJob(self, job):
        result = False
        try:
            _job = JobInstance(job)
            _job_id = 'ID-{0}:{1}:{2}'.format(job.id, job.code, job.title)
            print(_job_id)
            if job.type == 1:
                # 指定执行时间（仅执行一次）
                self.jobs.add_job('server:addjob', 'date'
                                  , args=[job.id]
                                  , id=_job_id
                                  , run_date= job.start_date.strftime("%Y-%m-%d %H:%M:%S")
                                  )
            else:
                # 定时重复执行
                self.jobs.add_job('server:addjob', 'cron'
                                  , args=[job.id]
                                  , id=_job_id
                                  , year=job.yr
                                  , month=job.mo
                                  , week=job.wk
                                  , day=job.dy
                                  , day_of_week=job.dy_of_week
                                  , hour=job.hr
                                  , minute=job.mi
                                  , second=job.se
                                  , start_date=job.start_date.strftime("%Y-%m-%d %H:%M:%S")
                                  , end_date=job.end_date.strftime("%Y-%m-%d %H:%M:%S")
                                  )
            # 运行启动记录
            if(self.jobs.get_job(_job_id)):
                self.addCronjobStatus(job, action=1)
                logger.info('Add Cronjob {0}'.format(job.title))
                result = True
            else:
                self.addCronjobStatus(job, action=1, status=2)
                logger.error('Error Add Cronjob {0}: {1}'.format(job.title, '启动失败'))

        except Exception as e:
            self.addCronjobStatus(job, action=1, status=2)
            logger.error('Error Add Cronjob {0}: {1}'.format(job.title, str(e)))

        return result


    def getJob(self, job):
        _job_id = 'ID-{0}:{1}:{2}'.format(job.id, job.code, job.title)
        return self.jobs.get_job(_job_id)


    def shutdown(self):
        self.jobs.shutdown()
        logger.info('===== shutdown cronjob =======')


    '''加入JOB启动记录'''
    def addCronjobStatus(self, job, action=1, status=1):
        state = {
            'cronjob': job,
            'task_type': job.task_type,
            'action': action,
            'status': status,
        }
        CronjobStateModel.objects.create(**state)



