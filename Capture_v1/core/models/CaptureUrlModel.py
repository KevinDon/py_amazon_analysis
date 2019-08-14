from core.libs.CommonUnit import getNowTime, getFormatTime
from core.libs.MongoDbHandler import MongoDB, tableField


class CaptureUrlMode(MongoDB):
    class Meta:
        db_table = 'pub_capture_url'

    fields = dict(
        url=tableField(),
        variants=tableField(),
        url_template=tableField(),
        job_code=tableField(),
        rule_code=tableField(),
        status=tableField(default=1),
        used_at=tableField(default=''),
        created_at=tableField(default=getFormatTime(getNowTime())),
    )
