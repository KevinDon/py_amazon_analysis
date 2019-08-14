from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from system.view.RegionView import getCountryAjaxView, getRegionAjaxView, getCityAjaxView, getIPsAjaxView

urlpatterns = [
    # url(r'^docs$', get_swagger_view(title='System Docs API')),
    # url(r'^dict/DictionaryByCodeGet/', GetDictByCodeView.as_view(), name='GetDictByCodeView'),
    # url(r'^dict/DictionarysByCodeGet/', GetDictsByCodeView.as_view(), name='GetDictsByCodeView'),
    # url(r'^dict/DictionaryAllGet/', GetAllDictsView.as_view(), name='GetAllDictsView'),
    url(r'^region/get_country/', getCountryAjaxView, name='getCountryAjaxView'),
    url(r'^region/get_region/', getRegionAjaxView, name='getRegionAjaxView'),
    url(r'^region/get_city/', getCityAjaxView, name='getCityAjaxView'),
    url(r'^proxy_id/get_ips/', getIPsAjaxView, name='getIpsAjaxView'),
]
