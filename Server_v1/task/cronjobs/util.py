from django.db.models import Q
import datetime
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
from core.libs import QueryFilter as QF


def condition_parse(data):
    if data['conjunction'] is not None:
        values = Q(_connector=data['conjunction'].upper())
        for v in data['filters']:
            values.children.append(condition_parse(v))
        return values
    else:
        return QF().parseField(data['field'], data['operator'], data['values'][0])


def get_var_data(message_type):
    keys = []
    values = []
    try:
        # 内置系统变量
        system = {
            'now': datetime.datetime.now(),
        }
        from system.model.TemplateVarModel import TemplateVarModel
        var_list = TemplateVarModel.objects.filter(
            Q(scope__exact='1') | Q(scope__gt='1', message_type__contains='\'{}\''.format(message_type)))
        for v in var_list:
            keys.append(v.code)
            # 自定义
            if v.is_custom:
                values.append(v.value)
            else:
                val = '' if v.code not in system.keys() else system[v.code]
                values.append(val)
    except Exception as e:
        return {}
    return dict(zip(keys, values))


if __name__ == '__main__':
    import json
    print(condition_parse(json.loads('{ "conjunction": "and", "filters": [ { "conjunction": null, "filters": null, "field": "sku", "operator": "lk", "values": [ "BK259P6" ], "type": "string" }, { "conjunction": null, "filters": null, "field": "line_id", "operator": "eq", "values": [ "1" ], "type": "string" } ], "field": null, "operator": null, "values": null, "type": null }')))