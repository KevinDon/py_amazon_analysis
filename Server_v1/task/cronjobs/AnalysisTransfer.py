# coding:utf-8
import os
import django
import datetime
from django.core.handlers.base import logger
from django.db import connections
from django.utils import timezone
import sys

sys.path.append('.')

'''同步关键词排名'''


def transferKeyword(ruleId):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # 你的django的settings文件
    django.setup()
    from amazon.model import CaptureSkuKeywordRankModel, SkuKeywordModel, AmazonProductCategoryModel
    from appfront.model import ProductAsinModel
    from rule.model import AnalysisRuleModel
    _result = False
    beginTime = datetime.datetime.now()
    try:
        logger.info('Send Command of TransferData: {0}'.format(beginTime.strftime('%H:%M:%S')))
        cfg = AnalysisRuleModel.objects.filter(pk=ruleId).first()
        sync_last_id = 0 if cfg.sync_last_id is None else int(cfg.sync_last_id)
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT * FROM analysis_product_keyword WHERE capture_code = %s AND id > %s ORDER BY id ASC limit 10000",
                           [str(cfg.capture_rule.rule_code), sync_last_id])
            rows = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
            asins = set()
            keywords = set()
            categorys = set()
            for row in rows:
                asins.add(row['asin'])
                keywords.add(row['keyword'])
                categorys.add(row['category_id'])
            product_list = ProductAsinModel.objects.filter(asin__in=asins).values_list('asin', 'combine_type', 'sku')
            keyword_list = SkuKeywordModel.objects.filter(title__in=keywords).values_list('title', 'id')
            category_list = AmazonProductCategoryModel.objects.filter(code__in=categorys).values_list('code', 'id')
            sku_map = {}
            for i in product_list:
                if sku_map.get(i[0]) is None:
                    sku_map[i[0]] = i
                elif int(sku_map[i[0]][1]) > int(i[1]):
                    sku_map[i[0]] = i
            keyword_map = {}
            for i in keyword_list:
                keyword_map[i[0]] = i[1]
            category_map = {}
            for i in category_list:
                category_map[i[0]] = i[1]
            data_list = []
            logger.info('rows:{}'.format(len(rows)))
            sync_at = timezone.now()
            for row in rows:
                if sku_map.get(row['asin']) is None or keyword_map.get(row['keyword']) is None:
                    continue
                sku = sku_map.get(row['asin'])[2]
                keyword_id = keyword_map.get(row['keyword'], '')
                category_id = category_map.get(row['category_id'], 1)
                category_title = 'All Category' if row['category_name'] == '' else row['category_name']
                rank_page = 5 if row['page'] == '' or row['page'] == 'None' else int(row['page'])
                data = {'platform': 'amazon', 'sku': sku, 'asin': row['asin'], 'keyword': row['keyword'],
                        'capture_at': row['capture_at'], 'rank_on': int(row['rank_on']),
                        'rank_page': rank_page, 'category_id': category_id, 'category_title': category_title,
                        'sku_keyword_id': keyword_id}
                data_list.append(CaptureSkuKeywordRankModel(**data))
                sync_last_id = sync_last_id if int(row['id']) < sync_last_id else int(row['id'])
            logger.info(
                'records:{0}, times:{1} s'.format(len(data_list), (datetime.datetime.now() - beginTime).seconds))
            if len(data_list) > 0:
                from django.db import transaction
                with transaction.atomic():
                    AnalysisRuleModel.objects.filter(pk=cfg.id).update(sync_at=sync_at, sync_last_id=sync_last_id)
                    # 批量写入
                    n = 1000
                    m_list = [data_list[i:i + n] for i in range(0, len(data_list), n)]
                    for m in m_list:
                        CaptureSkuKeywordRankModel.objects.bulk_create(m)
                    logger.info('records:{0}, times:{1} s'.format(len(data_list),
                                                                  (datetime.datetime.now() - beginTime).seconds))
                    cursor.execute(
                        'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_keyword_rank_day;'
                        'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_keyword_rank_month;'
                        'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_keyword_rank_week;'
                    )
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))
    logger.info('End for send command of TransferData: {0} s'.format((datetime.datetime.now() - beginTime).seconds))
    return _result


'''同步购物车占用状态'''


