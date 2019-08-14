from dictionary.vo import DataDictionaryCategoryVo
from system.model import *
from django.contrib.auth.admin import *
from manager.admin import CommonAdmin
from system.forms import *
from django.utils.translation import ugettext_lazy as _


class PlatformSettingManager(models.Manager):
    def get_queryset(self):
        return self._queryset_class(model=DataDictionaryCategoryModel, using=self._db, hints=self._hints)


class PlatformSettingModel(models.Model):

    objects = PlatformSettingManager()

    class Meta:
        app_label = "system"
        verbose_name = _("Platform Setting")
        verbose_name_plural = _("Platform Setting")
        managed = False


@admin.register(PlatformSettingModel)
class PlatformSettingAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, object_id=None):
        return False

    def save_model(self, request, obj, form, change):
        data_list = request.POST
        for k, v in data_list.items():
            if k[0:4] == 'dict' and int(k[4:]) > 0:
                DataDictionaryValueModel.objects.filter(pk=int(k[4:])).update(value=v)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(status=3).filter(data_type=2)

    def get_form(self, request, obj=None, **kwargs):
        class ModelMeta:
            app_label = "system"
            verbose_name = _("Platform")
            verbose_name_plural = _("Platform")
            managed = False
        model_attrs = {
            '__module__': obj.code+'Model',
            'Meta': ModelMeta}
        dict_list = DataDictionaryCategoryVo(instance=obj).data
        for dict in dict_list['dicts']:
            key = 'dict'+dict['dict_values'][0]['id'].__str__()
            model_attrs[key] = models.CharField(max_length=200, verbose_name=dict['title'], default=dict['dict_values'][0]['value'])

        class FormMeta:
            model = type(obj.code+'Model', (models.Model,), model_attrs)
            fields = '__all__'
        form = type(obj.code+'Form', (forms.ModelForm,), {
            'Meta': FormMeta,
            '__module__': obj.code+'Form'})
        return form
