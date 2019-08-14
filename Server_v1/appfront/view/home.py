# coding:utf-8

import datetime

from django.core.handlers.base import logger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

from appfront.model import *

'''首页'''
def index(request):
    params = {
        'site_name': 'Product QRcode',
        'name': 'Product QRcode',
        '_context': datetime.datetime.now(),
    }

    return render_to_response('front/index.html', params)


def testcron(request = ''):

    logger.info('test inner pro. cronjob')
    
    return HttpResponse('test cronjob')