def transferBuybox(ruleId):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # 你的django的settings文件
    django.setup()
    from amazon.model import CaptureSkuBuyBoxStateModel
    from appfront.model import ProductAsinModel
    from rule.model import AnalysisRuleModel
    _result = False
    beginTime = datetime.datetime.now()
    try:
        logger.info('Send Command of TransferData: {0}'.format(beginTime.strftime('%H:%M:%S')))
        cfg = AnalysisRuleModel.objects.filter(pk=ruleId).first()
        sync_last_id = 0 if cfg.sync_last_id is None else int(cfg.sync_last_id)
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT * FROM analysis_product_buybox WHERE capture_code = %s AND id > %s ORDER BY id ASC limit 10000",
                           [str(cfg.capture_rule.rule_code), sync_last_id])
            rows = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
            asins = set()
            for row in rows:
                asins.add(row['asin'])
            product_list = ProductAsinModel.objects.filter(asin__in=asins).values_list('asin', 'combine_type', 'sku')
            sku_map = {}
            for i in product_list:
                if sku_map.get(i[0]) is None:
                    sku_map[i[0]] = i
                elif int(sku_map[i[0]][1]) > int(i[1]):
                    sku_map[i[0]] = i
            data_list = []
            logger.info('rows:{}'.format(len(rows)))
            sync_at = timezone.now()
            for row in rows:
                sold_by_price = 0 if row['sold_by_price'] == '' else float(row['sold_by_price'])
                sold_by_price = sold_by_price if row['sold_by_price_buybox'] == '' else float(
                    row['sold_by_price_buybox'])
                sold_by = '' if row['sold_by'] == '' else row['sold_by']
                sold_by = sold_by if row['sold_by_buybox'] == '' else row['sold_by_buybox']
                if sku_map.get(row['asin']) is None or sold_by_price <= 0:
                    continue
                sku = sku_map.get(row['asin'])[2]
                if sold_by in ['Artiss Furnishings']:
                    buy_box_state = 2
                else:
                    buy_box_state = 1
                data = {'platform': 'amazon', 'sku': sku, 'asin': row['asin'], 'link': row['target_url'],
                        'buy_box_state': buy_box_state, 'capture_at': row['capture_at'],
                        'sold_by': sold_by, 'sold_by_price': sold_by_price}
                data_list.append(CaptureSkuBuyBoxStateModel(**data))
                sync_last_id = sync_last_id if int(row['id']) < sync_last_id else int(row['id'])
            logger.info(
                'records:{0}, times:{1} s'.format(len(data_list), (datetime.datetime.now() - beginTime).seconds))
            if len(data_list) > 0:
                from django.db import transaction
                with transaction.atomic():
                    AnalysisRuleModel.objects.filter(pk=cfg.id).update(sync_at=sync_at, sync_last_id=sync_last_id)
                    # 批量写入
                    n = 1000
                    m_list = [data_list[i:i + n] for i in range(0, len(data_list), n)]
                    for m in m_list:
                        CaptureSkuBuyBoxStateModel.objects.bulk_create(m)
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))
    logger.info('End for send command of TransferData: {0} s'.format((datetime.datetime.now() - beginTime).seconds))
    return _result


'''同步产品价格'''


def transferPrice(ruleId):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # 你的django的settings文件
    django.setup()
    from amazon.model import CaptureSkuPriceModel
    from appfront.model import ProductAsinModel
    from rule.model import AnalysisRuleModel
    _result = False
    beginTime = datetime.datetime.now()
    try:
        logger.info('Send Command of TransferData: {0}'.format(beginTime.strftime('%H:%M:%S')))
        cfg = AnalysisRuleModel.objects.filter(pk=ruleId).first()
        sync_last_id = 0 if cfg.sync_last_id is None else int(cfg.sync_last_id)
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT * FROM analysis_product_buybox WHERE capture_code = %s AND id > %s ORDER BY id ASC limit 10000",
                           [str(cfg.capture_rule.rule_code), sync_last_id])
            rows = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
            asins = set()
            for row in rows:
                asins.add(row['asin'])
            product_list = ProductAsinModel.objects.filter(asin__in=asins).values_list('asin', 'combine_type', 'sku')
            sku_map = {}
            for i in product_list:
                if sku_map.get(i[0]) is None:
                    sku_map[i[0]] = i
                elif int(sku_map[i[0]][1]) > int(i[1]):
                    sku_map[i[0]] = i
            data_list = []
            logger.info('rows:{}'.format(len(rows)))
            sync_at = timezone.now()
            for row in rows:
                sold_by_price = 0 if row['sold_by_price'] == '' else float(row['sold_by_price'])
                sold_by_price = sold_by_price if row['sold_by_price_buybox'] == '' else float(
                    row['sold_by_price_buybox'])
                if sku_map.get(row['asin']) is None or sold_by_price <= 0:
                    continue
                sku = sku_map.get(row['asin'])[2]
                data = {'platform': 'amazon', 'sku': sku, 'asin': row['asin'], 'link': row['target_url'],
                        'price': sold_by_price, 'capture_at': row['capture_at']}
                data_list.append(CaptureSkuPriceModel(**data))
                sync_last_id = sync_last_id if int(row['id']) < sync_last_id else int(row['id'])
            logger.info(
                'records:{0}, times:{1} s'.format(len(data_list), (datetime.datetime.now() - beginTime).seconds))
            if len(data_list) > 0:
                from django.db import transaction
                with transaction.atomic():
                    AnalysisRuleModel.objects.filter(pk=cfg.id).update(sync_at=sync_at, sync_last_id=sync_last_id)
                    # 批量写入
                    n = 1000
                    m_list = [data_list[i:i + n] for i in range(0, len(data_list), n)]
                    for m in m_list:
                        CaptureSkuPriceModel.objects.bulk_create(m)
                    logger.info('records:{0}, times:{1} s'.format(len(data_list),
                                                                  (datetime.datetime.now() - beginTime).seconds))
                    cursor.execute(
                        'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_price_log_day;'
                        'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_price_log_month;'
                        'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_price_log_week;'
                    )
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))
    logger.info('End for send command of TransferData: {0} s'.format((datetime.datetime.now() - beginTime).seconds))
    return _result


