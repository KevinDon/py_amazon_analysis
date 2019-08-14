from core.libs.MongoDbHandler import MongoDB, tableField


class CaptureRequestModel(MongoDB):
    class Meta:
        db_table = 'pub_capture_request'

    fields = dict(
        target_url=tableField(),
        task_code=tableField(),
        rule_code=tableField(),
        job_code=tableField(),
        request_code=tableField(),
        status=tableField(),
        request_at=tableField(),
        response_at=tableField(),
        cost_time=tableField(),
        request_data=tableField(),
        response_data=tableField(),
    )

