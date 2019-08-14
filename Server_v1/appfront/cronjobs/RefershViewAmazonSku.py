
import datetime
import time

from django.core.handlers.base import logger
from django.db import connections


def refershViewAmazonSku():
    result = False
    beginTime = datetime.datetime.now()
    try:
        logger.info('Begin for RefershViewAmazonSku: {0}'.format(beginTime.strftime('%H:%M:%S')))
        with connections['default'].cursor() as cursor:
            try:
                cursor.execute(
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_buy_box_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_pv_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_pv_month;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_pv_week;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_total_items_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_total_items_month;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_total_items_week;'
                )
                cursor.execute(
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_total_items_month;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_total_items_week;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_uv_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_uv_month;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_sku_uv_week;'
                )
                cursor.execute(
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_buy_box_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_pv_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_pv_month;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_pv_week;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_total_items_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_total_items_month;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_total_items_week;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_uv_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_uv_items_conversion_rate_day;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_uv_month;'
                    'REFRESH MATERIALIZED VIEW "public".view_i_amazon_line_uv_week;'
                )
                result = True
            except Exception as e:
                logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))

    except Exception as e:
        logger.error('error: {0} | {1}'.format((datetime.datetime.now() - beginTime).seconds, e))

    logger.info('End for RefershViewAmazonSku: {0} s'.format((datetime.datetime.now() - beginTime).seconds))

    return result