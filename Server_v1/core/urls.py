"""data_center1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import RedirectView, TemplateView
from django.views.static import serve

import appfront.views as views
from core.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/images/favicon.ico')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path(r'admin/', admin.site.urls),
    path(r'front/', include("appfront.urls")),
    path(r'cron/', include("cronjob.urls")),
    url(r'^api/', include('api.urls')),
    url(r'^system/', include('system.urls')),
    path('', views.index),
    url(r'^chart/', TemplateView.as_view(template_name="front/index.html")),
    # 处理 media 信息，用于图片获取
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^dictionary/', include('dictionary.urls')),
    url(r'^rule/', include('rule.urls')),
]

handler404 = 'appfront.views.page_not_found'
handler500 = 'appfront.views.page_error'
