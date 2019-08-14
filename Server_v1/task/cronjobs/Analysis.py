# coding:utf-8
import os
import django
import datetime, time
from django.core.handlers.base import logger
import re
import uuid
import sys
import subprocess

sys.path.append('.')

from django.db import connections
from django.utils import timezone

'''分析页面数据'''


def AnalysisData(ruleId):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # 你的django的settings文件
    django.setup()
    from core.libs.analysis_utils import ResultData
    from core.libs.xml_utils import XmlObject
    from rule.model import AnalysisRuleModel
    _result = False
    beginTime = datetime.datetime.now()
    try:
        logger.info('Send Command of AnalysisData: {0}'.format(beginTime.strftime('%H:%M:%S')))
        cfg = AnalysisRuleModel.objects.filter(pk=ruleId).first()
        config = XmlObject(xmlstr=cfg.xml_data)
        chunks = config.getElement("chunk").text
        table = config.getElement("table").text
        fields = config.getElement(xpath="//fields/field")
        pages_xpath = config.getElement("page").text
        model_list = []
        # 多页数据
        analysis_last_id = 0 if cfg.analysis_last_id is None else cfg.analysis_last_id
        analysis_at = timezone.now()
        analysis_code = uuid.uuid4()
        with connections['default'].cursor() as cursor:
            cursor.execute(
                'SELECT task_code,job_code,request_code,capture_code,target_url,capture_at,last_id,html FROM res_capture_html WHERE capture_code = %s AND last_id > %s ORDER BY last_id ASC limit 1000',
                [str(cfg.capture_rule.rule_code), int(analysis_last_id)])
            page_list = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
            logger.info('pages:{0} | {1}'.format(cfg.capture_rule.rule_code, len(page_list)))
            for page in range(len(page_list)):
                data = XmlObject(xmlstr=page_list[page]['html'], type="html")
                pages = [] if pages_xpath is None else data.getElement(xpath=pages_xpath)
                curr_page = 1 if len(pages) < 1 else int(pages[0])
                chunk_list = data.getElement(xpath=chunks)
                chunk_len = len(chunk_list)
                # 多模块数据
                for idx, chunk in enumerate(chunk_list):
                    if page_list[page]['last_id'] == '' or page_list[page]['last_id'] is None:
                        continue
                    # 公共字段，非业务数据
                    model = {'capture_at': page_list[page]['capture_at'], 'target_url': page_list[page]['target_url'],
                             'task_code': page_list[page]['task_code'], 'capture_code': page_list[page]['capture_code'],
                             'job_code': page_list[page]['job_code'], 'request_code': page_list[page]['request_code'],
                             'analysis_code': analysis_code, 'analysis_at': str(analysis_at),
                             'last_id': int(page_list[page]['last_id'])}
                    analysis_last_id = analysis_last_id if int(page_list[page]['last_id']) < analysis_last_id else int(
                        page_list[page]['last_id'])
                    passed = True
                    # 每条数据字段列表
                    for field in fields:
                        name = field.findtext('./name')
                        mode = field.findtext('./mode')
                        position = field.findtext('./position')
                        position_group = field.findtext('./position-group')
                        pattern_group = field.findtext('./pattern-group')
                        value_set = field.xpath('./value-set/mapper/item')
                        pattern = field.findtext('./pattern')
                        required = field.findtext('./required')
                        default = field.findtext('./default')
                        value_list = [] if position == '' else chunk.xpath(position)
                        position_group = int(position_group)
                        pattern_group = int(pattern_group)
                        values = [] if len(value_set) == 0 else [v.findtext("./value") for v in value_set]
                        model[name] = ''
                        if mode == '2' and len(value_list) == 0:  # 节点不存在
                            model[name] = '2' if len(values) <= 1 else values[1]
                        elif mode == '2' and len(value_list) > 0:  # 节点存在
                            model[name] = '1' if len(values) <= 1 else values[0]
                        elif mode == '3':  # 判断节点数
                            index = (curr_page - 1) * chunk_len + idx + 1
                            model[name] = index if len(values) <= index else values[int(index)]
                        else:  # 匹配节点值
                            if len(value_list) > 0:
                                target = "" if len(value_list) <= position_group else str(
                                    value_list[position_group]).strip()
                                rs = re.compile(r'{}'.format(pattern), re.DOTALL).search(target)
                                model[name] = "" if rs is None else rs[pattern_group]
                        if required == '1' and model[name] == '':
                            passed = False
                            continue
                        if model[name] == '':
                            model[name] = default
                    if passed:
                        model_list.append(model)
            # model_list.append(CaptureSkuBuyBoxStateModel(**model))
        # CaptureSkuBuyBoxStateModel.objects.bulk_create(model_list)
        logger.info('records:{0}, times:{1} s'.format(len(model_list), (datetime.datetime.now() - beginTime).seconds))
        if len(model_list) > 0:
            # 批量写入
            n = 10000
            m_list = [model_list[i:i + n] for i in range(0, len(model_list), n)]
            res = ResultData(table, fields=tuple(model_list[0].keys()))
            for ml in m_list:
                res.createInsert(values=[v.values() for v in ml])
            from django.db import transaction
            with transaction.atomic():
                _result = res.executeInsert()
                AnalysisRuleModel.objects.filter(pk=cfg.id).update(analysis_at=analysis_at,
                                                                   analysis_last_id=analysis_last_id)
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))
    logger.info('End for send command of AnalysisData: {0} s'.format((datetime.datetime.now() - beginTime).seconds))
    return _result

    '''执行系统命令'''


def execcmdCommand(command):
    stderrinfo = ''
    is_windows = (sys.platform == "win32")  # learning from 'subprocess' module
    is_linux = (sys.platform == "linux2")
    try:
        if (is_windows):
            output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                                      universal_newlines=True)
            stderrinfo, stdoutinfo = output.communicate()
        else:
            output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                                      universal_newlines=True)
            stderrinfo, stdoutinfo = output.communicate()

    except Exception as e:
        stderrinfo = e

    return stderrinfo

    '''触发kettle同步数据'''


def AsyncCapture():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # 你的django的settings文件
    django.setup()
    from system.model import ServerConfigModel
    server_list = ServerConfigModel.objects.all()
    for sever in server_list:
        if sever.server_status.running_status != 1:
            continue
        try:
            _result = execcmdCommand(
                '/var/www/html/amazon_analysis_v1/amazon/cronjobs/job_amazon_sync_capturc_data.sh ' + sever.ip)
            logger.info('result:{0} | {1}'.format(sever.ip, _result))
        except Exception as e:
            logger.error('faild:{0} | {1}'.format(sever.ip, e))
    logger.info('done')


if __name__ == '__main__':
    # transferKeyword(3)
    # transferBestseller(1)
    # transferPrice(4)
    # transferReview(5)
    # transferBuybox(2)
    AnalysisData(3)
    # AsyncCapture()