'''同步星级评论'''


def transferReview(ruleId):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # 你的django的settings文件
    django.setup()
    from amazon.model import CaptureSkuReviewModel
    from appfront.model import ProductAsinModel
    from rule.model import AnalysisRuleModel

    _result = False
    beginTime = datetime.datetime.now()
    try:
        logger.info('Send Command of TransferData: {0}'.format(beginTime.strftime('%H:%M:%S')))
        cfg = AnalysisRuleModel.objects.filter(pk=ruleId).first()
        sync_last_id = 0 if cfg.sync_last_id is None else int(cfg.sync_last_id)
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT * FROM analysis_product_review WHERE capture_code = %s AND id > %s ORDER BY id ASC limit 10000",
                           [str(cfg.capture_rule.rule_code), sync_last_id])
            rows = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
            asins = set()
            reviews = set()
            for row in rows:
                asins.add(row['asin'])
                reviews.add(row['review_id'])
            product_list = ProductAsinModel.objects.filter(asin__in=asins).values_list('asin', 'combine_type', 'sku')
            review_list = CaptureSkuReviewModel.objects.filter(review_id__in=reviews).values_list('review_id', 'id')
            sku_map = {}
            for i in product_list:
                if sku_map.get(i[0]) is None:
                    sku_map[i[0]] = i
                elif int(sku_map[i[0]][1]) > int(i[1]):
                    sku_map[i[0]] = i
            review_map = {}
            for i in review_list:
                review_map[i[0]] = i[1]
            data_list = []
            logger.info('rows:{}'.format(len(rows)))
            sync_at = timezone.now()
            for row in rows:
                if sku_map.get(row['asin']) is None or review_map.get(row['review_id']) is not None:
                    continue
                review_at = None if len(row['review_at']) < 1 \
                    else datetime.datetime.strptime(row['review_at'], '%d %B %Y').replace(
                    tzinfo=datetime.timezone(datetime.timedelta(hours=10))).astimezone(datetime.timezone.utc)
                sku = sku_map.get(row['asin'])[2]
                data = {'platform': 'amazon', 'sku': sku, 'asin': row['asin'], 'link': row['target_url'],
                        'review_at': review_at, 'review_id': row['review_id'],
                        'review_rank': row['rank_on'], 'author': row['author'],
                        'title': '', 'content': '', 'selection': '', 'capture_at': row['capture_at']}
                data_list.append(CaptureSkuReviewModel(**data))
                sync_last_id = sync_last_id if int(row['id']) < sync_last_id else int(row['id'])
            logger.info(
                'records:{0}, times:{1} s'.format(len(data_list), (datetime.datetime.now() - beginTime).seconds))
            if len(data_list) > 0:
                _list = {}
                for d in data_list:
                    _list[d.review_id] = d
                data_list = list(_list.values())
                from django.db import transaction
                with transaction.atomic():
                    AnalysisRuleModel.objects.filter(pk=cfg.id).update(sync_at=sync_at, sync_last_id=sync_last_id)
                    # 批量写入
                    n = 1000
                    m_list = [data_list[i:i + n] for i in range(0, len(data_list), n)]
                    for m in m_list:
                        CaptureSkuReviewModel.objects.bulk_create(m)
                    logger.info('records:{0}, times:{1} s'.format(len(data_list),
                                                                  (datetime.datetime.now() - beginTime).seconds))
                    cursor.execute(
                        'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_review_rank_day;'
                        'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_review_rank_month;'
                        'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_review_rank_week;'
                    )
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))
    logger.info('End for send command of TransferData: {0} s'.format((datetime.datetime.now() - beginTime).seconds))
    return _result


