# coding:utf-8
from manager.model import *
from django.contrib.auth.admin import *
from django.utils.translation import ugettext_lazy as _


class PermissionInline(admin.StackedInline):
    model = ApiPermissionModel
    fields = ('type',)


@admin.register(PermissionModel)
class PermissionAdmin(admin.ModelAdmin):
    inlines = (PermissionInline,)
    list_display = ('name', 'codename', 'type_name')
    search_fields = ('name', 'codename')
    ordering = ['-id']
    #exclude = ('content_type',)

    def type_name(self, obj):
        return _('Data').__str__() if hasattr(obj, 'api_permission') and obj.api_permission.type == 1 else _('Operation').__str__()
    type_name.short_description = _('type')

    # def get_queryset(self, request):
    #     content_type = ContentType.objects.filter(model='apipermission').last()
    #     return Permission.objects.filter(content_type=content_type)

    def save_model(self, request, obj, form, change):
        # if not hasattr(obj, 'content_type'):
        #     obj.content_type = ContentType.objects.filter(model='apipermission').last()
        obj.creator_id = request.user.id
        super().save_model(request, obj, form, change)
        if not hasattr(obj, 'api_permission'):
            api_permission = ApiPermissionModel(permission=obj, type=request.POST['api_permission-0-type'],
                                                creator_id=request.user.id)
            api_permission.save()
