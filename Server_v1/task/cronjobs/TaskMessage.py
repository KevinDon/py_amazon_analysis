import datetime
import os
import django
from django.core.handlers.base import logger
import requests as req


def send():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # 你的django的settings文件
    django.setup()
    from system.model.MessageContentModel import MessageContentModel
    result = 0
    beginTime = datetime.datetime.now()
    try:
        logger.info('Begin for TaskMessage: {0}'.format(beginTime.strftime('%H:%M:%S')))
        # 获取待发送任务 @todo
        config = ''
        # 执行任务
        msg_list = MessageContentModel.objects.filter(status=2).all()[:100]
        url = 'https://oapi.dingtalk.com/robot/send?access_token='
        for msg in msg_list:
            if msg:
                token = msg.token
                title = msg.title
                text = msg.content
                msgtype = msg.sending_type if msg.sending_type is not None else "markdown"
                # text += '\n##### '+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data = {"msgtype": msgtype,
                        'markdown': {"title": title, "text": text},
                        "at": {"isAtAll": True}}
                response = req.api.post(url + token, json=data, timeout=100)
                if response.status_code == 200 and response.json()['errcode'] == 0:
                    result = result+1
                    msg.status = 1
                    msg.save()
    except Exception as e:
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))
    logger.info('End for TaskMessage: {0} s'.format((datetime.datetime.now() - beginTime).seconds))
    return result


if __name__ == '__main__':
    send()
