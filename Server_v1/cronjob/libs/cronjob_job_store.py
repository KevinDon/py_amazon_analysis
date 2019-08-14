import pickle
import warnings

from apscheduler.job import Job
from apscheduler.jobstores.base import BaseJobStore, JobLookupError
from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.base import logger
from django.db import OperationalError, ProgrammingError, connections

from cronjob.libs.cronjob_func import serialize_dt, deserialize_dt
from cronjob.model import CronjobJobStoreModel


LOGGER = logger

def ignore_database_error(on_error_value=None):

    def dec(func):
        from functools import wraps

        @wraps(func)
        def inner(*a, **k):
            try:
                return func(*a, **k)
            except (OperationalError, ProgrammingError) as e:
                warnings.warn(
                    "Got OperationalError: {}. "
                    "Please, check that you have migrated the database via python manage.py migrate".format(e),
                    category=RuntimeWarning,
                    stacklevel=3
                )
                return on_error_value
        return inner
    return dec


class CronjobDbJobStore(BaseJobStore):

    """
    Stores jobs in a Django database.
    :param int pickle_protocol: pickle protocol level to use (for serialization), defaults to the
        highest available
    """

    def __init__(self, pickle_protocol=pickle.HIGHEST_PROTOCOL):
        super(CronjobDbJobStore, self).__init__()
        self.pickle_protocol = pickle_protocol

    @ignore_database_error()
    def lookup_job(self, job_id):
        LOGGER.debug("Lookup for a job %s", job_id)
        try:
            job_state = CronjobJobStoreModel.objects.get(name=job_id).job_state
        except ObjectDoesNotExist:
            return None
        r = self._reconstitute_job(job_state) if job_state else None
        LOGGER.debug("Got %s", r)
        return r

    @ignore_database_error(on_error_value=[])
    def get_due_jobs(self, now):
        LOGGER.debug("get_due_jobs for time=%s", now)
        try:
            out = self._get_jobs(next_run_time__lte=serialize_dt(now))
            LOGGER.debug("Got %s", out)
            return out
        except:
            LOGGER.exception("Exception during getting jobs")
            return []

    @ignore_database_error()
    def get_next_run_time(self):
        try:
            return deserialize_dt(CronjobJobStoreModel.objects.filter(next_run_time__isnull=False).earliest('next_run_time').next_run_time)
        except ObjectDoesNotExist:  # no active jobs
            return
        except:
            LOGGER.exception("Exception during get_next_run_time for jobs")


    @ignore_database_error(on_error_value=[])
    def get_all_jobs(self):
        jobs = self._get_jobs()
        self._fix_paused_jobs_sorting(jobs)
        return jobs

    @ignore_database_error()
    def add_job(self, job):
        import re
        from cronjob.model import CronjobModel

        cronjob_id = int(re.findall('^(ID-)(\d+):', job.id)[0][1]) if re.findall('^(ID-)(\d+):', job.id)[0][1] is not None else 0
        task_type = 0
        if (cronjob_id>0):
            cronjob = CronjobModel.objects.get(id=cronjob_id)
            task_type = cronjob.task_type

        dbJob, created = CronjobJobStoreModel.objects.get_or_create(
            defaults=dict(
                next_run_time=serialize_dt(job.next_run_time),
                job_state=pickle.dumps(job.__getstate__(), self.pickle_protocol)
            ),
            name=job.id,
            cronjob_id=cronjob_id,
            task_type=task_type
        )

        if not created:
            LOGGER.warning("Job with id %s already in jobstore. I'll refresh it", job.id)
            dbJob.next_run_time = serialize_dt(job.next_run_time)
            dbJob.job_state=pickle.dumps(job.__getstate__(), self.pickle_protocol)
            dbJob.save()

    @ignore_database_error()
    def update_job(self, job):
        updated = CronjobJobStoreModel.objects.filter(name=job.id).update(
            next_run_time=serialize_dt(job.next_run_time),
            job_state=pickle.dumps(job.__getstate__(), self.pickle_protocol)
        )

        LOGGER.debug(
            "Update job %s: next_run_time=%s, job_state=%s",
            job,
            serialize_dt(job.next_run_time),
            job.__getstate__()

        )

        if updated == 0:
            LOGGER.info("Job with id %s not found", job.id)
            raise JobLookupError(job.id)

    @ignore_database_error()
    def remove_job(self, job_id):
        qs = CronjobJobStoreModel.objects.filter(name=job_id)
        if not qs.exists():
            LOGGER.warning("Job with id %s not found. Can't remove job.", job_id)
        qs.delete()

    @ignore_database_error()
    def remove_all_jobs(self):
        with connections["default"].cursor() as c:
            c.execute("""
                DELETE FROM django_apscheduler_djangojobexecution;
            """)
            c.execute("DELETE FROM django_apscheduler_djangojob;")

    def _reconstitute_job(self, job_state):
        job_state = pickle.loads(job_state)
        job_state['jobstore'] = self
        job = Job.__new__(Job)
        job.__setstate__(job_state)
        job._scheduler = self._scheduler
        job._jobstore_alias = self._alias
        return job

    def _get_jobs(self, **filters):
        job_states = CronjobJobStoreModel.objects.filter(**filters).values_list('id', 'job_state')
        jobs = []
        failed_job_ids = set()
        for job_id, job_state in job_states:
            try:
                jobs.append(self._reconstitute_job(job_state))
            except:
                self._logger.exception('Unable to restore job "%s" -- removing it', job_id)
                failed_job_ids.add(job_id)

        # Remove all the jobs we failed to restore
        if failed_job_ids:
            LOGGER.warning("Remove bad jobs: %s", failed_job_ids)
            CronjobJobStoreModel.objects.filter(id__in=failed_job_ids).delete()

        def map_jobs(job):
            job.next_run_time = deserialize_dt(job.next_run_time)
            return job

        return list(map(map_jobs, jobs))