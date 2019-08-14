# coding:utf-8

from django.forms import widgets

class CaptureRuleIdWidget(widgets.Select):

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        html = self._render(self.template_name, context, renderer)
        script = """
        <script>
            jQuery(document).ready(function () {
                jQuery('select#id_rule_id').bind('change',function(e){
                    _value = jQuery('select#id_rule_id').val()
                    if (_value >0){
                        jQuery('#id_command').val('task.cronjobs.Spider.CaptureSpider('+ _value + ')')
                    }else{
                        jQuery('#id_command').val('')
                    }
                })
            })
        </script>
        """

        return  '%s%s' % (html, script)

    def __init__(self, *args, **kwargs):
        super(CaptureRuleIdWidget, self).__init__(*args, **kwargs)


class AnalysisRuleIdWidget(widgets.Select):

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        html = self._render(self.template_name, context, renderer)
        script = """
        <script>
            jQuery(document).ready(function () {
                jQuery('select#id_rule_id').bind('change',function(e){
                    _value = jQuery('select#id_rule_id').val()
                    if (_value >0){
                        jQuery('#id_command').val('task.cronjobs.Analysis.AnalysisData('+ _value + ')')
                    }else{
                        jQuery('#id_command').val('')
                    }
                })
            })
        </script>
        """

        return  '%s%s' % (html, script)

    def __init__(self, *args, **kwargs):
        super(AnalysisRuleIdWidget, self).__init__(*args, **kwargs)
