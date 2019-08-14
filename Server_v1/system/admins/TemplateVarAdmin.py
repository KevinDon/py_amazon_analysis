from system.model import *
from django.contrib.auth.admin import *
from system.forms import *
from manager.admin import CommonAdmin


@admin.register(TemplateVarModel)
class TemplateVarAdmin(CommonAdmin):
    list_display = ('name', 'code', 'type', 'scope')
    form = TemplateVarForm
    search_fields = ('name', 'message_type')
    fieldsets = (
        (None, {
            'fields': ('name', 'code', 'type',  'scope', 'message_type', 'is_custom', 'value')
        }),)

    class Media:
        js = ('system/template-var-form.js',)

