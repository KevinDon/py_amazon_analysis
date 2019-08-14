import os
import django
import datetime
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")  # 你的django的settings文件
django.setup()
from appfront.model import *
from amazon.model import *

if __name__ == '__main__':
    data_list = []
    # for i in range(100):
    #     data_list.append(SkuKeywordModel(title="123456"))
    # SkuKeywordModel.objects.bulk_create(data_list)
    #
    keyword = SkuKeywordModel.objects.create(title="test")
    category = ProductCategoryModel.objects.create(title="test")
    # 获取产品列表
    product_list = ProductAsinModel.objects.all()[0:10]
    # 购物车占有
    buy_box_list = []
    # 星级评论
    review_list = []
    # 分类排名
    cate_rank_list = []
    # 关键词排名
    keyword_rank_list = []
    # 价格轨迹
    price_log_list = []
    for i in product_list:
        i.category = category
        i.save()
        buy_box_list.append(
            CaptureSkuBuyBoxStateModel(sku=i.sku, asin=i.asin, capture_at=datetime.datetime.now(), buy_box_state=1, sold_by_price=1, sold_by='test', link='test'))
        review_list.append(
            CaptureSkuReviewModel(sku=i.sku, asin=i.asin, capture_at=datetime.datetime.now(), review_rank=random.randint(0,5), selection='test', link='test'))
        cate_rank_list.append(
            CaptureSkuCategoryRankModel(sku=i.sku, asin=i.asin, capture_at=datetime.datetime.now(), category_id=i.category.id, category_title=i.category.title, rank_on=random.randint(0,5), rank_page='test'))
        keyword_rank_list.append(
            CaptureSkuKeywordRankModel(sku=i.sku, asin=i.asin, capture_at=datetime.datetime.now(), sku_keyword_id=keyword.id, category_title=i.category.title, rank_on=random.randint(0,5), rank_page='test'))
        price_log_list.append(
            CaptureSkuPriceModel(sku=i.sku, asin=i.asin, capture_at=datetime.datetime.now(), price=random.randint(1,100), link='test'))
    CaptureSkuBuyBoxStateModel.objects.bulk_create(buy_box_list)
    CaptureSkuReviewModel.objects.bulk_create(review_list)
    CaptureSkuCategoryRankModel.objects.bulk_create(cate_rank_list)
    CaptureSkuKeywordRankModel.objects.bulk_create(keyword_rank_list)
    CaptureSkuPriceModel.objects.bulk_create(price_log_list)