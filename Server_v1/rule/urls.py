from django.conf.urls import url

from rule.view.CaptureRuleView import *

urlpatterns = [
    url(r'^get_capture$', getCaptureRuleAjaxView, name='getCaptureRuleAjaxView'),
    url(r'^get_capture_xml$', getCaptureRuleXMLAjaxView, name='getCaptureRuleXMLAjaxView'),
]
