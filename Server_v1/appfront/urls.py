from django.conf.urls import url

from appfront.view.ProductAsinView import getProductAjaxView
from appfront.views import *

urlpatterns = [
    # url(r'^list/', toList),
    # url(r'^toAdd/', toAdd),
    # url(r'^addTest/', addTest),
    # url(r'^toUpdate/', toUpdate),
    # url(r'^updateTest/', updateTest),
    # url(r'^deleteTest/', deleteTest),
    url(r'get_product_list$', getProductAjaxView, name='getProductAjaxView')
]
