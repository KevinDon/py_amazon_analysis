# coding:utf-8

# Create your views here.
from appfront.view import *


# 404 错误
def page_not_found(request, *args, **kwargs):
    return render(request, 'sites/404.html')

# 500 错误
def page_error(request, *args, **kwargs):
    return render(request, 'sites/500.html', {})
