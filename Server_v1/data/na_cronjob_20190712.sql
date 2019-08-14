INSERT INTO "na_cronjob"("id", "type", "code", "title", "yr", "mo", "dy", "wk", "dy_of_week", "hr", "mi", "se", "start_date", "end_date", "timezone", "status", "command", "command_type", "updated_at", "created_at", "creator_id", "task_type") VALUES (7, 2, 'SHIPPINGCART', '购物车占用通知', '*', '*', '*', '*', '*', '*', '*/5', '0', '2019-06-12 03:00:00+00', '2019-06-30 03:05:00+00', NULL, 1, 'task.cronjobs.ShoppingCartNotice.handle()', 1, '2019-07-02 09:22:40.844+00', '2019-06-12 05:08:41.197+00', 1, 4);
INSERT INTO "na_cronjob"("id", "type", "code", "title", "yr", "mo", "dy", "wk", "dy_of_week", "hr", "mi", "se", "start_date", "end_date", "timezone", "status", "command", "command_type", "updated_at", "created_at", "creator_id", "task_type") VALUES (8, 2, 'PRODUCTSTARNOTICE', '产品星级评论通知', '*', '*', '*', '*', '*', '*', '*', '*/20', '2019-06-13 06:25:00+00', '2019-06-30 06:55:00+00', NULL, 1, 'task.cronjobs.ProductStarNotice.handle()', 1, '2019-06-13 08:25:31.3914+00', '2019-06-13 08:25:31.3784+00', 1, 4);
INSERT INTO "na_cronjob"("id", "type", "code", "title", "yr", "mo", "dy", "wk", "dy_of_week", "hr", "mi", "se", "start_date", "end_date", "timezone", "status", "command", "command_type", "updated_at", "created_at", "creator_id", "task_type") VALUES (3, 1, 'ABCDD', '每天刷新固化视图', '*', '*', '*/1', '*', '*', '0', '15', '0', '2019-03-31 21:55:00+00', '2050-08-01 06:55:00+00', NULL, 2, 'appfront.cronjobs.RefershViewAmazonSku.refershViewAmazonSku()', 1, '2019-05-21 06:43:53.954204+00', '2019-04-05 08:56:27.354+00', 1, 5);
INSERT INTO "na_cronjob"("id", "type", "code", "title", "yr", "mo", "dy", "wk", "dy_of_week", "hr", "mi", "se", "start_date", "end_date", "timezone", "status", "command", "command_type", "updated_at", "created_at", "creator_id", "task_type") VALUES (1, 2, 'PROXYIPCHECK', '代理IP池检查', '*', '*', '*', '*', '*', '*', '*', '*/50', '2019-07-08 06:55:00+00', '2019-07-08 06:55:00+00', NULL, 1, 'task.cronjobs.ProxyIpCheck.handle()', 1, '2019-07-08 08:26:49.642+00', '2019-07-08 08:26:32.098+00', 1, 9);
INSERT INTO "na_cronjob"("id", "type", "code", "title", "yr", "mo", "dy", "wk", "dy_of_week", "hr", "mi", "se", "start_date", "end_date", "timezone", "status", "command", "command_type", "updated_at", "created_at", "creator_id", "task_type") VALUES (2, 2, 'TASK_MESSAGE', '消息发送任务', '*', '*', '*', '*', '*', '*', '*', '*/30', '2019-05-20 01:00:00+00', '2019-06-28 01:30:00+00', NULL, 1, 'task.cronjobs.TaskMessage.send()', 1, '2019-06-13 02:20:15.0704+00', '2019-05-20 02:58:50.197+00', 1, 9);
