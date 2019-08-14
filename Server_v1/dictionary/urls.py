from django.conf.urls import url

from dictionary.view.DataDictionaryView import *

urlpatterns = [
    # url(r'^docs$', get_swagger_view(title='System Docs API')),
    # url(r'^dict/DictionaryByCodeGet/', GetDictByCodeView.as_view(), name='GetDictByCodeView'),
    # url(r'^dict/DictionarysByCodeMainGet/', GetDictsByCodeView.as_view(), name='GetDictsByCodeView'),
    # url(r'^dict/DictionaryAllGet/', GetAllDictsView.as_view(), name='GetAllDictsView'),
    url(r'^ajax/get_dict/', getDictByCodeAjaxView, name='getDictByCodeAjaxView'),
    url(r'^ajax/get_all_dict/', getDictsAllAjaxView, name='getDictsAllAjaxView'),
    url(r'^ajax/get_dict_by_code_main/', getDictsByCodeAjaxView, name='getDictsByCodeAjaxView'),
    url(r'^ajax/get_dict_by_cate/', getDictsByCateAjaxView, name='getDictsByCateAjaxView'),
]
