import os, csv
import sys

import django
from django.db.models import Q
from django.utils import timezone

sys.path.append('.')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from appfront.model import ProductAsinModel, ProductAsinCombineRelationModel

_suc = 0
_fai = 0
_fai_list = []


# 导入脚本开始

def update_product_asin(sku, asin=None, combine_type=0):
    _product = ProductAsinModel.objects.filter(Q(sku=sku) & Q(combine_type=combine_type)).first()

    if _product is None:
        _product = ProductAsinModel()
        _product.created_at = timezone.now
        _product.status = 1
        _product.sort = 1
        _product.creator_id = 1
        _product.sku = sku
        _product.combine_type = combine_type

    if asin is not None:
        _product.asin = asin

    _product.updated_at = timezone.now
    _product.save()

    return _product


import_single_file = 'batch_single_sku_list.csv'

# single sku - ok
with open(os.path.realpath(os.path.join(os.path.dirname(__file__), import_single_file))) as f:
    csv_reader = csv.reader(f)
    columns = next(csv_reader)
    for row in csv_reader:
        if row[0] is '':
            continue
        try:
            _single_product = update_product_asin(sku=row[0], asin=row[1] or None, combine_type=1)
            _suc += 1
            print('成功导入%s条数据:sku:%s,asin:%s OK!' % (_suc, row[0], row[1]))
        except Exception as e:
            _fai += 1
            row += [e]
            _fai_list.append(row)

    # 导入脚本完毕
print('任务成功更新了 %s 条,失败了 %s ' % (_suc, _fai))
if _fai > 0:
    user_input = input('是否导出失败记录到failed.log?(Y/N)')
    if user_input.lower() == 'y':
        log_file = 'failed.log'
        with open(os.path.relpath(os.path.join(os.path.dirname(__file__), log_file)), 'w+', newline='') as f:
            for item in _fai_list:
                f.write(str(item) + '\n')