'''同步畅销排名'''


def transferBestseller(ruleId):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # 你的django的settings文件
    django.setup()
    from amazon.model import CaptureSkuBestsellerRankModel, AmazonProductCategoryModel
    from appfront.model import ProductAsinModel
    from rule.model import AnalysisRuleModel
    _result = False
    beginTime = datetime.datetime.now()
    logger.info("ruleId:{}".format(ruleId))
    try:
        logger.info('Send Command of TransferData: {0}'.format(beginTime.strftime('%H:%M:%S')))
        cfg = AnalysisRuleModel.objects.filter(pk=ruleId).first()
        sync_last_id = 0 if cfg.sync_last_id is None else int(cfg.sync_last_id)
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT * FROM analysis_product_bestseller WHERE capture_code = %s AND id > %s ORDER BY id ASC limit 10000",
                           [str(cfg.capture_rule.rule_code), sync_last_id])
            rows = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
            asins = set()
            categorys = set()
            sync_at = timezone.now()
            for row in rows:
                asins.add(row['asin'])
                categorys.add(row['category_id'])
            product_list = ProductAsinModel.objects.filter(asin__in=asins).values_list('asin', 'combine_type', 'sku')
            category_list = AmazonProductCategoryModel.objects.filter(code__in=categorys).values_list('code', 'id')
            sku_map = {}
            for i in product_list:
                if sku_map.get(i[0]) is None:
                    sku_map[i[0]] = i
                elif int(sku_map[i[0]][1]) > int(i[1]):
                    sku_map[i[0]] = i
            category_map = {}
            for i in category_list:
                category_map[i[0]] = i[1]
            data_list = []
            logger.info('rows:{}'.format(len(rows)))
            for row in rows:
                if sku_map.get(row['asin']) is None:
                    continue
                sku = sku_map.get(row['asin'])[2]
                category_id = category_map.get(row['category_id'], 1)
                category_title = 'All Category' if row['category_name'] == '' else row['category_name']
                rank_page = 5 if row['page'] == '' or row['page'] == 'None' else int(row['page'])
                data = {'platform': 'amazon', 'sku': sku, 'asin': row['asin'], 'capture_at': row['capture_at'],
                        'rank_on': int(row['rank_on']), 'rank_page': rank_page,
                        'category_id': category_id, 'category_title': category_title}
                data_list.append(CaptureSkuBestsellerRankModel(**data))
                sync_last_id = sync_last_id if int(row['id']) < sync_last_id else int(row['id'])
            logger.info(
                'records:{0}, times:{1} s'.format(len(data_list), (datetime.datetime.now() - beginTime).seconds))
            if len(data_list) > 0:
                from django.db import transaction
                with transaction.atomic():
                    AnalysisRuleModel.objects.filter(pk=cfg.id).update(sync_at=sync_at, sync_last_id=sync_last_id)
                    # 批量写入
                    n = 5000
                    m_list = [data_list[i:i + n] for i in range(0, len(data_list), n)]
                    for m in m_list:
                        CaptureSkuBestsellerRankModel.objects.bulk_create(m)
                    logger.info('records:{0}, times:{1} s'.format(len(data_list),
                                                                  (datetime.datetime.now() - beginTime).seconds))
                    cursor.execute(
                        'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_bestseller_rank_day;'
                        'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_bestseller_rank_month;'
                        'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_bestseller_rank_week;'
                    )
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))
    logger.info('End for send command of TransferData: {0} s'.format((datetime.datetime.now() - beginTime).seconds))
    return _result


'''刷新视图'''


def refershView():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # 你的django的settings文件
    django.setup()
    result = False
    beginTime = datetime.datetime.now()
    try:
        logger.info('Begin for RefershView: {0}'.format(beginTime.strftime('%H:%M:%S')))
        with connections['default'].cursor() as cursor:
            try:
                cursor.execute(
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_keyword_rank_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_keyword_rank_month;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_keyword_rank_week;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_bestseller_rank_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_bestseller_rank_month;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_bestseller_rank_week;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_review_rank_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_review_rank_month;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_review_rank_week;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_price_log_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_price_log_month;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_price_log_week;'
                )
                result = True
            except Exception as e:
                import traceback
                traceback.print_exc()
                logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))
    logger.info('End for RefershView: {0} s'.format((datetime.datetime.now() - beginTime).seconds))
    return result


if __name__ == '__main__':
    transferKeyword(3)
    # transferBestseller(1)
    # transferPrice(4)
    # transferReview(5)
    # transferBuybox(2)
    # refershView()
