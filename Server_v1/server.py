#!/usr/bin/env python
# coding=utf-8

import rpyc, os, sys
import django
from rpyc.utils.server import ThreadedServer
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc

def addjob(set_id):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    django.setup()
    from cronjob.libs.job_instance import JobInstance
    from cronjob.model import CronjobModel, CronjobJobStoreModel
    job = CronjobModel.objects.get(id = set_id)
    _job = JobInstance(job)
    _job.runJob()


class SchedulerService(rpyc.Service):
    def exposed_add_job(self, func, *args, **kwargs):
        from cronjob.model import CronjobModel, CronjobJobStoreModel
        job = scheduler.add_job(func, *args, **kwargs)
        return job

    def exposed_modify_job(self, job_id, jobstore=None, **changes):
        return scheduler.modify_job(job_id, jobstore, **changes)

    def exposed_reschedule_job(self, job_id, jobstore=None, trigger=None, **trigger_args):
        return scheduler.reschedule_job(job_id, jobstore, trigger, **trigger_args)

    def exposed_pause_job(self, job_id, jobstore=None):
        return scheduler.pause_job(job_id, jobstore)

    def exposed_resume_job(self, job_id, jobstore=None):
        return scheduler.resume_job(job_id, jobstore)

    def exposed_remove_job(self, job_id, jobstore=None):
        scheduler.remove_job(job_id, jobstore)

    def exposed_get_job(self, job_id):
        return scheduler.get_job(job_id)

    def exposed_get_jobs(self, jobstore=None):
        return scheduler.get_jobs(jobstore)

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    django.setup()
    from cronjob.libs.cronjob_job_store import CronjobDbJobStore
    from cronjob.model import CronjobModel, CronjobConfigModel

    c_pt = CronjobConfigModel.objects.get(key='pool_thread').value
    c_pp = CronjobConfigModel.objects.get(key='pool_process').value
    c_jc = CronjobConfigModel.objects.get(key='job_coalesce').value
    c_jmi = CronjobConfigModel.objects.get(key='job_max_instances').value
    c_mgt = CronjobConfigModel.objects.get(key='misfire_grace_time').value

    executors = {
        'default': ThreadPoolExecutor(c_pt if c_pt is not None else 10),
        'processpool': ProcessPoolExecutor(c_pp if c_pp is not None else 5)
    }
    job_defaults = {
        'coalesce': True if c_jc == 'True' else False,
        'max_instances': False if c_jmi is not None and c_jmi == 'False' else 1000,
        'misfire_grace_time': c_mgt if c_mgt is not None else 3000  #600秒的任务超时容错
    }
    scheduler = BackgroundScheduler(executors=executors, job_defaults=job_defaults, timezone=utc)
    scheduler.add_jobstore(CronjobDbJobStore(), "default")
    scheduler.start()
    print(scheduler.get_jobs())

    protocol_config = {'allow_public_attrs': True}
    c_sport = CronjobConfigModel.objects.get(key='server_port').value
    server = ThreadedServer(SchedulerService, port=int(c_sport) if c_sport is not None else 12345, protocol_config=protocol_config)
    try:
        server.start()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        scheduler.shutdown()