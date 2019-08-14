# coding:utf-8
from django.contrib.admin.utils import get_deleted_objects

from manager.forms import *
from manager.model import *
from django.contrib.auth.admin import *
from django.utils.translation import ugettext_lazy as _


class GroupInline(admin.StackedInline):
    model = GroupProfileModel
    verbose_name = 'profile'
    fields = ('code', 'parent',)
    form = GroupInlineForm


class GroupProfileAdmin(GroupAdmin):
    inlines = (GroupInline,)
    list_display = ('name', 'code', 'parent_name')
    form = GroupProfileForm

    def code(self, obj):
        return obj.group_profile.code
    code.short_description = _('code')

    def parent_name(self, obj):
        parent_name = ''
        if obj.group_profile.parent is not None:
            parent_name = obj.group_profile.parent.group.name
        return parent_name
    parent_name.short_description = _('parent name')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not hasattr(obj, 'group_profile'):
            parent = None if request.POST['group_profile-0-parent'] == '' \
                else GroupProfileModel.objects.get(pk=request.POST['group_profile-0-parent'])
            profile = GroupProfileModel(group=obj, code=request.POST['group_profile-0-code'], parent=parent)
            profile.save()

    def get_deleted_objects(self, objs, request):
        to_delete, model_count, perms_needed, protected = get_deleted_objects(objs, request, self.admin_site)
        for obj in objs:
            protected = protected + list(obj.user_set.all())
        return to_delete, model_count, perms_needed, protected


admin.site.unregister(Group)
admin.site.register(GroupModel, GroupProfileAdmin)
