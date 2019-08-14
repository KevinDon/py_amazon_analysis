# coding:utf-8
import datetime
from django import forms
from django.utils.translation import ugettext as _
from appfront.model import BusinessReportModel

class BusinessReportForm(forms.ModelForm):
    class Meta:
        model = BusinessReportModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BusinessReportForm, self).__init__(*args, **kwargs)

    # def has_change_permission(self, request):
    #     """ 取消后台编辑附件功能 """
    #     return False
    #
    # def save(self, *args, **kwargs):
    #     # 创建用户时，为用户自动生成个人唯一ID
    #     # if not self.pk:
    #     #     # 存在就更新，不存在就创建
    #     #     m = hashlib.md5()
    #     #     m.update(self.username.encode(encoding="utf-8"))
    #     #     self.uid = m.hexdigest()
    #     # logger.info(self.updated_at)
    #     logger.info(self)
    #     # module.updated_at = datetime.datetime.now()
    #     super(ProductQrcodeModel, self).save(self, *args, **kwargs)
    #     # super(ProductQrcodeModel, self).save(*args, **kwargs)

    # def save_m2m(self, *args, **kwargs):
    #     print('save_m2m')

    def clean_sku(self):
        sku = self.cleaned_data.get('sku')
        return sku.upper()

    def clean_location(self):
        location = self.cleaned_data.get('location')
        return location.upper() if location is not None else ''
