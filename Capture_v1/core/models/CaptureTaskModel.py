from core.libs.CommonUnit import getNowTime, getFormatTime
from core.libs.MongoDbHandler import MongoDB, tableField


class CaptureTaskModel(MongoDB):
    class Meta:
        db_table = 'pub_capture_task'

    fields = dict(
        task_code=tableField(verbose_name='task code'),
        rule_code=tableField(verbose_name='rule code'),
        status=tableField(default=1),
        request_cursor=tableField(default=0),
        request_total=tableField(default=0),
        request_failed=tableField(default=0),
        request_slice_num=tableField(default=0),
        request_slice_cursor=tableField(default=1),
        request_success=tableField(default=0),
        slice=tableField(),
        redo=tableField(default=0),
        updated_at=tableField(default=getFormatTime(getNowTime())),
    )


class CaptureJobModel(MongoDB):
    class Meta:
        db_table = 'pub_capture_task_job'

    fields = dict(
        task_code=tableField(),
        rule_code=tableField(),
        status=tableField(default=0),
        request_cursor=tableField(default=0),
        request_total=tableField(default=0),
        request_redo=tableField(),
        request_failed=tableField(default=0),
        request_success=tableField(default=0),
        created_at=tableField(),
        finish_at=tableField(),
        cost_time=tableField(),
        updated_at=tableField(default=getFormatTime(getNowTime())),
        scrapyd_job_id=tableField(),
    )


class SyncTaskModel(MongoDB):
    class Meta:
        db_table = 'pub_sync_task'

    fields = dict(
        task_code=tableField(),
        rule_code=tableField(),
        status=tableField(default=1),
        request_api=tableField(),
        cur_page=tableField(default=1),
        end_page=tableField(default=1),
        total_row=tableField(default=1),
        created_at=tableField(),
        updated_at=tableField(default=getFormatTime(getNowTime())),
    )


class SyncJobModel(MongoDB):
    class Meta:
        db_table = 'pub_sync_task_job'

    fields = dict(
        task_code=tableField(),
        rule_code=tableField(),
        status=tableField(default=0),
        request_cursor=tableField(default=0),
        request_total=tableField(default=0),
        request_redo=tableField(),
        request_failed=tableField(default=0),
        request_success=tableField(default=0),
        created_at=tableField(),
        finish_at=tableField(),
        cost_time=tableField(),
        updated_at=tableField(default=getFormatTime(getNowTime())),
        scrapyd_job_id=tableField(),
    )
