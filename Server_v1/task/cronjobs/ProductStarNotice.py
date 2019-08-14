import datetime
import os
import django
from django.core.handlers.base import logger
import json
from django.template import Template, Context
from task.cronjobs.util import condition_parse, get_var_data


def handle():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # 你的django的settings文件
    django.setup()
    from system.model import MessageTemplateModel, TemplateRunLogModel, MessageContentModel
    from amazon.dv import CaptureSkuReviewDv
    result = False
    beginTime = datetime.datetime.now()
    message_type = "ProductStarNotice"
    try:
        logger.info('Begin for {0}: {1}'.format(message_type, beginTime.strftime('%H:%M:%S')))
        # 获取对应模块的模板列表
        template_list = MessageTemplateModel.objects.filter(message_type=message_type, status=1)
        # 获取模板变量
        data = get_var_data(message_type)
        for template in template_list:
            # 解析业务条件
            condition = json.loads(template.condition)
            conditions = condition_parse(condition)
            # 通过条件获取业务数据
            queryset = CaptureSkuReviewDv.objects.all()
            queryset = queryset.filter(conditions)
            data_list = []
            log_list = []
            for sku in queryset:
                if TemplateRunLogModel.objects.filter(template_id=template.id, sku_buy_box_state_id=sku.id).count() > 0:
                    continue
                log_list.append(TemplateRunLogModel(template_id=template.id, sku_buy_box_state_id=sku.id))
                data_list.append(sku)
            if len(data_list) == 0:
                continue
            # 通过业务数据，模板变量，组装消息模板
            tpl = Template(template.content)
            data['data'] = data_list
            ctx = Context(data)
            text = tpl.render(ctx)
            # 创建消息
            message = MessageContentModel()
            message.title = template.describe
            message.sending_type = template.type
            message.message_type = message_type
            message.condition = str(conditions)
            message.content = text
            # 发送到模板指定的所有群
            for dt in template.dingtalk.all():
                message.group_name = dt.name
                message.token = dt.token
                message.status = 2
                message.save()
            # 写入模板运行日志
            TemplateRunLogModel.objects.bulk_create(log_list)
    except Exception as e:
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))
    logger.info('End for {0}: {1} s'.format(message_type, (datetime.datetime.now() - beginTime).seconds))
    return result


if __name__ == '__main__':
    handle()
