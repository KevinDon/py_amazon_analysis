INSERT INTO "system_message_template"("id", "name", "describe", "content", "type", "message_type", "created_at", "updated_at", "creator_id", "cronjob_id", "condition") VALUES (3, '购物车被占用', '购物车被占用', '### 购物车占有提醒
{% for sku in data %}
   {{ sku.asin }}:{{ sku.asin }}:{{ sku.capture_at }}:[详细](http://www.thinkpage.cn/)
{% endfor %}
#### sendtime:{{ now }}   
#### sender:{{ sender }}   
{{ test }}', 'markdown', 'ShoppingCartNotice', '2019-06-12 05:08:54.864+00', '2019-06-12 05:35:54.469+00', NULL, 7, '{
  "conjunction": "and",
  "filters": [
    {
      "conjunction": null,
      "filters": null,
      "field": "sku",
      "operator": "lk",
      "values": [
        "BK259P6"
      ],
      "type": "string"
    },
    {
      "conjunction": null,
      "filters": null,
      "field": "line_id",
      "operator": "eq",
      "values": [
        "1"
      ],
      "type": "string"
    }
  ],
  "field": null,
  "operator": null,
  "values": null,
  "type": null
}');
INSERT INTO "system_message_template"("id", "name", "describe", "content", "type", "message_type", "created_at", "updated_at", "creator_id", "cronjob_id", "condition") VALUES (4, '购物车占用2', '购物车占用2', '### 购物车占有提醒2
{% for sku in data %}
   {{ sku.asin }}:{{ sku.asin }}:{{ sku.capture_at }}:[详细](http://www.thinkpage.cn/)
{% endfor %}
#### sendtime:{{ now }}   
#### sender:{{ sender }}   
{{ test }}', 'markdown', 'ShoppingCartNotice', '2019-06-12 05:21:34.416+00', '2019-06-12 06:16:03.203+00', NULL, 7, '{
  "conjunction": "and",
  "filters": [
    {
      "conjunction": null,
      "filters": null,
      "field": "sku",
      "operator": "lk",
      "values": [
        "BK259P6"
      ],
      "type": "string"
    },
    {
      "conjunction": null,
      "filters": null,
      "field": "line_id",
      "operator": "eq",
      "values": [
        "1"
      ],
      "type": "string"
    }
  ],
  "field": null,
  "operator": null,
  "values": null,
  "type": null
}');
INSERT INTO "system_message_template"("id", "name", "describe", "content", "type", "message_type", "created_at", "updated_at", "creator_id", "cronjob_id", "condition") VALUES (5, '产品星级评论通知', '产品星级评论通知', '### 星级评论
{% for sku in data %}
   {{ sku.asin }}:{{ sku.asin }}:{{ sku.review_rank}}:[详细](http://www.thinkpage.cn/)
{% endfor %}
#### sendtime:{{ now }}   
#### sender:{{ sender }}   
{{ test }}', 'markdown', 'ProductStarNotice', '2019-06-13 08:25:45.7824+00', '2019-06-13 08:37:21.6374+00', NULL, 8, '{
  "conjunction": "and",
  "filters": [
    {
      "conjunction": null,
      "filters": null,
      "field": "sku",
      "operator": "lk",
      "values": [
        "P6"
      ],
      "type": "string"
    },
    {
      "conjunction": null,
      "filters": null,
      "field": "line_id",
      "operator": "eq",
      "values": [
        "1"
      ],
      "type": "string"
    }
  ],
  "field": null,
  "operator": null,
  "values": null,
  "type": null
}');
