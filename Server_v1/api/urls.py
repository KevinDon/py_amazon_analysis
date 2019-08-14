# coding:utf-8

from django.conf.urls import url
from django.urls import include, path
# from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from api.views import *

# router = routers.DefaultRouter()    # 创建路由对象
# router.register(r'statvisitqrcodeskus', StatVisitQrcodeSkusSet, basename='sku')
# router.register(r'statvisitqrcodeskuday', StatVisitQrcodeSkuDaySet, basename='sku')

# schema_view = get_schema_view(title='API DOCS', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^docs$',schema_view),
    # url(r'^(?P<version>[v1|v2]+)/',include(router.urls)),
    # url(r'^test$',TestSet.as_view()),
    url(r'^docs$', get_swagger_view(title='Docs API')),
    url(r'^(?P<version>[v1|v2]+)/apitokenauth', LoginSet.as_view(), name='apitokenauth'),
    url(r'^(?P<version>[v1|v2]+)/userprofile', UserProfileSet.as_view(), name='userprofile'),
    # url(r'^api-token-auth', obtain_jwt_token),
    url(r'^(?P<version>[v1|v2]+)/statamazonsku/', StatAmazonSkuSet.as_view(), name='statamazonsku'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskulist/', StatAmazonSkuListGet.as_view(), name='statamazonskulist'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskuuvday/', StatAmazonSkuUvDaySet.as_view(), name='statamazonskuuvday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskuuvmonth/', StatAmazonSkuUvMonthSet.as_view(), name='statamazonskuuvmonth'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskuuvweek/', StatAmazonSkuUvWeekSet.as_view(), name='statamazonskuuvweek'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskupvday/', StatAmazonSkuPvDaySet.as_view(), name='statamazonskupvday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskupvmonth/', StatAmazonSkuPvMonthSet.as_view(), name='statamazonskupvmonth'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskupvweek/', StatAmazonSkuPvWeekSet.as_view(), name='statamazonskupvweek'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskutotalitemsday/', StatAmazonSkuTotalItemsDaySet.as_view(), name='statamazonskutotalitemsday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskutotalitemsmonth/', StatAmazonSkuTotalItemsMonthSet.as_view(), name='statamazonskutotalitemsmonth'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskutotalitemsweek/', StatAmazonSkuTotalItemsWeekSet.as_view(), name='statamazonskutotalitemsweek'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskubuyboxday/', StatAmazonSkuBuyBoxDaySet.as_view(), name='statamazonskubuyboxday'),

    # amazon category
    url(r'^(?P<version>[v1|v2]+)/statmazoncategorylist/', StatAmazonCategoryListSet.as_view(), name='statamazoncategorylistset'),
    url(r'^(?P<version>[v1|v2]+)/statmazoncategorys/', StatAmazonCategorySet.as_view(), name='statamazoncategorysset'),
    # keyword
    url(r'^(?P<version>[v1|v2]+)/statamazonkeywordlistset/', StatAmazonKeywordListSet.as_view(), name='statamazonkeywordlistset'),
    url(r'^(?P<version>[v1|v2]+)/statamazonkeywordsset/', StatAmazonKeywordsSet.as_view(), name='statamazonkeywordsset'),
    # template variant
    url(r'^(?P<version>[v1|v2]+)/statamazonvariantlistset/', StatAmazonVariantListSet.as_view(), name='statamazonvariantlistset'),

    # proxy ip
    url(r'^(?P<version>[v1|v2]+)/statamazonproxyiplistset/', StatAmazonProxyIpListSet.as_view(), name='statamazonproxyiplistset'),

    # line
    url(r'^(?P<version>[v1|v2]+)/statamazonline/', StatAmazonLineSet.as_view(), name='statamazonline'),
    url(r'^(?P<version>[v1|v2]+)/statamazonlineuvday/', StatAmazonLineUvDaySet.as_view(), name='statamazonlineuvday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonlineuvmonth/', StatAmazonLineUvMonthSet.as_view(), name='statamazonlineuvmonth'),
    url(r'^(?P<version>[v1|v2]+)/statamazonlineuvweek/', StatAmazonLineUvWeekSet.as_view(), name='statamazonlineuvweek'),
    url(r'^(?P<version>[v1|v2]+)/statamazonlinepvday/', StatAmazonLinePvDaySet.as_view(), name='statamazonlinepvday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonlinepvmonth/', StatAmazonLinePvMonthSet.as_view(), name='statamazonlinepvmonth'),
    url(r'^(?P<version>[v1|v2]+)/statamazonlinepvweek/', StatAmazonLinePvWeekSet.as_view(), name='statamazonlinepvweek'),
    url(r'^(?P<version>[v1|v2]+)/statamazonlinetotalitemsday/', StatAmazonLineTotalItemsDaySet.as_view(), name='statamazonlinetotalitemsday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonlinetotalitemsmonth/', StatAmazonLineTotalItemsMonthSet.as_view(), name='statamazonlinetotalitemsmonth'),
    url(r'^(?P<version>[v1|v2]+)/statamazonlinetotalitemsweek/', StatAmazonLineTotalItemsWeekSet.as_view(), name='statamazonlinetotalitemsweek'),
    url(r'^(?P<version>[v1|v2]+)/statamazonlinebuyboxday/', StatAmazonLineBuyBoxDaySet.as_view(), name='statamazonlinebuyboxday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonlineuvitemsconversionrateday/', StatAmazonLineUvItemsConversionRateDaySet.as_view(), name='statamazonlineuvitemsconversionrateday'),
    # Category Rank
    url(r'^(?P<version>[v1|v2]+)/statamazonskucategoryrankday/', StatAmazonSkuCategoryRankDaySet.as_view(), name='statamazonskucategoryrankday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskucategoryrankmonth/', StatAmazonSkuCategoryRankMonthSet.as_view(), name='statamazonskucategoryrankmonth'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskucategoryrankweek/', StatAmazonSkuCategoryRankWeekSet.as_view(), name='statamazonskucategoryrankweek'),
    # Keyword Rank
    url(r'^(?P<version>[v1|v2]+)/statamazonskukeywordrankday/', StatAmazonSkuKeywordRankDaySet.as_view(), name='statamazonskukeywordrankday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskukeywordrankmonth/', StatAmazonSkuKeywordRankMonthSet.as_view(), name='statamazonskukeywordrankmonth'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskukeywordrankweek/', StatAmazonSkuKeywordRankWeekSet.as_view(), name='statamazonskukeywordrankweek'),
    # Review Rank
    url(r'^(?P<version>[v1|v2]+)/statamazonskureviewrankday/', StatAmazonSkuReviewRankDaySet.as_view(), name='statamazonskureviewrankday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskureviewrankmonth/', StatAmazonSkuReviewRankMonthSet.as_view(), name='statamazonskureviewrankmonth'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskureviewrankweek/', StatAmazonSkuReviewRankWeekSet.as_view(), name='statamazonskureviewrankweek'),
    # Composite Report
    url(r'^(?P<version>[v1|v2]+)/statamazonskucompositereportday/', StatAmazonSkuCompositeReportDaySet.as_view(), name='statamazonskucompositereportday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskucompositereportmonth/', StatAmazonSkuCompositeReportMonthSet.as_view(), name='statamazonskucompositereportmonth'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskucompositereportweek/', StatAmazonSkuCompositeReportWeekSet.as_view(), name='statamazonskucompositereportweek'),
    # Price Log
    url(r'^(?P<version>[v1|v2]+)/statamazonskupricelogday/', StatAmazonSkuPriceLogDaySet.as_view(), name='statamazonskupricelogday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskupricelogmonth/', StatAmazonSkuPriceLogMonthSet.as_view(), name='statamazonskupricelogmonth'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskupricelogweek/', StatAmazonSkuPriceLogWeekSet.as_view(), name='statamazonskupricelogweek'),
    # Bestseller Rank
    url(r'^(?P<version>[v1|v2]+)/statamazonskubestsellerrankday/', StatAmazonSkuBestsellerRankDaySet.as_view(), name='statamazonskubestsellerrankday'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskubestsellerrankmonth/', StatAmazonSkuBestsellerRankMonthSet.as_view(), name='statamazonskubestsellerrankmonth'),
    url(r'^(?P<version>[v1|v2]+)/statamazonskubestsellerrankweek/', StatAmazonSkuBestsellerRankWeekSet.as_view(), name='statamazonskubestsellerrankweek'),
    # Auth Department
    url(r'^(?P<version>[v1|v2]+)/statauthdepartment/', StatAuthDepartmentView.as_view(), name='statauthdepartment'),
]

'''
request params:
{
"pager":{"size":5, "page":1}
,"order":["dy", "-sku"]
,"filter": [[{"sku-eq":"WBLANKET-PLUSH-5KG"},{"sku-eq":"HM-BED-TASSEL-COT-CR"}],[{"dy-lk-and":"2019-03-19"}]]
}
'''
