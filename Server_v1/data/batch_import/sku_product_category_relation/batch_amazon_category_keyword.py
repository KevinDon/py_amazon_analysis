import os, csv,sys

import django
from django.db.models import Q
from django.utils import timezone
sys.path.append('.')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()



from amazon.model.AmazonProductCategoryModel import AmazonProductCategoryModel
from amazon.model.SkuKeywordModel import SkuKeywordModel

_suc = 0
_fai = 0
_fai_list = []

# 导入脚本开始

import_batch_file = 'cateogory_keyword.csv'
with open(os.path.realpath(os.path.join(os.path.dirname(__file__),import_batch_file))) as f:
    csv_reader = csv.reader(f)
    columns = next(csv_reader)
    for row in csv_reader:
        _keyword = SkuKeywordModel.objects.filter(Q(title=row[1])).first()
        _amazon_category = AmazonProductCategoryModel.objects.filter(Q(code=row[0])).first()

        if _keyword is None or _amazon_category is None:
            _fai += 1
            _fai_list.append(row)
            continue
        try:
            _amazon_category.keyword.add(_keyword)
            _amazon_category.save()
            _suc += 1
        except Exception as e:
            _fai += 1
            row +=[e]
            _fai_list.append(row)

# 导入脚本完毕
print('任务成功更新了 %s 条,失败了 %s ' % (_suc, _fai))
if _fai > 0:
    user_input = input('是否导出失败记录到failed.log?(Y/N)')
    if user_input.lower() == 'y':
        log_file = 'failed.log'
        with open(os.path.relpath(os.path.join(os.path.dirname(__file__),log_file)), 'w+', newline='') as f:
            for item in _fai_list:
                f.write(str(item)+'\n')
