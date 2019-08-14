/*
 Navicat Premium Data Transfer

 Source Server         : localPgSql
 Source Server Type    : PostgreSQL
 Source Server Version : 100007
 Source Host           : localhost:5432
 Source Catalog        : newaim_amazon_analysis_server
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 100007
 File Encoding         : 65001

 Date: 15/05/2019 18:41:59
*/


-- ----------------------------
-- Table structure for auth_group_profile
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_group_profile";
CREATE TABLE "public"."auth_group_profile" (
  "id" int4 NOT NULL DEFAULT nextval('auth_group_profile_id_seq'::regclass),
  "code" varchar(100) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "created_at" timestamptz(6) DEFAULT NULL,
  "updated_at" timestamptz(6) DEFAULT NULL,
  "is_enable" int4 DEFAULT NULL,
  "is_delete" int4 DEFAULT NULL,
  "creator_id" int4 DEFAULT NULL,
  "group_id" int4 NOT NULL DEFAULT NULL,
  "parent_id" int4 DEFAULT NULL,
  "updater_id" int4 DEFAULT NULL
)
;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_permission";
CREATE TABLE "public"."auth_permission" (
  "id" int4 NOT NULL DEFAULT nextval('auth_permission_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "content_type_id" int4 NOT NULL DEFAULT NULL,
  "codename" varchar(100) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL
)
;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO "public"."auth_permission" VALUES (1, 'Can add user dashboard module', 1, 'add_userdashboardmodule');
INSERT INTO "public"."auth_permission" VALUES (2, 'Can change user dashboard module', 1, 'change_userdashboardmodule');
INSERT INTO "public"."auth_permission" VALUES (3, 'Can delete user dashboard module', 1, 'delete_userdashboardmodule');
INSERT INTO "public"."auth_permission" VALUES (4, 'Can view user dashboard module', 1, 'view_userdashboardmodule');
INSERT INTO "public"."auth_permission" VALUES (5, 'Can add bookmark', 2, 'add_bookmark');
INSERT INTO "public"."auth_permission" VALUES (6, 'Can change bookmark', 2, 'change_bookmark');
INSERT INTO "public"."auth_permission" VALUES (7, 'Can delete bookmark', 2, 'delete_bookmark');
INSERT INTO "public"."auth_permission" VALUES (8, 'Can view bookmark', 2, 'view_bookmark');
INSERT INTO "public"."auth_permission" VALUES (9, 'Can add pinned application', 3, 'add_pinnedapplication');
INSERT INTO "public"."auth_permission" VALUES (10, 'Can change pinned application', 3, 'change_pinnedapplication');
INSERT INTO "public"."auth_permission" VALUES (11, 'Can delete pinned application', 3, 'delete_pinnedapplication');
INSERT INTO "public"."auth_permission" VALUES (12, 'Can view pinned application', 3, 'view_pinnedapplication');
INSERT INTO "public"."auth_permission" VALUES (13, 'Can add log entry', 4, 'add_logentry');
INSERT INTO "public"."auth_permission" VALUES (14, 'Can change log entry', 4, 'change_logentry');
INSERT INTO "public"."auth_permission" VALUES (15, 'Can delete log entry', 4, 'delete_logentry');
INSERT INTO "public"."auth_permission" VALUES (16, 'Can view log entry', 4, 'view_logentry');
INSERT INTO "public"."auth_permission" VALUES (17, 'Can add group', 5, 'add_group');
INSERT INTO "public"."auth_permission" VALUES (18, 'Can change group', 5, 'change_group');
INSERT INTO "public"."auth_permission" VALUES (19, 'Can delete group', 5, 'delete_group');
INSERT INTO "public"."auth_permission" VALUES (20, 'Can view group', 5, 'view_group');
INSERT INTO "public"."auth_permission" VALUES (21, 'Can add user', 6, 'add_user');
INSERT INTO "public"."auth_permission" VALUES (22, 'Can change user', 6, 'change_user');
INSERT INTO "public"."auth_permission" VALUES (23, 'Can delete user', 6, 'delete_user');
INSERT INTO "public"."auth_permission" VALUES (24, 'Can view user', 6, 'view_user');
INSERT INTO "public"."auth_permission" VALUES (25, 'Can add permission', 7, 'add_permission');
INSERT INTO "public"."auth_permission" VALUES (26, 'Can change permission', 7, 'change_permission');
INSERT INTO "public"."auth_permission" VALUES (27, 'Can delete permission', 7, 'delete_permission');
INSERT INTO "public"."auth_permission" VALUES (28, 'Can view permission', 7, 'view_permission');
INSERT INTO "public"."auth_permission" VALUES (29, 'Can add content type', 8, 'add_contenttype');
INSERT INTO "public"."auth_permission" VALUES (30, 'Can change content type', 8, 'change_contenttype');
INSERT INTO "public"."auth_permission" VALUES (31, 'Can delete content type', 8, 'delete_contenttype');
INSERT INTO "public"."auth_permission" VALUES (32, 'Can view content type', 8, 'view_contenttype');
INSERT INTO "public"."auth_permission" VALUES (33, 'Can add session', 9, 'add_session');
INSERT INTO "public"."auth_permission" VALUES (34, 'Can change session', 9, 'change_session');
INSERT INTO "public"."auth_permission" VALUES (35, 'Can delete session', 9, 'delete_session');
INSERT INTO "public"."auth_permission" VALUES (36, 'Can view session', 9, 'view_session');
INSERT INTO "public"."auth_permission" VALUES (37, 'Can add Business Report', 10, 'add_businessreportmodel');
INSERT INTO "public"."auth_permission" VALUES (38, 'Can change Business Report', 10, 'change_businessreportmodel');
INSERT INTO "public"."auth_permission" VALUES (39, 'Can delete Business Report', 10, 'delete_businessreportmodel');
INSERT INTO "public"."auth_permission" VALUES (40, 'Can view Business Report', 10, 'view_businessreportmodel');
INSERT INTO "public"."auth_permission" VALUES (41, 'Can add Product Asin', 11, 'add_productasinmodel');
INSERT INTO "public"."auth_permission" VALUES (42, 'Can change Product Asin', 11, 'change_productasinmodel');
INSERT INTO "public"."auth_permission" VALUES (43, 'Can delete Product Asin', 11, 'delete_productasinmodel');
INSERT INTO "public"."auth_permission" VALUES (44, 'Can view Product Asin', 11, 'view_productasinmodel');
INSERT INTO "public"."auth_permission" VALUES (45, 'Can add Stat Days', 12, 'add_pubstatdaysmodel');
INSERT INTO "public"."auth_permission" VALUES (46, 'Can change Stat Days', 12, 'change_pubstatdaysmodel');
INSERT INTO "public"."auth_permission" VALUES (47, 'Can delete Stat Days', 12, 'delete_pubstatdaysmodel');
INSERT INTO "public"."auth_permission" VALUES (48, 'Can view Stat Days', 12, 'view_pubstatdaysmodel');
INSERT INTO "public"."auth_permission" VALUES (49, 'Can add Stat Month', 13, 'add_pubstatmonthmodel');
INSERT INTO "public"."auth_permission" VALUES (50, 'Can change Stat Month', 13, 'change_pubstatmonthmodel');
INSERT INTO "public"."auth_permission" VALUES (51, 'Can delete Stat Month', 13, 'delete_pubstatmonthmodel');
INSERT INTO "public"."auth_permission" VALUES (52, 'Can view Stat Month', 13, 'view_pubstatmonthmodel');
INSERT INTO "public"."auth_permission" VALUES (53, 'Can add Stat Week', 14, 'add_pubstatweeksmodel');
INSERT INTO "public"."auth_permission" VALUES (54, 'Can change Stat Week', 14, 'change_pubstatweeksmodel');
INSERT INTO "public"."auth_permission" VALUES (55, 'Can delete Stat Week', 14, 'delete_pubstatweeksmodel');
INSERT INTO "public"."auth_permission" VALUES (56, 'Can view Stat Week', 14, 'view_pubstatweeksmodel');
INSERT INTO "public"."auth_permission" VALUES (58, 'Can add user dashboard module', 16, 'add_userdashboardmodule');
INSERT INTO "public"."auth_permission" VALUES (59, 'Can change user dashboard module', 16, 'change_userdashboardmodule');
INSERT INTO "public"."auth_permission" VALUES (60, 'Can delete user dashboard module', 16, 'delete_userdashboardmodule');
INSERT INTO "public"."auth_permission" VALUES (61, 'Can view user dashboard module', 16, 'view_userdashboardmodule');
INSERT INTO "public"."auth_permission" VALUES (62, 'Can add Cronjob Set', 17, 'add_cronjobmodel');
INSERT INTO "public"."auth_permission" VALUES (63, 'Can change Cronjob Set', 17, 'change_cronjobmodel');
INSERT INTO "public"."auth_permission" VALUES (64, 'Can delete Cronjob Set', 17, 'delete_cronjobmodel');
INSERT INTO "public"."auth_permission" VALUES (65, 'Can view Cronjob Set', 17, 'view_cronjobmodel');
INSERT INTO "public"."auth_permission" VALUES (66, 'Can add Task List', 18, 'add_cronjobjobstoremodel');
INSERT INTO "public"."auth_permission" VALUES (67, 'Can change Task List', 18, 'change_cronjobjobstoremodel');
INSERT INTO "public"."auth_permission" VALUES (68, 'Can delete Task List', 18, 'delete_cronjobjobstoremodel');
INSERT INTO "public"."auth_permission" VALUES (69, 'Can view Task List', 18, 'view_cronjobjobstoremodel');
INSERT INTO "public"."auth_permission" VALUES (70, 'Can add Logs for Run', 19, 'add_cronjoblogsmodel');
INSERT INTO "public"."auth_permission" VALUES (71, 'Can change Logs for Run', 19, 'change_cronjoblogsmodel');
INSERT INTO "public"."auth_permission" VALUES (72, 'Can delete Logs for Run', 19, 'delete_cronjoblogsmodel');
INSERT INTO "public"."auth_permission" VALUES (73, 'Can view Logs for Run', 19, 'view_cronjoblogsmodel');
INSERT INTO "public"."auth_permission" VALUES (74, 'Can add Logs for Load', 20, 'add_cronjobstatemodel');
INSERT INTO "public"."auth_permission" VALUES (75, 'Can change Logs for Load', 20, 'change_cronjobstatemodel');
INSERT INTO "public"."auth_permission" VALUES (76, 'Can delete Logs for Load', 20, 'delete_cronjobstatemodel');
INSERT INTO "public"."auth_permission" VALUES (77, 'Can view Logs for Load', 20, 'view_cronjobstatemodel');
INSERT INTO "public"."auth_permission" VALUES (78, 'Can add Cronjob Config', 21, 'add_cronjobconfigmodel');
INSERT INTO "public"."auth_permission" VALUES (79, 'Can change Cronjob Config', 21, 'change_cronjobconfigmodel');
INSERT INTO "public"."auth_permission" VALUES (80, 'Can delete Cronjob Config', 21, 'delete_cronjobconfigmodel');
INSERT INTO "public"."auth_permission" VALUES (81, 'Can view Cronjob Config', 21, 'view_cronjobconfigmodel');
INSERT INTO "public"."auth_permission" VALUES (82, 'Can add stat amazon sku buy box day dv', 22, 'add_statamazonskubuyboxdaydv');
INSERT INTO "public"."auth_permission" VALUES (83, 'Can change stat amazon sku buy box day dv', 22, 'change_statamazonskubuyboxdaydv');
INSERT INTO "public"."auth_permission" VALUES (84, 'Can delete stat amazon sku buy box day dv', 22, 'delete_statamazonskubuyboxdaydv');
INSERT INTO "public"."auth_permission" VALUES (85, 'Can view stat amazon sku buy box day dv', 22, 'view_statamazonskubuyboxdaydv');
INSERT INTO "public"."auth_permission" VALUES (86, 'Can add stat amazon sku pv day dv', 23, 'add_statamazonskupvdaydv');
INSERT INTO "public"."auth_permission" VALUES (87, 'Can change stat amazon sku pv day dv', 23, 'change_statamazonskupvdaydv');
INSERT INTO "public"."auth_permission" VALUES (88, 'Can delete stat amazon sku pv day dv', 23, 'delete_statamazonskupvdaydv');
INSERT INTO "public"."auth_permission" VALUES (89, 'Can view stat amazon sku pv day dv', 23, 'view_statamazonskupvdaydv');
INSERT INTO "public"."auth_permission" VALUES (90, 'Can add stat amazon sku pv month dv', 24, 'add_statamazonskupvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (91, 'Can change stat amazon sku pv month dv', 24, 'change_statamazonskupvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (92, 'Can delete stat amazon sku pv month dv', 24, 'delete_statamazonskupvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (93, 'Can view stat amazon sku pv month dv', 24, 'view_statamazonskupvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (94, 'Can add stat amazon sku pv week dv', 25, 'add_statamazonskupvweekdv');
INSERT INTO "public"."auth_permission" VALUES (95, 'Can change stat amazon sku pv week dv', 25, 'change_statamazonskupvweekdv');
INSERT INTO "public"."auth_permission" VALUES (96, 'Can delete stat amazon sku pv week dv', 25, 'delete_statamazonskupvweekdv');
INSERT INTO "public"."auth_permission" VALUES (97, 'Can view stat amazon sku pv week dv', 25, 'view_statamazonskupvweekdv');
INSERT INTO "public"."auth_permission" VALUES (98, 'Can add stat amazon sku total items day dv', 26, 'add_statamazonskutotalitemsdaydv');
INSERT INTO "public"."auth_permission" VALUES (99, 'Can change stat amazon sku total items day dv', 26, 'change_statamazonskutotalitemsdaydv');
INSERT INTO "public"."auth_permission" VALUES (100, 'Can delete stat amazon sku total items day dv', 26, 'delete_statamazonskutotalitemsdaydv');
INSERT INTO "public"."auth_permission" VALUES (101, 'Can view stat amazon sku total items day dv', 26, 'view_statamazonskutotalitemsdaydv');
INSERT INTO "public"."auth_permission" VALUES (102, 'Can add stat amazon sku total items month dv', 27, 'add_statamazonskutotalitemsmonthdv');
INSERT INTO "public"."auth_permission" VALUES (103, 'Can change stat amazon sku total items month dv', 27, 'change_statamazonskutotalitemsmonthdv');
INSERT INTO "public"."auth_permission" VALUES (104, 'Can delete stat amazon sku total items month dv', 27, 'delete_statamazonskutotalitemsmonthdv');
INSERT INTO "public"."auth_permission" VALUES (105, 'Can view stat amazon sku total items month dv', 27, 'view_statamazonskutotalitemsmonthdv');
INSERT INTO "public"."auth_permission" VALUES (106, 'Can add stat amazon sku total items week dv', 28, 'add_statamazonskutotalitemsweekdv');
INSERT INTO "public"."auth_permission" VALUES (107, 'Can change stat amazon sku total items week dv', 28, 'change_statamazonskutotalitemsweekdv');
INSERT INTO "public"."auth_permission" VALUES (108, 'Can delete stat amazon sku total items week dv', 28, 'delete_statamazonskutotalitemsweekdv');
INSERT INTO "public"."auth_permission" VALUES (109, 'Can view stat amazon sku total items week dv', 28, 'view_statamazonskutotalitemsweekdv');
INSERT INTO "public"."auth_permission" VALUES (110, 'Can add stat amazon sku uv day dv', 29, 'add_statamazonskuuvdaydv');
INSERT INTO "public"."auth_permission" VALUES (111, 'Can change stat amazon sku uv day dv', 29, 'change_statamazonskuuvdaydv');
INSERT INTO "public"."auth_permission" VALUES (112, 'Can delete stat amazon sku uv day dv', 29, 'delete_statamazonskuuvdaydv');
INSERT INTO "public"."auth_permission" VALUES (113, 'Can view stat amazon sku uv day dv', 29, 'view_statamazonskuuvdaydv');
INSERT INTO "public"."auth_permission" VALUES (114, 'Can add stat amazon sku uv month dv', 30, 'add_statamazonskuuvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (115, 'Can change stat amazon sku uv month dv', 30, 'change_statamazonskuuvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (116, 'Can delete stat amazon sku uv month dv', 30, 'delete_statamazonskuuvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (117, 'Can view stat amazon sku uv month dv', 30, 'view_statamazonskuuvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (118, 'Can add stat amazon sku uv week dv', 31, 'add_statamazonskuuvweekdv');
INSERT INTO "public"."auth_permission" VALUES (119, 'Can change stat amazon sku uv week dv', 31, 'change_statamazonskuuvweekdv');
INSERT INTO "public"."auth_permission" VALUES (120, 'Can delete stat amazon sku uv week dv', 31, 'delete_statamazonskuuvweekdv');
INSERT INTO "public"."auth_permission" VALUES (121, 'Can view stat amazon sku uv week dv', 31, 'view_statamazonskuuvweekdv');
INSERT INTO "public"."auth_permission" VALUES (122, 'Can add Product Category', 32, 'add_productcategorymodel');
INSERT INTO "public"."auth_permission" VALUES (123, 'Can change Product Category', 32, 'change_productcategorymodel');
INSERT INTO "public"."auth_permission" VALUES (124, 'Can delete Product Category', 32, 'delete_productcategorymodel');
INSERT INTO "public"."auth_permission" VALUES (125, 'Can view Product Category', 32, 'view_productcategorymodel');
INSERT INTO "public"."auth_permission" VALUES (126, 'Can add Product Line', 33, 'add_productlinemodel');
INSERT INTO "public"."auth_permission" VALUES (127, 'Can change Product Line', 33, 'change_productlinemodel');
INSERT INTO "public"."auth_permission" VALUES (128, 'Can delete Product Line', 33, 'delete_productlinemodel');
INSERT INTO "public"."auth_permission" VALUES (129, 'Can view Product Line', 33, 'view_productlinemodel');
INSERT INTO "public"."auth_permission" VALUES (130, 'Can add stat amazon line buy box day dv', 34, 'add_statamazonlinebuyboxdaydv');
INSERT INTO "public"."auth_permission" VALUES (131, 'Can change stat amazon line buy box day dv', 34, 'change_statamazonlinebuyboxdaydv');
INSERT INTO "public"."auth_permission" VALUES (132, 'Can delete stat amazon line buy box day dv', 34, 'delete_statamazonlinebuyboxdaydv');
INSERT INTO "public"."auth_permission" VALUES (133, 'Can view stat amazon line buy box day dv', 34, 'view_statamazonlinebuyboxdaydv');
INSERT INTO "public"."auth_permission" VALUES (134, 'Can add stat amazon line pv day dv', 35, 'add_statamazonlinepvdaydv');
INSERT INTO "public"."auth_permission" VALUES (135, 'Can change stat amazon line pv day dv', 35, 'change_statamazonlinepvdaydv');
INSERT INTO "public"."auth_permission" VALUES (136, 'Can delete stat amazon line pv day dv', 35, 'delete_statamazonlinepvdaydv');
INSERT INTO "public"."auth_permission" VALUES (137, 'Can view stat amazon line pv day dv', 35, 'view_statamazonlinepvdaydv');
INSERT INTO "public"."auth_permission" VALUES (138, 'Can add stat amazon line pv month dv', 36, 'add_statamazonlinepvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (139, 'Can change stat amazon line pv month dv', 36, 'change_statamazonlinepvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (140, 'Can delete stat amazon line pv month dv', 36, 'delete_statamazonlinepvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (141, 'Can view stat amazon line pv month dv', 36, 'view_statamazonlinepvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (142, 'Can add stat amazon line pv week dv', 37, 'add_statamazonlinepvweekdv');
INSERT INTO "public"."auth_permission" VALUES (143, 'Can change stat amazon line pv week dv', 37, 'change_statamazonlinepvweekdv');
INSERT INTO "public"."auth_permission" VALUES (144, 'Can delete stat amazon line pv week dv', 37, 'delete_statamazonlinepvweekdv');
INSERT INTO "public"."auth_permission" VALUES (145, 'Can view stat amazon line pv week dv', 37, 'view_statamazonlinepvweekdv');
INSERT INTO "public"."auth_permission" VALUES (146, 'Can add stat amazon line total items day dv', 38, 'add_statamazonlinetotalitemsdaydv');
INSERT INTO "public"."auth_permission" VALUES (147, 'Can change stat amazon line total items day dv', 38, 'change_statamazonlinetotalitemsdaydv');
INSERT INTO "public"."auth_permission" VALUES (148, 'Can delete stat amazon line total items day dv', 38, 'delete_statamazonlinetotalitemsdaydv');
INSERT INTO "public"."auth_permission" VALUES (149, 'Can view stat amazon line total items day dv', 38, 'view_statamazonlinetotalitemsdaydv');
INSERT INTO "public"."auth_permission" VALUES (150, 'Can add stat amazon line total items month dv', 39, 'add_statamazonlinetotalitemsmonthdv');
INSERT INTO "public"."auth_permission" VALUES (151, 'Can change stat amazon line total items month dv', 39, 'change_statamazonlinetotalitemsmonthdv');
INSERT INTO "public"."auth_permission" VALUES (152, 'Can delete stat amazon line total items month dv', 39, 'delete_statamazonlinetotalitemsmonthdv');
INSERT INTO "public"."auth_permission" VALUES (153, 'Can view stat amazon line total items month dv', 39, 'view_statamazonlinetotalitemsmonthdv');
INSERT INTO "public"."auth_permission" VALUES (154, 'Can add stat amazon line total items week dv', 40, 'add_statamazonlinetotalitemsweekdv');
INSERT INTO "public"."auth_permission" VALUES (155, 'Can change stat amazon line total items week dv', 40, 'change_statamazonlinetotalitemsweekdv');
INSERT INTO "public"."auth_permission" VALUES (156, 'Can delete stat amazon line total items week dv', 40, 'delete_statamazonlinetotalitemsweekdv');
INSERT INTO "public"."auth_permission" VALUES (157, 'Can view stat amazon line total items week dv', 40, 'view_statamazonlinetotalitemsweekdv');
INSERT INTO "public"."auth_permission" VALUES (158, 'Can add stat amazon line uv day dv', 41, 'add_statamazonlineuvdaydv');
INSERT INTO "public"."auth_permission" VALUES (159, 'Can change stat amazon line uv day dv', 41, 'change_statamazonlineuvdaydv');
INSERT INTO "public"."auth_permission" VALUES (160, 'Can delete stat amazon line uv day dv', 41, 'delete_statamazonlineuvdaydv');
INSERT INTO "public"."auth_permission" VALUES (161, 'Can view stat amazon line uv day dv', 41, 'view_statamazonlineuvdaydv');
INSERT INTO "public"."auth_permission" VALUES (162, 'Can add stat amazon line uv items conversion rate day dv', 42, 'add_statamazonlineuvitemsconversionratedaydv');
INSERT INTO "public"."auth_permission" VALUES (163, 'Can change stat amazon line uv items conversion rate day dv', 42, 'change_statamazonlineuvitemsconversionratedaydv');
INSERT INTO "public"."auth_permission" VALUES (164, 'Can delete stat amazon line uv items conversion rate day dv', 42, 'delete_statamazonlineuvitemsconversionratedaydv');
INSERT INTO "public"."auth_permission" VALUES (165, 'Can view stat amazon line uv items conversion rate day dv', 42, 'view_statamazonlineuvitemsconversionratedaydv');
INSERT INTO "public"."auth_permission" VALUES (166, 'Can add stat amazon line uv month dv', 43, 'add_statamazonlineuvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (167, 'Can change stat amazon line uv month dv', 43, 'change_statamazonlineuvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (168, 'Can delete stat amazon line uv month dv', 43, 'delete_statamazonlineuvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (169, 'Can view stat amazon line uv month dv', 43, 'view_statamazonlineuvmonthdv');
INSERT INTO "public"."auth_permission" VALUES (170, 'Can add stat amazon line uv week dv', 44, 'add_statamazonlineuvweekdv');
INSERT INTO "public"."auth_permission" VALUES (171, 'Can change stat amazon line uv week dv', 44, 'change_statamazonlineuvweekdv');
INSERT INTO "public"."auth_permission" VALUES (172, 'Can delete stat amazon line uv week dv', 44, 'delete_statamazonlineuvweekdv');
INSERT INTO "public"."auth_permission" VALUES (173, 'Can view stat amazon line uv week dv', 44, 'view_statamazonlineuvweekdv');
INSERT INTO "public"."auth_permission" VALUES (174, 'Can add Data Dictionary', 45, 'add_datadictionary');
INSERT INTO "public"."auth_permission" VALUES (175, 'Can change Data Dictionary', 45, 'change_datadictionary');
INSERT INTO "public"."auth_permission" VALUES (176, 'Can delete Data Dictionary', 45, 'delete_datadictionary');
INSERT INTO "public"."auth_permission" VALUES (177, 'Can view Data Dictionary', 45, 'view_datadictionary');
INSERT INTO "public"."auth_permission" VALUES (178, 'Can add Data Dictionary Value', 46, 'add_datadictionaryvalue');
INSERT INTO "public"."auth_permission" VALUES (179, 'Can change Data Dictionary Value', 46, 'change_datadictionaryvalue');
INSERT INTO "public"."auth_permission" VALUES (180, 'Can delete Data Dictionary Value', 46, 'delete_datadictionaryvalue');
INSERT INTO "public"."auth_permission" VALUES (181, 'Can view Data Dictionary Value', 46, 'view_datadictionaryvalue');
INSERT INTO "public"."auth_permission" VALUES (182, 'Can add Data Dictionary Category', 47, 'add_datadictionarycategory');
INSERT INTO "public"."auth_permission" VALUES (183, 'Can change Data Dictionary Category', 47, 'change_datadictionarycategory');
INSERT INTO "public"."auth_permission" VALUES (184, 'Can delete Data Dictionary Category', 47, 'delete_datadictionarycategory');
INSERT INTO "public"."auth_permission" VALUES (185, 'Can view Data Dictionary Category', 47, 'view_datadictionarycategory');
INSERT INTO "public"."auth_permission" VALUES (186, 'Can add Data Dictionary Category', 48, 'add_datadictionarycategorymodel');
INSERT INTO "public"."auth_permission" VALUES (187, 'Can change Data Dictionary Category', 48, 'change_datadictionarycategorymodel');
INSERT INTO "public"."auth_permission" VALUES (188, 'Can delete Data Dictionary Category', 48, 'delete_datadictionarycategorymodel');
INSERT INTO "public"."auth_permission" VALUES (189, 'Can view Data Dictionary Category', 48, 'view_datadictionarycategorymodel');
INSERT INTO "public"."auth_permission" VALUES (190, 'Can add Data Dictionary', 49, 'add_datadictionarymodel');
INSERT INTO "public"."auth_permission" VALUES (191, 'Can change Data Dictionary', 49, 'change_datadictionarymodel');
INSERT INTO "public"."auth_permission" VALUES (192, 'Can delete Data Dictionary', 49, 'delete_datadictionarymodel');
INSERT INTO "public"."auth_permission" VALUES (193, 'Can view Data Dictionary', 49, 'view_datadictionarymodel');
INSERT INTO "public"."auth_permission" VALUES (194, 'Can add Data Dictionary Value', 50, 'add_datadictionaryvaluemodel');
INSERT INTO "public"."auth_permission" VALUES (195, 'Can change Data Dictionary Value', 50, 'change_datadictionaryvaluemodel');
INSERT INTO "public"."auth_permission" VALUES (196, 'Can delete Data Dictionary Value', 50, 'delete_datadictionaryvaluemodel');
INSERT INTO "public"."auth_permission" VALUES (197, 'Can view Data Dictionary Value', 50, 'view_datadictionaryvaluemodel');
INSERT INTO "public"."auth_permission" VALUES (199, '1', 2, '1');
INSERT INTO "public"."auth_permission" VALUES (200, 'Can add cors model', 51, 'add_corsmodel');
INSERT INTO "public"."auth_permission" VALUES (201, 'Can change cors model', 51, 'change_corsmodel');
INSERT INTO "public"."auth_permission" VALUES (202, 'Can delete cors model', 51, 'delete_corsmodel');
INSERT INTO "public"."auth_permission" VALUES (203, 'Can view cors model', 51, 'view_corsmodel');
INSERT INTO "public"."auth_permission" VALUES (204, 'Can add Token', 52, 'add_token');
INSERT INTO "public"."auth_permission" VALUES (205, 'Can change Token', 52, 'change_token');
INSERT INTO "public"."auth_permission" VALUES (206, 'Can delete Token', 52, 'delete_token');
INSERT INTO "public"."auth_permission" VALUES (207, 'Can view Token', 52, 'view_token');
INSERT INTO "public"."auth_permission" VALUES (208, 'Can add User Profile', 53, 'add_userprofilemodel');
INSERT INTO "public"."auth_permission" VALUES (209, 'Can change User Profile', 53, 'change_userprofilemodel');
INSERT INTO "public"."auth_permission" VALUES (210, 'Can delete User Profile', 53, 'delete_userprofilemodel');
INSERT INTO "public"."auth_permission" VALUES (211, 'Can view User Profile', 53, 'view_userprofilemodel');
INSERT INTO "public"."auth_permission" VALUES (212, 'Can add Token', 54, 'add_tokenmodel');
INSERT INTO "public"."auth_permission" VALUES (213, 'Can change Token', 54, 'change_tokenmodel');
INSERT INTO "public"."auth_permission" VALUES (214, 'Can delete Token', 54, 'delete_tokenmodel');
INSERT INTO "public"."auth_permission" VALUES (215, 'Can view Token', 54, 'view_tokenmodel');
INSERT INTO "public"."auth_permission" VALUES (216, 'Can add Group Profile', 55, 'add_groupprofilemodel');
INSERT INTO "public"."auth_permission" VALUES (217, 'Can change Group Profile', 55, 'change_groupprofilemodel');
INSERT INTO "public"."auth_permission" VALUES (218, 'Can delete Group Profile', 55, 'delete_groupprofilemodel');
INSERT INTO "public"."auth_permission" VALUES (219, 'Can view Group Profile', 55, 'view_groupprofilemodel');
INSERT INTO "public"."auth_permission" VALUES (220, 'Can add Dict', 56, 'add_datadictionarymodel');
INSERT INTO "public"."auth_permission" VALUES (221, 'Can change Dict', 56, 'change_datadictionarymodel');
INSERT INTO "public"."auth_permission" VALUES (222, 'Can delete Dict', 56, 'delete_datadictionarymodel');
INSERT INTO "public"."auth_permission" VALUES (223, 'Can view Dict', 56, 'view_datadictionarymodel');
INSERT INTO "public"."auth_permission" VALUES (224, 'Can add Dict Value', 57, 'add_datadictionaryvaluemodel');
INSERT INTO "public"."auth_permission" VALUES (225, 'Can change Dict Value', 57, 'change_datadictionaryvaluemodel');
INSERT INTO "public"."auth_permission" VALUES (226, 'Can delete Dict Value', 57, 'delete_datadictionaryvaluemodel');
INSERT INTO "public"."auth_permission" VALUES (227, 'Can view Dict Value', 57, 'view_datadictionaryvaluemodel');
INSERT INTO "public"."auth_permission" VALUES (228, 'Can add Dict Category', 58, 'add_datadictionarycategorymodel');
INSERT INTO "public"."auth_permission" VALUES (229, 'Can change Dict Category', 58, 'change_datadictionarycategorymodel');
INSERT INTO "public"."auth_permission" VALUES (230, 'Can delete Dict Category', 58, 'delete_datadictionarycategorymodel');
INSERT INTO "public"."auth_permission" VALUES (231, 'Can view Dict Category', 58, 'view_datadictionarycategorymodel');

-- ----------------------------
-- Table structure for auth_token
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_token";
CREATE TABLE "public"."auth_token" (
  "key" varchar(40) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "updated_at" timestamptz(6) DEFAULT NULL,
  "created_at" timestamptz(6) DEFAULT NULL,
  "user_id" int4 NOT NULL DEFAULT NULL
)
;

-- ----------------------------
-- Table structure for auth_user_profile
-- ----------------------------
DROP TABLE IF EXISTS "public"."auth_user_profile";
CREATE TABLE "public"."auth_user_profile" (
  "id" int4 NOT NULL DEFAULT nextval('auth_user_profile_id_seq'::regclass),
  "nick" varchar(100) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "ding_talk_account" varchar(100) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "updated_at" timestamptz(6) DEFAULT NULL,
  "created_at" timestamptz(6) DEFAULT NULL,
  "is_delete" int4 DEFAULT NULL,
  "user_id" int4 NOT NULL DEFAULT NULL
)
;

-- ----------------------------
-- Table structure for na_cronjob
-- ----------------------------
DROP TABLE IF EXISTS "public"."na_cronjob";
CREATE TABLE "public"."na_cronjob" (
  "id" int4 NOT NULL DEFAULT nextval('na_cronjob_id_seq'::regclass),
  "type" int4 NOT NULL DEFAULT NULL,
  "code" varchar(50) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "title" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "yr" varchar(100) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "mo" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "dy" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "wk" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "dy_of_week" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "hr" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "mi" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "se" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "start_date" timestamptz(6) DEFAULT NULL,
  "end_date" timestamptz(6) DEFAULT NULL,
  "timezone" varchar(100) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "status" int4 NOT NULL DEFAULT NULL,
  "updated_at" timestamptz(6) DEFAULT NULL,
  "created_at" timestamptz(6) DEFAULT NULL,
  "command" text COLLATE "pg_catalog"."default" DEFAULT NULL,
  "creator_id" int4 DEFAULT NULL,
  "command_type" int4 DEFAULT NULL
)
;

-- ----------------------------
-- Records of na_cronjob
-- ----------------------------
INSERT INTO "public"."na_cronjob" VALUES (6, 2, 'RUN_CMD', 'Runcmd', '*', '*', '*', '*', '*', '*', '*/2', '*', '2019-04-26 13:25:00+08', '2019-04-26 20:40:00+08', 'Asia/Shanghai', 1, '2019-04-26 17:41:19.515+08', '2019-04-26 16:28:07.2616+08', 'appfront.cronjobs.LocalScrapydAPI.createJob()', 1, 1);

-- ----------------------------
-- Table structure for na_cronjob_job_config
-- ----------------------------
DROP TABLE IF EXISTS "public"."na_cronjob_job_config";
CREATE TABLE "public"."na_cronjob_job_config" (
  "id" int4 NOT NULL DEFAULT nextval('na_cronjob_job_config_id_seq'::regclass),
  "key" varchar(50) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "name" varchar(100) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "value" varchar(100) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "updated_at" timestamptz(6) DEFAULT NULL,
  "created_at" timestamptz(6) DEFAULT NULL,
  "creator_id" int4 DEFAULT NULL
)
;

-- ----------------------------
-- Records of na_cronjob_job_config
-- ----------------------------
INSERT INTO "public"."na_cronjob_job_config" VALUES (1, 'pool_thread', 'Max Thread for Pool', '30', '2019-04-09 19:27:34.9618+08', '2019-04-09 19:27:34.9618+08', NULL);
INSERT INTO "public"."na_cronjob_job_config" VALUES (2, 'pool_process', 'Max Process for Pool', '15', '2019-04-09 19:27:34.9618+08', '2019-04-09 19:27:34.9618+08', NULL);
INSERT INTO "public"."na_cronjob_job_config" VALUES (3, 'job_coalesce', 'Job Coalesce', 'Flase', '2019-04-09 19:27:34.9618+08', '2019-04-09 19:27:34.9618+08', NULL);
INSERT INTO "public"."na_cronjob_job_config" VALUES (4, 'job_max_instances', 'Job Max Instances', '5', '2019-04-09 19:27:34.9618+08', '2019-04-09 19:27:34.9618+08', NULL);

-- ----------------------------
-- Table structure for na_cronjob_job_store
-- ----------------------------
DROP TABLE IF EXISTS "public"."na_cronjob_job_store";
CREATE TABLE "public"."na_cronjob_job_store" (
  "id" int4 NOT NULL DEFAULT nextval('na_cronjob_job_store_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT NULL,
  "next_run_time" timestamptz(6) DEFAULT NULL,
  "job_state" bytea NOT NULL DEFAULT NULL,
  "updated_at" timestamptz(6) DEFAULT NULL,
  "created_at" timestamptz(6) DEFAULT NULL
)
;

-- ----------------------------
-- Records of na_cronjob_job_store
-- ----------------------------
INSERT INTO "public"."na_cronjob_job_store" VALUES (20, 'ID-6:RUN_CMD:Runcmd', NULL, E'\\200\\004\\225\\353\\005\\000\\000\\000\\000\\000\\000}\\224(\\214\\007version\\224K\\001\\214\\002id\\224\\214\\023ID-6:RUN_CMD:Runcmd\\224\\214\\004func\\224\\214,cronjob.libs.cronjob_util:JobInstance.runJob\\224\\214\\007trigger\\224\\214\\031apscheduler.triggers.cron\\224\\214\\013CronTrigger\\224\\223\\224)\\201\\224}\\224(h\\001K\\002\\214\\010timezone\\224\\214\\004pytz\\224\\214\\004_UTC\\224\\223\\224)R\\224\\214\\012start_date\\224\\214\\010datetime\\224\\214\\010datetime\\224\\223\\224C\\012\\007\\343\\004\\032\\005\\031\\000\\000\\000\\000\\224h\\020\\206\\224R\\224\\214\\010end_date\\224h\\024C\\012\\007\\343\\004\\032\\014(\\000\\000\\000\\000\\224h\\020\\206\\224R\\224\\214\\006fields\\224]\\224(\\214 apscheduler.triggers.cron.fields\\224\\214\\011BaseField\\224\\223\\224)\\201\\224}\\224(\\214\\004name\\224\\214\\004year\\224\\214\\012is_default\\224\\211\\214\\013expressions\\224]\\224\\214%apscheduler.triggers.cron.expressions\\224\\214\\015AllExpression\\224\\223\\224)\\201\\224}\\224\\214\\004step\\224Nsbaubh\\036\\214\\012MonthField\\224\\223\\224)\\201\\224}\\224(h#\\214\\005month\\224h%\\211h&]\\224h*)\\201\\224}\\224h-Nsbaubh\\036\\214\\017DayOfMonthField\\224\\223\\224)\\201\\224}\\224(h#\\214\\003day\\224h%\\211h&]\\224h*)\\201\\224}\\224h-Nsbaubh\\036\\214\\011WeekField\\224\\223\\224)\\201\\224}\\224(h#\\214\\004week\\224h%\\211h&]\\224h*)\\201\\224}\\224h-Nsbaubh\\036\\214\\016DayOfWeekField\\224\\223\\224)\\201\\224}\\224(h#\\214\\013day_of_week\\224h%\\211h&]\\224h*)\\201\\224}\\224h-Nsbaubh )\\201\\224}\\224(h#\\214\\004hour\\224h%\\211h&]\\224h*)\\201\\224}\\224h-Nsbaubh )\\201\\224}\\224(h#\\214\\006minute\\224h%\\211h&]\\224h*)\\201\\224}\\224h-K\\002sbaubh )\\201\\224}\\224(h#\\214\\006second\\224h%\\211h&]\\224h*)\\201\\224}\\224h-Nsbaube\\214\\006jitter\\224Nub\\214\\010executor\\224\\214\\007default\\224\\214\\004args\\224\\214\\031cronjob.libs.cronjob_util\\224\\214\\013JobInstance\\224\\223\\224)\\201\\224}\\224(\\214\\003job\\224\\214\\025django.db.models.base\\224\\214\\016model_unpickle\\224\\223\\224\\214\\007cronjob\\224\\214\\014CronjobModel\\224\\206\\224\\205\\224R\\224}\\224(\\214\\006_state\\224hj\\214\\012ModelState\\224\\223\\224)\\201\\224}\\224(\\214\\006adding\\224\\211\\214\\002db\\224hbubh\\002K\\006\\214\\004type\\224K\\002\\214\\004code\\224\\214\\007RUN_CMD\\224\\214\\005title\\224\\214\\006Runcmd\\224\\214\\002yr\\224\\214\\001*\\224\\214\\002mo\\224h\\200\\214\\002dy\\224h\\200\\214\\002wk\\224h\\200\\214\\012dy_of_week\\224h\\200\\214\\002hr\\224h\\200\\214\\002mi\\224\\214\\003*/2\\224\\214\\002se\\224h\\200h\\021h\\027h\\030h\\033h\\014\\214\\015Asia/Shanghai\\224\\214\\006status\\224K\\001\\214\\007command\\224\\214-appfront.cronjobs.LocalScrapydAPI.createJob()\\224\\214\\014command_type\\224K\\001\\214\\012updated_at\\224h\\024C\\012\\007\\343\\004\\032\\011)\\023\\007\\333\\270\\224h\\020\\206\\224R\\224\\214\\012created_at\\224h\\024C\\012\\007\\343\\004\\032\\010\\034\\007\\003\\375\\340\\224h\\020\\206\\224R\\224\\214\\012creator_id\\224K\\001\\214\\017_django_version\\224\\214\\0032.2\\224ubh\\002K\\006h{h|h}h~hzK\\002h\\213h\\214h\\215K\\001ub\\205\\224\\214\\006kwargs\\224}\\224h#\\214\\022JobInstance.runJob\\224\\214\\022misfire_grace_time\\224K\\001\\214\\010coalesce\\224\\211\\214\\015max_instances\\224K\\005\\214\\015next_run_time\\224Nu.', '2019-05-15 18:32:01.4642+08', '2019-04-30 08:17:17.2264+08');

-- ----------------------------
-- Table structure for na_cronjob_logs
-- ----------------------------
DROP TABLE IF EXISTS "public"."na_cronjob_logs";
CREATE TABLE "public"."na_cronjob_logs" (
  "id" int4 NOT NULL DEFAULT nextval('na_cronjob_logs_id_seq'::regclass),
  "status" int4 NOT NULL DEFAULT NULL,
  "content" text COLLATE "pg_catalog"."default" DEFAULT NULL,
  "process" varchar(100) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "thread" int4 DEFAULT NULL,
  "time_long" float8 NOT NULL DEFAULT NULL,
  "date_begin" timestamptz(6) DEFAULT NULL,
  "date_end" timestamptz(6) DEFAULT NULL,
  "created_at" timestamptz(6) DEFAULT NULL,
  "cronjob_id" int4 DEFAULT NULL
)
;

-- ----------------------------
-- Records of na_cronjob_logs
-- ----------------------------
INSERT INTO "public"."na_cronjob_logs" VALUES (123, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 2, '2019-04-26 17:05:00.0726+08', '2019-04-26 17:05:02.4756+08', '2019-04-26 17:05:02.5126+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (124, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 5, '2019-04-26 17:05:01.0116+08', '2019-04-26 17:05:06.2646+08', '2019-04-26 17:05:06.3156+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (125, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 6, '2019-04-26 17:05:02.0066+08', '2019-04-26 17:05:08.1426+08', '2019-04-26 17:05:08.1816+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (126, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 7, '2019-04-26 17:05:03.0076+08', '2019-04-26 17:05:10.0616+08', '2019-04-26 17:05:10.0976+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (127, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 7, '2019-04-26 17:05:04.0086+08', '2019-04-26 17:05:11.9356+08', '2019-04-26 17:05:11.9356+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (128, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:05:05.0076+08', '2019-04-26 17:05:13.8206+08', '2019-04-26 17:05:13.8606+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (129, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:05:07.0076+08', '2019-04-26 17:05:15.8836+08', '2019-04-26 17:05:15.9296+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (130, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:05:09.0156+08', '2019-04-26 17:05:17.8136+08', '2019-04-26 17:05:17.8576+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (131, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:05:11.0076+08', '2019-04-26 17:05:19.6996+08', '2019-04-26 17:05:19.6996+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (132, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:12.0086+08', '2019-04-26 17:05:21.7946+08', '2019-04-26 17:05:21.8326+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (133, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:14.0056+08', '2019-04-26 17:05:23.6766+08', '2019-04-26 17:05:23.6766+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (134, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:16.0396+08', '2019-04-26 17:05:25.6656+08', '2019-04-26 17:05:25.6656+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (135, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:18.0116+08', '2019-04-26 17:05:27.5996+08', '2019-04-26 17:05:27.6436+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (136, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:20.0106+08', '2019-04-26 17:05:29.5456+08', '2019-04-26 17:05:29.5846+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (137, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:22.0066+08', '2019-04-26 17:05:31.4916+08', '2019-04-26 17:05:31.4916+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (138, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:24.0086+08', '2019-04-26 17:05:33.3966+08', '2019-04-26 17:05:33.4356+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (139, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:26.0176+08', '2019-04-26 17:05:35.3276+08', '2019-04-26 17:05:35.3286+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (140, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 7, '2019-04-26 17:05:28.0106+08', '2019-04-26 17:05:35.3296+08', '2019-04-26 17:05:35.3296+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (141, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:30.0076+08', '2019-04-26 17:05:39.1806+08', '2019-04-26 17:05:39.2196+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (142, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:32.0096+08', '2019-04-26 17:05:41.0876+08', '2019-04-26 17:05:41.0876+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (143, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:34.0066+08', '2019-04-26 17:05:43.0156+08', '2019-04-26 17:05:43.0166+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (144, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:05:36.0116+08', '2019-04-26 17:05:44.9116+08', '2019-04-26 17:05:44.9126+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (145, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:37.0126+08', '2019-04-26 17:05:46.7826+08', '2019-04-26 17:05:46.8206+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (146, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:05:40.0126+08', '2019-04-26 17:05:48.6956+08', '2019-04-26 17:05:48.6966+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (147, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:05:42.0086+08', '2019-04-26 17:05:50.5896+08', '2019-04-26 17:05:50.6276+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (148, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:05:44.0176+08', '2019-04-26 17:05:52.5026+08', '2019-04-26 17:05:52.5026+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (149, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:45.0146+08', '2019-04-26 17:05:54.4116+08', '2019-04-26 17:05:54.4126+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (150, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:47.0146+08', '2019-04-26 17:05:56.3636+08', '2019-04-26 17:05:56.4156+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (151, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:49.0076+08', '2019-04-26 17:05:58.2466+08', '2019-04-26 17:05:58.2846+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (152, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:51.0116+08', '2019-04-26 17:06:00.1396+08', '2019-04-26 17:06:00.1406+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (153, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:05:53.0106+08', '2019-04-26 17:06:02.0136+08', '2019-04-26 17:06:02.0546+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (154, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:05:55.0166+08', '2019-04-26 17:06:03.9266+08', '2019-04-26 17:06:03.9646+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (155, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:05:57.0146+08', '2019-04-26 17:06:05.8176+08', '2019-04-26 17:06:05.8176+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (156, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 6, '2019-04-26 17:05:59.0086+08', '2019-04-26 17:06:05.8166+08', '2019-04-26 17:06:05.8576+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (157, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 2, '2019-04-26 17:42:00.01+08', '2019-04-26 17:42:02.198+08', '2019-04-26 17:42:02.241+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (158, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 3, '2019-04-26 17:42:01.009+08', '2019-04-26 17:42:04.091+08', '2019-04-26 17:42:04.131+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (159, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 5, '2019-04-26 17:42:02.007+08', '2019-04-26 17:42:07.829+08', '2019-04-26 17:42:07.872+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (160, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 6, '2019-04-26 17:42:03.007+08', '2019-04-26 17:42:09.777+08', '2019-04-26 17:42:09.777+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (161, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 7, '2019-04-26 17:42:04.008+08', '2019-04-26 17:42:11.648+08', '2019-04-26 17:42:11.689+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (162, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:42:05.007+08', '2019-04-26 17:42:13.526+08', '2019-04-26 17:42:13.564+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (163, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:42:06.008+08', '2019-04-26 17:42:15.415+08', '2019-04-26 17:42:15.452+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (164, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:42:08.01+08', '2019-04-26 17:42:17.303+08', '2019-04-26 17:42:17.345+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (165, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:42:10.008+08', '2019-04-26 17:42:19.184+08', '2019-04-26 17:42:19.184+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (166, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 17:42:12.011+08', '2019-04-26 17:42:21.091+08', '2019-04-26 17:42:21.131+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (167, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:42:14.007+08', '2019-04-26 17:42:22.99+08', '2019-04-26 17:42:23.036+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (168, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 17:42:16.006+08', '2019-04-26 17:42:24.895+08', '2019-04-26 17:42:24.896+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (169, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 3, '2019-04-26 17:42:22.021+08', '2019-04-26 17:42:25.203+08', '2019-04-26 17:42:25.203+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (170, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 1, '2019-04-26 17:42:24.021+08', '2019-04-26 17:42:25.218+08', '2019-04-26 17:42:25.219+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (171, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:42:25.022+08', '2019-04-26 17:42:25.204+08', '2019-04-26 17:42:25.258+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (172, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 5, '2019-04-26 17:42:20.006+08', '2019-04-26 17:42:25.217+08', '2019-04-26 17:42:25.281+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (173, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 7, '2019-04-26 17:42:18.018+08', '2019-04-26 17:42:25.207+08', '2019-04-26 17:42:25.282+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (174, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:00.054+08', '2019-04-26 17:44:00.21+08', '2019-04-26 17:44:00.246+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (175, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:01.014+08', '2019-04-26 17:44:01.128+08', '2019-04-26 17:44:01.128+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (176, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:02.019+08', '2019-04-26 17:44:02.119+08', '2019-04-26 17:44:02.166+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (177, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:03.009+08', '2019-04-26 17:44:03.117+08', '2019-04-26 17:44:03.156+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (178, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:04.02+08', '2019-04-26 17:44:04.118+08', '2019-04-26 17:44:04.118+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (179, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:05.006+08', '2019-04-26 17:44:05.106+08', '2019-04-26 17:44:05.107+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (180, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:06.019+08', '2019-04-26 17:44:06.121+08', '2019-04-26 17:44:06.161+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (181, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:07.012+08', '2019-04-26 17:44:07.112+08', '2019-04-26 17:44:07.112+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (182, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:08.015+08', '2019-04-26 17:44:08.12+08', '2019-04-26 17:44:08.161+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (183, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:09.02+08', '2019-04-26 17:44:09.123+08', '2019-04-26 17:44:09.162+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (184, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:10.01+08', '2019-04-26 17:44:10.109+08', '2019-04-26 17:44:10.109+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (185, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:11.012+08', '2019-04-26 17:44:11.121+08', '2019-04-26 17:44:11.157+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (186, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:12.019+08', '2019-04-26 17:44:12.122+08', '2019-04-26 17:44:12.161+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (187, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:13.008+08', '2019-04-26 17:44:13.119+08', '2019-04-26 17:44:13.12+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (188, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:14.022+08', '2019-04-26 17:44:14.126+08', '2019-04-26 17:44:14.168+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (189, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 0, '2019-04-26 17:44:15.022+08', '2019-04-26 17:44:15.123+08', '2019-04-26 17:44:15.124+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (190, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 2, '2019-04-26 18:04:27.048+08', '2019-04-26 18:04:29.374+08', '2019-04-26 18:04:29.412+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (191, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 5, '2019-04-26 18:04:28.019+08', '2019-04-26 18:04:33.276+08', '2019-04-26 18:04:33.322+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (192, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 6, '2019-04-26 18:04:29.028+08', '2019-04-26 18:04:35.169+08', '2019-04-26 18:04:35.208+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (193, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 7, '2019-04-26 18:04:30.01+08', '2019-04-26 18:04:37.051+08', '2019-04-26 18:04:37.092+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (201, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 2, '2019-04-26 18:04:45.006+08', '2019-04-26 18:04:47.166+08', '2019-04-26 18:04:47.166+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (194, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 7, '2019-04-26 18:04:31.023+08', '2019-04-26 18:04:39.017+08', '2019-04-26 18:04:39.017+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (195, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 18:04:32.045+08', '2019-04-26 18:04:40.915+08', '2019-04-26 18:04:40.956+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (196, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 18:04:34.008+08', '2019-04-26 18:04:42.85+08', '2019-04-26 18:04:42.889+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (200, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 4, '2019-04-26 18:04:43.013+08', '2019-04-26 18:04:47.162+08', '2019-04-26 18:04:47.163+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (197, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 8, '2019-04-26 18:04:36.007+08', '2019-04-26 18:04:44.787+08', '2019-04-26 18:04:44.788+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (198, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 5, '2019-04-26 18:04:41.023+08', '2019-04-26 18:04:46.662+08', '2019-04-26 18:04:46.7+08', 6);
INSERT INTO "public"."na_cronjob_logs" VALUES (199, 1, 'Complated Cronjob Runcmd: False', NULL, NULL, 9, '2019-04-26 18:04:38.018+08', '2019-04-26 18:04:47.161+08', '2019-04-26 18:04:47.162+08', 6);

-- ----------------------------
-- Table structure for na_cronjob_state
-- ----------------------------
DROP TABLE IF EXISTS "public"."na_cronjob_state";
CREATE TABLE "public"."na_cronjob_state" (
  "id" int4 NOT NULL DEFAULT nextval('na_cronjob_state_id_seq'::regclass),
  "status" int4 NOT NULL DEFAULT NULL,
  "action" int4 NOT NULL DEFAULT NULL,
  "created_at" timestamptz(6) DEFAULT NULL,
  "cronjob_id" int4 DEFAULT NULL,
  "process_id" int4 DEFAULT NULL
)
;

-- ----------------------------
-- Records of na_cronjob_state
-- ----------------------------
INSERT INTO "public"."na_cronjob_state" VALUES (70, 1, 1, '2019-04-29 19:24:45.2246+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (71, 1, 1, '2019-04-29 19:25:15.8436+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (72, 1, 1, '2019-04-29 19:25:55.4866+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (73, 1, 1, '2019-04-29 19:28:55.8716+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (74, 1, 1, '2019-04-29 19:29:58.0686+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (75, 1, 1, '2019-04-29 19:30:45.4416+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (76, 1, 1, '2019-04-29 19:30:50.9116+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (77, 1, 1, '2019-04-29 19:30:57.9606+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (78, 1, 1, '2019-04-29 19:31:29.5466+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (79, 1, 1, '2019-04-29 19:32:22.4236+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (80, 1, 1, '2019-04-29 19:32:30.5846+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (81, 1, 1, '2019-04-29 19:32:54.6356+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (82, 1, 1, '2019-04-29 19:33:01.0586+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (83, 1, 1, '2019-04-29 19:36:42.0016+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (84, 1, 1, '2019-04-29 19:36:49.3986+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (85, 1, 1, '2019-04-29 19:47:49.9346+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (86, 1, 1, '2019-04-29 19:48:42.9496+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (87, 1, 1, '2019-04-29 19:49:08.8186+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (88, 1, 1, '2019-04-29 19:49:15.5816+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (89, 1, 1, '2019-04-29 19:50:34.9106+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (90, 1, 1, '2019-04-29 19:50:47.8846+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (91, 1, 1, '2019-04-29 19:52:33.1606+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (92, 1, 1, '2019-04-29 19:52:40.7356+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (93, 1, 1, '2019-04-29 19:58:55.9406+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (94, 1, 1, '2019-04-29 19:59:43.0276+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (95, 1, 1, '2019-04-29 20:00:25.0036+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (96, 1, 1, '2019-04-29 20:02:12.8096+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (97, 1, 1, '2019-04-29 20:03:34.6896+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (98, 1, 1, '2019-04-29 20:05:48.5686+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (99, 1, 1, '2019-04-29 20:07:07.5446+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (100, 1, 1, '2019-04-29 20:07:51.8986+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (101, 1, 1, '2019-04-29 20:07:58.2276+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (102, 1, 1, '2019-04-29 20:08:56.2656+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (103, 1, 1, '2019-04-29 20:09:49.4596+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (104, 1, 1, '2019-04-29 20:10:43.3546+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (105, 1, 1, '2019-04-29 20:10:49.8996+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (106, 1, 1, '2019-04-29 20:11:35.3366+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (107, 1, 1, '2019-04-29 20:11:41.1506+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (108, 1, 1, '2019-04-29 20:16:13.2016+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (109, 1, 1, '2019-04-29 20:16:32.8886+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (110, 1, 1, '2019-04-29 20:17:21.7826+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (111, 1, 1, '2019-04-29 20:18:18.9436+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (112, 1, 1, '2019-04-29 20:18:25.0776+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (113, 1, 1, '2019-04-29 20:22:54.8136+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (114, 1, 1, '2019-04-29 20:23:03.1446+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (115, 1, 1, '2019-04-29 20:24:11.8206+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (116, 1, 1, '2019-04-29 20:24:41.5616+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (117, 1, 1, '2019-04-29 20:24:49.7446+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (118, 1, 1, '2019-04-29 20:25:49.3646+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (119, 1, 1, '2019-04-29 20:25:55.7526+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (120, 1, 1, '2019-04-29 20:28:27.5256+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (121, 1, 1, '2019-04-29 20:29:31.8536+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (122, 1, 1, '2019-04-29 20:29:38.6856+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (123, 1, 1, '2019-04-30 08:09:06.2444+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (124, 1, 1, '2019-04-30 08:09:47.7954+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (125, 1, 1, '2019-04-30 08:10:46.3184+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (57, 1, 1, '2019-04-26 17:36:48.224+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (58, 1, 1, '2019-04-26 17:38:17.164+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (59, 1, 1, '2019-04-26 17:39:22.309+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (60, 1, 2, '2019-04-26 17:39:57.624+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (61, 1, 2, '2019-04-26 17:40:00.336+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (62, 1, 2, '2019-04-26 17:40:01.831+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (63, 1, 2, '2019-04-26 17:40:01.969+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (64, 1, 2, '2019-04-26 17:40:02.113+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (65, 1, 1, '2019-04-26 17:40:12.033+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (66, 1, 1, '2019-04-26 17:40:59.835+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (67, 1, 1, '2019-04-26 17:41:20.946+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (68, 1, 1, '2019-04-26 17:43:46.623+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (69, 1, 1, '2019-04-26 18:04:26.665+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (126, 1, 1, '2019-04-30 08:11:04.1154+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (127, 1, 1, '2019-04-30 08:12:07.8134+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (128, 1, 1, '2019-04-30 08:12:24.4894+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (129, 1, 1, '2019-04-30 08:13:31.3374+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (130, 1, 1, '2019-04-30 08:13:39.2144+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (131, 1, 1, '2019-04-30 08:14:50.3684+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (132, 1, 2, '2019-04-30 08:15:28.2804+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (133, 1, 1, '2019-04-30 08:17:17.2194+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (134, 1, 1, '2019-04-30 08:17:29.6174+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (135, 1, 1, '2019-04-30 08:19:14.8234+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (136, 1, 1, '2019-04-30 08:19:17.8774+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (137, 1, 1, '2019-04-30 08:19:28.0484+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (138, 1, 1, '2019-04-30 08:19:30.8834+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (139, 1, 1, '2019-04-30 08:20:03.7924+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (140, 1, 1, '2019-04-30 08:20:04.9824+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (141, 1, 1, '2019-04-30 08:20:58.7114+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (142, 1, 1, '2019-04-30 08:21:01.6094+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (143, 1, 1, '2019-04-30 08:21:18.2084+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (144, 1, 1, '2019-04-30 08:21:19.8954+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (145, 1, 1, '2019-04-30 08:21:38.5644+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (146, 1, 1, '2019-04-30 09:24:50.6634+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (147, 1, 1, '2019-04-30 09:31:19.4504+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (148, 1, 1, '2019-04-30 10:48:37.9024+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (149, 1, 1, '2019-04-30 10:48:39.7174+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (150, 1, 1, '2019-04-30 10:53:23.9354+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (151, 1, 1, '2019-04-30 11:17:20.9704+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (152, 1, 1, '2019-04-30 11:17:58.3434+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (153, 1, 1, '2019-04-30 11:18:29.2724+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (154, 1, 1, '2019-04-30 11:52:18.6484+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (155, 1, 1, '2019-04-30 11:52:34.0454+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (156, 1, 1, '2019-04-30 11:53:55.9994+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (157, 1, 1, '2019-04-30 12:18:51.4054+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (158, 1, 1, '2019-04-30 12:20:57.3594+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (159, 1, 1, '2019-04-30 12:21:31.7354+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (160, 1, 1, '2019-04-30 12:22:39.2384+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (161, 1, 1, '2019-04-30 12:25:24.7384+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (162, 1, 1, '2019-04-30 12:25:34.0284+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (163, 1, 1, '2019-04-30 12:25:57.2254+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (164, 1, 1, '2019-04-30 12:26:57.4364+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (165, 1, 1, '2019-04-30 12:27:26.2554+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (166, 1, 1, '2019-04-30 12:32:59.9704+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (167, 1, 1, '2019-04-30 12:33:15.8724+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (168, 1, 1, '2019-04-30 12:35:19.1954+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (169, 1, 1, '2019-04-30 12:37:56.2964+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (170, 1, 1, '2019-04-30 12:43:32.6144+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (171, 1, 1, '2019-04-30 12:44:42.4824+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (172, 1, 1, '2019-04-30 12:44:48.3484+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (173, 1, 1, '2019-04-30 12:45:32.8424+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (174, 1, 1, '2019-04-30 12:45:41.5674+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (175, 1, 1, '2019-04-30 12:45:56.2694+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (176, 1, 1, '2019-04-30 12:46:01.5974+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (177, 1, 1, '2019-04-30 12:46:37.7794+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (178, 1, 1, '2019-04-30 12:47:30.7644+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (179, 1, 1, '2019-04-30 12:49:19.5004+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (180, 1, 1, '2019-04-30 12:50:07.4394+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (181, 1, 1, '2019-04-30 12:50:13.1454+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (182, 1, 1, '2019-04-30 12:51:06.3984+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (183, 1, 1, '2019-04-30 12:52:09.2034+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (184, 1, 1, '2019-04-30 12:54:29.3584+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (185, 1, 1, '2019-04-30 12:55:15.7364+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (186, 1, 1, '2019-04-30 12:55:34.4614+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (187, 1, 1, '2019-04-30 12:55:52.9934+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (188, 1, 1, '2019-04-30 12:55:54.6794+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (189, 1, 1, '2019-04-30 12:56:17.1304+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (190, 1, 1, '2019-04-30 12:56:17.4784+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (191, 1, 1, '2019-04-30 12:58:44.6214+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (192, 1, 1, '2019-04-30 12:58:46.1874+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (193, 1, 1, '2019-04-30 12:58:56.6034+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (194, 1, 1, '2019-04-30 12:58:59.2704+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (195, 1, 1, '2019-04-30 12:59:17.9904+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (196, 1, 1, '2019-04-30 12:59:39.2554+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (197, 1, 1, '2019-04-30 13:00:53.7074+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (198, 1, 1, '2019-04-30 13:00:56.4234+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (199, 1, 1, '2019-04-30 13:02:09.4424+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (200, 1, 1, '2019-04-30 13:05:38.0294+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (201, 1, 1, '2019-04-30 13:06:43.7194+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (202, 1, 1, '2019-04-30 13:10:22.7564+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (203, 1, 1, '2019-04-30 13:10:29.3574+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (204, 1, 1, '2019-04-30 13:11:01.4094+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (205, 1, 1, '2019-04-30 13:11:27.7404+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (206, 1, 1, '2019-04-30 13:36:43.1464+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (207, 1, 1, '2019-04-30 13:37:08.3294+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (208, 1, 1, '2019-04-30 13:44:41.5914+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (209, 1, 1, '2019-04-30 13:47:07.3914+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (210, 1, 1, '2019-04-30 13:47:37.2524+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (211, 1, 1, '2019-04-30 13:47:57.7704+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (212, 1, 1, '2019-04-30 13:48:49.6504+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (213, 1, 1, '2019-04-30 13:49:19.9234+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (214, 1, 1, '2019-04-30 13:52:03.5714+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (215, 1, 1, '2019-04-30 13:54:17.2594+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (216, 1, 1, '2019-04-30 13:54:42.2214+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (217, 1, 1, '2019-04-30 13:58:57.4194+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (218, 1, 1, '2019-04-30 14:01:10.1954+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (219, 1, 1, '2019-04-30 14:05:00.1264+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (220, 1, 1, '2019-04-30 14:08:16.0944+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (221, 1, 1, '2019-04-30 14:08:39.4954+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (222, 1, 1, '2019-04-30 14:09:45.2664+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (223, 1, 1, '2019-04-30 14:10:02.7614+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (224, 1, 1, '2019-04-30 14:10:53.5244+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (225, 1, 1, '2019-04-30 14:11:21.6594+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (226, 1, 1, '2019-04-30 14:11:51.6804+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (227, 1, 1, '2019-04-30 14:13:58.7474+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (228, 1, 1, '2019-04-30 14:17:49.3074+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (229, 1, 1, '2019-04-30 14:22:42.9604+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (230, 1, 1, '2019-04-30 14:23:21.9054+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (231, 1, 1, '2019-04-30 14:23:35.4404+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (232, 1, 1, '2019-04-30 14:24:20.6384+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (233, 1, 1, '2019-04-30 14:24:56.3604+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (234, 1, 1, '2019-04-30 14:25:07.5414+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (235, 1, 1, '2019-04-30 14:26:18.0674+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (236, 1, 1, '2019-04-30 14:26:26.1954+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (237, 1, 1, '2019-04-30 14:26:59.7554+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (238, 1, 1, '2019-04-30 14:27:33.4114+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (239, 1, 1, '2019-04-30 14:28:17.8204+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (240, 1, 1, '2019-04-30 14:28:33.8584+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (241, 1, 1, '2019-04-30 14:28:36.9164+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (242, 1, 1, '2019-04-30 14:28:50.1324+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (243, 1, 1, '2019-04-30 14:29:33.8584+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (244, 1, 1, '2019-04-30 14:29:50.0254+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (245, 1, 1, '2019-04-30 14:30:21.9724+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (246, 1, 1, '2019-04-30 14:30:35.9934+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (247, 1, 1, '2019-04-30 14:31:28.9904+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (248, 1, 1, '2019-04-30 14:32:26.1164+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (249, 1, 1, '2019-04-30 14:32:27.1694+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (250, 1, 1, '2019-04-30 14:32:56.1434+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (251, 1, 1, '2019-04-30 14:33:58.3044+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (252, 1, 1, '2019-04-30 14:33:58.5014+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (253, 1, 1, '2019-04-30 14:34:05.6734+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (254, 1, 1, '2019-04-30 14:38:35.9734+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (255, 1, 1, '2019-04-30 14:40:45.2084+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (256, 1, 1, '2019-04-30 14:40:52.2514+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (257, 1, 1, '2019-04-30 14:41:33.4564+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (258, 1, 1, '2019-04-30 14:42:15.6514+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (259, 1, 1, '2019-04-30 14:42:21.4924+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (260, 1, 1, '2019-04-30 14:42:41.6074+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (261, 1, 1, '2019-04-30 14:45:31.7014+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (262, 1, 1, '2019-04-30 14:45:52.3484+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (263, 1, 1, '2019-04-30 14:46:22.2534+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (264, 1, 1, '2019-04-30 14:46:52.6994+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (265, 1, 1, '2019-04-30 14:47:29.8354+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (266, 1, 1, '2019-04-30 14:47:32.0384+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (267, 1, 1, '2019-04-30 14:49:42.6884+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (268, 1, 1, '2019-04-30 14:49:46.3114+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (269, 1, 1, '2019-04-30 14:50:08.9384+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (270, 1, 1, '2019-04-30 14:50:09.3034+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (271, 1, 1, '2019-04-30 14:50:27.3494+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (272, 1, 1, '2019-04-30 14:50:28.8594+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (273, 1, 1, '2019-04-30 14:50:49.2344+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (274, 1, 1, '2019-04-30 14:50:49.4204+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (275, 1, 1, '2019-04-30 14:51:20.0894+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (276, 1, 1, '2019-04-30 14:51:23.8154+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (277, 1, 1, '2019-04-30 14:53:30.5524+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (278, 1, 1, '2019-04-30 14:53:32.7664+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (279, 1, 1, '2019-04-30 14:54:02.8954+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (280, 1, 1, '2019-04-30 14:54:32.0674+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (281, 1, 1, '2019-04-30 14:54:33.8144+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (282, 1, 1, '2019-04-30 14:55:18.1714+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (283, 1, 1, '2019-04-30 14:55:33.8994+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (284, 1, 1, '2019-04-30 14:55:43.2644+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (285, 1, 1, '2019-04-30 14:55:46.0054+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (286, 1, 1, '2019-04-30 14:58:12.2204+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (287, 1, 1, '2019-04-30 14:58:15.5094+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (288, 1, 1, '2019-04-30 15:00:15.1954+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (289, 1, 1, '2019-04-30 15:00:17.0124+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (290, 1, 1, '2019-04-30 15:00:44.7284+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (291, 1, 1, '2019-04-30 15:00:45.9774+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (292, 1, 1, '2019-04-30 15:01:13.2764+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (293, 1, 1, '2019-04-30 15:01:14.5564+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (294, 1, 1, '2019-04-30 15:02:49.1554+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (295, 1, 1, '2019-04-30 15:04:07.2364+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (296, 1, 1, '2019-04-30 15:04:08.7504+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (297, 1, 1, '2019-04-30 15:05:06.6344+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (298, 1, 1, '2019-04-30 15:05:08.2764+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (299, 1, 1, '2019-04-30 15:06:37.7614+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (300, 1, 1, '2019-04-30 15:06:38.8734+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (301, 1, 1, '2019-04-30 15:07:13.2384+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (302, 1, 1, '2019-04-30 15:07:27.5544+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (303, 1, 1, '2019-04-30 15:07:29.9254+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (304, 1, 1, '2019-04-30 15:08:46.6014+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (305, 1, 1, '2019-04-30 15:08:47.4374+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (306, 1, 1, '2019-04-30 15:09:36.8544+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (307, 1, 1, '2019-04-30 15:09:38.5454+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (308, 1, 1, '2019-04-30 15:11:00.0714+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (309, 1, 1, '2019-04-30 15:11:00.5264+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (310, 1, 1, '2019-04-30 15:11:32.7804+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (311, 1, 1, '2019-04-30 15:11:36.2344+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (312, 1, 1, '2019-04-30 15:11:44.8134+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (313, 1, 1, '2019-04-30 15:11:46.0074+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (314, 1, 1, '2019-04-30 15:12:39.7044+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (315, 1, 1, '2019-04-30 15:12:39.8624+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (316, 1, 1, '2019-04-30 15:13:03.4004+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (317, 1, 1, '2019-04-30 15:13:03.4014+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (318, 1, 1, '2019-04-30 15:13:13.9884+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (319, 1, 1, '2019-04-30 15:13:14.5164+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (320, 1, 1, '2019-04-30 15:13:37.7614+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (321, 1, 1, '2019-04-30 15:13:39.8954+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (322, 1, 1, '2019-04-30 15:13:51.1224+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (323, 1, 1, '2019-04-30 15:16:58.4034+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (324, 1, 1, '2019-04-30 15:17:54.2244+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (325, 1, 1, '2019-04-30 15:20:04.0924+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (326, 1, 1, '2019-04-30 15:20:05.3544+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (327, 1, 1, '2019-04-30 15:20:46.8344+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (328, 1, 1, '2019-04-30 15:20:48.2844+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (329, 1, 1, '2019-04-30 15:21:04.0594+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (330, 1, 1, '2019-04-30 15:21:04.5264+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (331, 1, 1, '2019-04-30 15:21:34.4834+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (332, 1, 1, '2019-04-30 15:21:34.8204+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (333, 1, 1, '2019-04-30 15:21:47.1134+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (334, 1, 1, '2019-04-30 15:21:49.0854+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (335, 1, 1, '2019-04-30 15:25:07.4724+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (336, 1, 1, '2019-04-30 15:25:29.1554+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (337, 1, 1, '2019-04-30 15:27:01.8264+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (338, 1, 1, '2019-04-30 15:27:02.9934+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (339, 1, 1, '2019-04-30 15:27:19.9394+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (340, 1, 1, '2019-04-30 15:27:32.8384+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (341, 1, 1, '2019-04-30 15:27:35.1554+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (342, 1, 1, '2019-04-30 15:28:07.6454+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (343, 1, 1, '2019-04-30 15:28:08.5694+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (344, 1, 1, '2019-04-30 15:28:19.4554+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (345, 1, 1, '2019-04-30 15:28:22.4434+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (346, 1, 1, '2019-04-30 15:28:35.1234+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (347, 1, 1, '2019-04-30 15:28:35.8264+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (348, 1, 1, '2019-04-30 15:29:06.8334+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (349, 1, 1, '2019-04-30 15:29:09.0884+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (350, 1, 1, '2019-04-30 15:31:04.0184+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (351, 1, 1, '2019-04-30 15:31:06.4204+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (352, 1, 1, '2019-04-30 15:33:16.1944+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (353, 1, 1, '2019-04-30 15:33:17.0504+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (354, 1, 1, '2019-04-30 15:33:46.4604+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (355, 1, 1, '2019-04-30 15:33:48.1574+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (356, 1, 1, '2019-04-30 15:35:00.5304+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (357, 1, 1, '2019-04-30 15:35:18.0204+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (358, 1, 1, '2019-05-01 10:22:18.833+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (359, 1, 1, '2019-05-01 10:44:28.888+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (360, 1, 1, '2019-05-01 17:01:46.8635+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (361, 1, 1, '2019-05-02 08:09:34.6116+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (362, 1, 1, '2019-05-02 15:35:17.8826+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (363, 1, 1, '2019-05-03 09:26:03.3048+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (364, 1, 1, '2019-05-03 13:11:57.8768+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (365, 1, 1, '2019-05-03 13:34:11.8458+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (366, 1, 1, '2019-05-03 13:40:54.4948+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (367, 1, 1, '2019-05-03 13:41:09.3568+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (368, 1, 1, '2019-05-03 13:45:14.8138+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (369, 1, 1, '2019-05-03 13:45:54.9258+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (370, 1, 1, '2019-05-03 13:46:05.7488+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (371, 1, 1, '2019-05-03 13:49:11.1778+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (372, 1, 1, '2019-05-03 13:50:57.1808+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (373, 1, 1, '2019-05-03 13:51:33.2218+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (374, 1, 1, '2019-05-03 13:52:48.8858+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (375, 1, 1, '2019-05-03 13:52:53.6448+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (376, 1, 1, '2019-05-03 13:53:02.5668+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (377, 1, 1, '2019-05-03 13:53:29.1478+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (378, 1, 1, '2019-05-03 13:53:40.3488+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (379, 1, 1, '2019-05-03 13:53:57.9058+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (380, 1, 1, '2019-05-03 13:54:05.0788+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (381, 1, 1, '2019-05-03 13:55:15.8598+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (382, 1, 1, '2019-05-03 13:55:49.1958+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (383, 1, 1, '2019-05-03 13:55:58.8138+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (384, 1, 1, '2019-05-03 13:56:03.2558+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (385, 1, 1, '2019-05-03 13:58:22.1758+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (386, 1, 1, '2019-05-03 14:20:28.7728+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (387, 1, 1, '2019-05-03 14:20:38.2998+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (388, 1, 1, '2019-05-03 14:20:43.0538+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (389, 1, 1, '2019-05-03 14:20:52.2578+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (390, 1, 1, '2019-05-03 14:20:56.7898+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (391, 1, 1, '2019-05-03 14:21:20.0528+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (392, 1, 1, '2019-05-03 14:21:29.7778+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (393, 1, 1, '2019-05-03 14:21:50.3968+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (394, 1, 1, '2019-05-03 14:22:10.8748+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (395, 1, 1, '2019-05-03 14:23:54.3668+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (396, 1, 1, '2019-05-03 14:24:14.9788+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (397, 1, 1, '2019-05-03 14:24:26.7008+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (398, 1, 1, '2019-05-03 14:25:03.3628+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (399, 1, 1, '2019-05-03 14:25:35.5888+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (400, 1, 1, '2019-05-03 14:26:23.6848+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (401, 1, 1, '2019-05-03 14:30:38.4268+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (402, 1, 1, '2019-05-03 14:36:32.5278+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (403, 1, 1, '2019-05-03 14:36:36.9258+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (404, 1, 1, '2019-05-03 14:37:57.5748+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (405, 1, 1, '2019-05-03 14:38:02.3958+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (406, 1, 1, '2019-05-03 14:38:06.9518+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (407, 1, 1, '2019-05-03 14:39:02.1298+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (408, 1, 1, '2019-05-03 14:39:10.5728+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (409, 1, 1, '2019-05-03 14:41:48.0938+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (410, 1, 1, '2019-05-03 14:52:09.8508+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (411, 1, 1, '2019-05-03 15:07:51.4558+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (412, 1, 1, '2019-05-03 16:03:52.3988+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (413, 1, 1, '2019-05-03 16:04:40.8778+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (414, 1, 1, '2019-05-03 18:23:50.2008+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (415, 1, 1, '2019-05-06 10:52:26.838+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (416, 1, 1, '2019-05-06 10:55:55.06+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (417, 1, 1, '2019-05-06 10:56:52.372+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (418, 1, 1, '2019-05-06 10:57:00.536+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (419, 1, 1, '2019-05-06 10:57:51.333+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (420, 1, 1, '2019-05-06 10:58:38.355+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (421, 1, 1, '2019-05-06 11:00:07.61+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (422, 1, 1, '2019-05-06 11:00:48.709+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (423, 1, 1, '2019-05-06 11:03:43.535+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (424, 1, 1, '2019-05-06 11:44:08.075+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (425, 1, 1, '2019-05-06 11:44:42.683+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (426, 1, 1, '2019-05-06 11:47:55.171+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (427, 1, 1, '2019-05-06 11:49:03.802+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (428, 1, 1, '2019-05-06 11:49:52.016+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (429, 1, 1, '2019-05-06 11:50:53.508+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (430, 1, 1, '2019-05-06 11:54:29.587+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (431, 1, 1, '2019-05-06 11:54:42.126+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (432, 1, 1, '2019-05-06 11:55:09.334+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (433, 1, 1, '2019-05-07 12:27:12.7004+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (434, 1, 1, '2019-05-07 12:27:44.7014+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (435, 1, 1, '2019-05-07 12:28:11.7684+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (436, 1, 1, '2019-05-07 12:28:34.5244+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (437, 1, 1, '2019-05-07 12:29:39.3694+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (438, 1, 1, '2019-05-07 12:30:24.1954+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (439, 1, 1, '2019-05-07 12:30:37.0364+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (440, 1, 1, '2019-05-07 12:31:15.7224+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (441, 1, 1, '2019-05-07 12:31:39.2244+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (442, 1, 1, '2019-05-07 12:31:44.2744+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (443, 1, 1, '2019-05-07 12:31:48.5934+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (444, 1, 1, '2019-05-07 12:46:27.3714+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (445, 1, 1, '2019-05-07 12:46:32.4514+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (446, 1, 1, '2019-05-07 12:49:16.9254+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (447, 1, 1, '2019-05-07 12:51:29.8004+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (448, 1, 1, '2019-05-07 12:52:28.8744+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (449, 1, 1, '2019-05-07 12:54:19.4504+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (450, 1, 1, '2019-05-07 12:54:54.4164+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (451, 1, 1, '2019-05-07 12:56:02.6244+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (452, 1, 1, '2019-05-07 12:56:31.3864+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (453, 1, 1, '2019-05-07 12:57:38.6874+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (454, 1, 1, '2019-05-07 12:58:04.4414+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (455, 1, 1, '2019-05-07 12:58:33.3744+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (456, 1, 1, '2019-05-07 18:37:09.8324+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (457, 1, 1, '2019-05-07 18:38:43.8044+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (458, 1, 1, '2019-05-07 18:40:06.5574+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (459, 1, 1, '2019-05-07 18:45:12.1734+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (460, 1, 1, '2019-05-07 18:45:30.2964+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (461, 1, 1, '2019-05-07 18:45:35.4164+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (462, 1, 1, '2019-05-07 18:46:07.2144+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (463, 1, 1, '2019-05-07 18:46:25.2484+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (464, 1, 1, '2019-05-07 18:51:34.9374+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (465, 1, 1, '2019-05-07 18:52:13.7764+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (466, 1, 1, '2019-05-07 18:52:26.8874+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (467, 1, 1, '2019-05-07 18:52:52.0714+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (468, 1, 1, '2019-05-07 18:53:05.8864+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (469, 1, 1, '2019-05-07 18:53:18.8494+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (470, 1, 1, '2019-05-07 18:53:44.3574+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (471, 1, 1, '2019-05-08 08:24:54.9548+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (472, 1, 1, '2019-05-08 08:25:42.9138+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (473, 1, 1, '2019-05-08 08:26:00.9498+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (474, 1, 1, '2019-05-08 08:41:54.0288+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (475, 1, 1, '2019-05-08 08:44:25.5378+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (476, 1, 1, '2019-05-08 08:46:57.5888+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (477, 1, 1, '2019-05-08 08:54:01.4698+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (478, 1, 1, '2019-05-08 08:56:48.9098+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (479, 1, 1, '2019-05-08 08:59:58.8008+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (480, 1, 1, '2019-05-08 09:00:33.0198+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (481, 1, 1, '2019-05-08 09:04:02.9258+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (482, 1, 1, '2019-05-08 09:08:30.2438+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (483, 1, 1, '2019-05-08 09:18:53.7448+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (484, 1, 1, '2019-05-08 09:19:44.9908+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (485, 1, 1, '2019-05-08 09:21:03.3788+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (486, 1, 1, '2019-05-08 09:21:49.9318+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (487, 1, 1, '2019-05-08 09:22:50.1888+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (488, 1, 1, '2019-05-08 09:23:23.0998+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (489, 1, 1, '2019-05-08 09:23:36.1808+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (490, 1, 1, '2019-05-08 09:23:57.1048+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (491, 1, 1, '2019-05-08 09:26:09.4858+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (492, 1, 1, '2019-05-08 10:21:13.0978+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (493, 1, 1, '2019-05-08 10:21:23.0938+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (494, 1, 1, '2019-05-08 10:29:25.8448+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (495, 1, 1, '2019-05-08 10:29:31.9618+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (496, 1, 1, '2019-05-08 10:30:01.7178+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (497, 1, 1, '2019-05-08 10:41:17.8538+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (498, 1, 1, '2019-05-08 10:44:00.3088+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (499, 1, 1, '2019-05-08 10:44:08.2618+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (500, 1, 1, '2019-05-08 10:50:05.1538+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (501, 1, 1, '2019-05-09 12:49:47.9334+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (502, 1, 1, '2019-05-09 12:53:46.1404+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (503, 1, 1, '2019-05-09 12:53:53.6604+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (504, 1, 1, '2019-05-09 12:54:28.5534+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (505, 1, 1, '2019-05-09 13:21:59.7804+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (506, 1, 1, '2019-05-09 13:23:17.1634+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (507, 1, 1, '2019-05-09 13:23:41.8254+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (508, 1, 1, '2019-05-09 13:24:21.8784+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (509, 1, 1, '2019-05-09 13:54:37.2534+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (510, 1, 1, '2019-05-09 13:55:15.4204+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (511, 1, 1, '2019-05-09 13:57:03.8104+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (512, 1, 1, '2019-05-09 13:58:56.1634+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (513, 1, 1, '2019-05-09 13:59:56.5584+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (514, 1, 1, '2019-05-09 14:03:34.3364+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (515, 1, 1, '2019-05-09 14:06:52.2474+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (516, 1, 1, '2019-05-09 14:07:15.6864+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (517, 1, 1, '2019-05-09 14:07:56.1164+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (518, 1, 1, '2019-05-09 14:08:12.6984+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (519, 1, 1, '2019-05-09 14:08:44.7494+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (520, 1, 1, '2019-05-09 14:09:04.6174+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (521, 1, 1, '2019-05-09 14:21:40.8454+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (522, 1, 1, '2019-05-09 14:23:43.4294+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (523, 1, 1, '2019-05-09 14:24:53.1714+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (524, 1, 1, '2019-05-09 14:25:29.0744+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (525, 1, 1, '2019-05-09 14:26:05.8094+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (526, 1, 1, '2019-05-09 14:27:08.2324+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (527, 1, 1, '2019-05-09 14:45:30.4284+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (528, 1, 1, '2019-05-09 15:36:15.8084+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (529, 1, 1, '2019-05-09 15:36:47.0954+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (530, 1, 1, '2019-05-09 15:41:03.6864+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (531, 1, 1, '2019-05-09 15:41:31.6464+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (532, 1, 1, '2019-05-09 15:41:46.4794+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (533, 1, 1, '2019-05-09 15:45:39.6014+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (534, 1, 1, '2019-05-09 15:47:00.3324+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (535, 1, 1, '2019-05-09 15:47:06.7614+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (536, 1, 1, '2019-05-09 15:47:56.9204+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (537, 1, 1, '2019-05-09 15:49:15.0124+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (538, 1, 1, '2019-05-09 15:51:25.4324+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (539, 1, 1, '2019-05-09 15:51:34.0794+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (540, 1, 1, '2019-05-09 15:52:15.6364+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (541, 1, 1, '2019-05-09 15:53:38.4384+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (542, 1, 1, '2019-05-09 15:54:40.7464+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (543, 1, 1, '2019-05-09 15:55:05.2424+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (544, 1, 1, '2019-05-09 15:55:19.6874+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (545, 1, 1, '2019-05-09 16:01:59.9174+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (546, 1, 1, '2019-05-09 16:06:40.8864+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (547, 1, 1, '2019-05-09 16:06:47.0624+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (548, 1, 1, '2019-05-09 16:07:29.3644+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (549, 1, 1, '2019-05-09 16:08:11.9274+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (550, 1, 1, '2019-05-09 16:08:29.0864+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (551, 1, 1, '2019-05-09 16:09:16.8204+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (552, 1, 1, '2019-05-09 16:11:37.5064+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (553, 1, 1, '2019-05-09 16:23:34.8844+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (554, 1, 1, '2019-05-09 16:26:29.9934+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (555, 1, 1, '2019-05-09 16:27:03.2684+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (556, 1, 1, '2019-05-09 16:27:11.7664+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (557, 1, 1, '2019-05-09 16:27:38.8514+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (558, 1, 1, '2019-05-09 16:29:17.9774+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (559, 1, 1, '2019-05-09 16:40:40.1644+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (560, 1, 1, '2019-05-09 16:46:13.8654+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (561, 1, 1, '2019-05-09 16:47:51.8194+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (562, 1, 1, '2019-05-09 16:48:44.5394+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (563, 1, 1, '2019-05-09 16:56:06.2204+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (564, 1, 1, '2019-05-09 16:57:30.4804+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (565, 1, 1, '2019-05-09 16:58:11.6724+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (566, 1, 1, '2019-05-09 16:59:12.1824+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (567, 1, 1, '2019-05-09 16:59:32.7204+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (568, 1, 1, '2019-05-09 17:00:20.0844+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (569, 1, 1, '2019-05-09 17:01:27.0214+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (570, 1, 1, '2019-05-09 17:05:58.2424+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (571, 1, 1, '2019-05-09 17:53:44.3834+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (572, 1, 1, '2019-05-09 18:00:10.7714+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (573, 1, 1, '2019-05-09 18:00:21.7484+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (574, 1, 1, '2019-05-09 18:02:39.8014+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (575, 1, 1, '2019-05-09 18:03:03.9444+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (576, 1, 1, '2019-05-09 18:03:29.0384+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (577, 1, 1, '2019-05-09 18:04:15.3304+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (578, 1, 1, '2019-05-09 18:04:45.1734+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (579, 1, 1, '2019-05-09 18:05:29.8174+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (580, 1, 1, '2019-05-09 18:11:35.7964+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (581, 1, 1, '2019-05-09 18:16:46.0644+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (582, 1, 1, '2019-05-09 18:17:31.4664+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (583, 1, 1, '2019-05-09 18:18:08.6174+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (584, 1, 1, '2019-05-09 18:18:51.3494+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (585, 1, 1, '2019-05-09 18:21:17.9884+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (586, 1, 1, '2019-05-09 18:21:49.5414+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (587, 1, 1, '2019-05-09 18:22:47.9374+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (588, 1, 1, '2019-05-09 18:24:37.1134+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (589, 1, 1, '2019-05-09 18:24:50.9874+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (590, 1, 1, '2019-05-09 18:25:05.8374+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (591, 1, 1, '2019-05-09 18:25:37.1894+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (592, 1, 1, '2019-05-09 18:26:25.1104+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (593, 1, 1, '2019-05-09 18:36:18.9824+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (594, 1, 1, '2019-05-09 18:36:41.3464+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (595, 1, 1, '2019-05-09 18:37:39.4714+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (596, 1, 1, '2019-05-09 18:37:57.2614+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (597, 1, 1, '2019-05-09 18:38:46.0724+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (598, 1, 1, '2019-05-09 18:39:47.3234+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (599, 1, 1, '2019-05-09 18:40:26.9074+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (600, 1, 1, '2019-05-09 18:40:48.0524+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (601, 1, 1, '2019-05-09 18:48:17.5884+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (602, 1, 1, '2019-05-09 18:50:33.5214+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (603, 1, 1, '2019-05-09 18:52:19.3854+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (604, 1, 1, '2019-05-09 18:53:09.3664+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (605, 1, 1, '2019-05-09 18:53:29.3154+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (606, 1, 1, '2019-05-09 18:53:46.3024+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (607, 1, 1, '2019-05-09 18:54:12.7184+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (608, 1, 1, '2019-05-09 18:54:46.0124+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (609, 1, 1, '2019-05-09 19:06:45.2854+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (610, 1, 1, '2019-05-09 19:08:27.5284+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (611, 1, 1, '2019-05-09 19:11:21.4654+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (612, 1, 1, '2019-05-09 19:12:36.8964+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (613, 1, 1, '2019-05-09 19:13:19.7504+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (614, 1, 1, '2019-05-09 19:14:30.4434+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (615, 1, 1, '2019-05-09 19:14:44.0114+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (616, 1, 1, '2019-05-09 19:18:58.0304+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (617, 1, 1, '2019-05-09 19:22:41.2914+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (618, 1, 1, '2019-05-09 19:22:51.6334+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (619, 1, 1, '2019-05-09 19:22:59.5984+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (620, 1, 1, '2019-05-09 19:23:32.0624+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (621, 1, 1, '2019-05-09 19:25:12.8474+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (622, 1, 1, '2019-05-09 19:27:02.4374+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (623, 1, 1, '2019-05-09 19:28:43.4104+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (624, 1, 1, '2019-05-09 19:29:02.1124+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (625, 1, 1, '2019-05-09 19:30:53.6064+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (626, 1, 1, '2019-05-09 19:31:06.4864+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (627, 1, 1, '2019-05-09 19:33:19.5834+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (628, 1, 1, '2019-05-09 19:33:39.4714+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (629, 1, 1, '2019-05-10 09:24:41.9316+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (630, 1, 1, '2019-05-10 09:57:24.3076+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (631, 1, 1, '2019-05-10 10:00:55.5086+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (632, 1, 1, '2019-05-10 10:01:00.9526+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (633, 1, 1, '2019-05-10 10:01:09.0136+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (634, 1, 1, '2019-05-10 10:01:24.5416+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (635, 1, 1, '2019-05-13 15:28:16.9578+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (636, 1, 1, '2019-05-13 15:30:17.1488+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (637, 1, 1, '2019-05-13 15:30:43.9638+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (638, 1, 1, '2019-05-13 15:31:09.7038+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (639, 1, 1, '2019-05-13 15:34:06.4108+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (640, 1, 1, '2019-05-13 15:34:23.4928+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (641, 1, 1, '2019-05-13 15:35:07.3768+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (642, 1, 1, '2019-05-13 15:35:42.5458+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (643, 1, 1, '2019-05-13 15:35:58.3748+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (644, 1, 1, '2019-05-13 15:36:19.5568+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (645, 1, 1, '2019-05-13 15:37:08.1708+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (646, 1, 1, '2019-05-13 15:37:27.7598+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (647, 1, 1, '2019-05-13 16:00:55.9648+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (648, 1, 1, '2019-05-13 16:01:39.2858+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (649, 1, 1, '2019-05-13 16:01:45.1948+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (650, 1, 1, '2019-05-13 16:01:53.5678+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (651, 1, 1, '2019-05-13 16:02:54.2858+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (652, 1, 1, '2019-05-13 16:03:37.8678+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (653, 1, 1, '2019-05-13 16:09:58.2078+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (654, 1, 1, '2019-05-13 16:10:03.9778+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (655, 1, 1, '2019-05-13 16:11:42.4428+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (656, 1, 1, '2019-05-13 16:11:51.5868+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (657, 1, 1, '2019-05-13 16:12:03.5948+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (658, 1, 1, '2019-05-13 16:15:38.0478+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (659, 1, 1, '2019-05-13 16:15:40.9318+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (660, 1, 1, '2019-05-13 16:16:03.1638+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (661, 1, 1, '2019-05-13 16:16:24.7928+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (662, 1, 1, '2019-05-13 16:18:23.8788+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (663, 1, 1, '2019-05-13 16:18:43.0628+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (664, 1, 1, '2019-05-13 16:19:32.1158+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (665, 1, 1, '2019-05-13 16:19:45.8508+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (666, 1, 1, '2019-05-13 16:19:57.1508+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (667, 1, 1, '2019-05-13 16:20:17.5418+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (668, 1, 1, '2019-05-13 16:21:51.1368+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (669, 1, 1, '2019-05-13 16:22:10.3548+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (670, 1, 1, '2019-05-13 16:25:12.0458+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (671, 1, 1, '2019-05-13 16:45:41.2268+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (672, 1, 1, '2019-05-13 20:42:00.0678+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (673, 1, 1, '2019-05-13 20:51:10.2958+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (674, 1, 1, '2019-05-13 20:51:36.7268+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (675, 1, 1, '2019-05-13 20:52:54.8398+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (676, 1, 1, '2019-05-13 20:53:26.1458+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (677, 1, 1, '2019-05-13 20:53:50.2508+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (678, 1, 1, '2019-05-13 20:54:29.6088+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (679, 1, 1, '2019-05-13 20:56:44.9168+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (680, 1, 1, '2019-05-13 20:57:07.2198+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (681, 1, 1, '2019-05-13 20:57:43.3558+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (682, 1, 1, '2019-05-13 20:58:42.7988+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (683, 1, 1, '2019-05-13 21:01:20.0768+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (684, 1, 1, '2019-05-13 21:01:26.7398+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (685, 1, 1, '2019-05-13 21:01:47.5118+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (686, 1, 1, '2019-05-13 21:02:22.5068+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (687, 1, 1, '2019-05-13 21:02:41.8418+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (688, 1, 1, '2019-05-13 21:04:46.9228+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (689, 1, 1, '2019-05-13 21:05:49.9518+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (690, 1, 1, '2019-05-13 21:09:05.6348+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (691, 1, 1, '2019-05-13 21:19:02.5968+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (692, 1, 1, '2019-05-13 21:31:53.2708+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (693, 1, 1, '2019-05-13 21:32:04.9448+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (694, 1, 1, '2019-05-13 21:32:26.2358+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (695, 1, 1, '2019-05-13 21:32:34.0788+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (696, 1, 1, '2019-05-13 21:32:41.9258+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (697, 1, 1, '2019-05-13 21:32:58.2638+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (698, 1, 1, '2019-05-13 21:34:12.7548+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (699, 1, 1, '2019-05-13 21:34:36.6018+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (700, 1, 1, '2019-05-13 21:35:15.3908+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (701, 1, 1, '2019-05-14 17:55:49.4322+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (702, 1, 1, '2019-05-14 17:56:22.2022+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (703, 1, 1, '2019-05-14 19:10:38.5482+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (704, 1, 1, '2019-05-14 19:20:43.0282+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (705, 1, 1, '2019-05-14 19:21:11.6752+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (706, 1, 1, '2019-05-14 19:21:37.1022+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (707, 1, 1, '2019-05-15 10:32:33.5364+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (708, 1, 1, '2019-05-15 11:30:25.9234+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (709, 1, 1, '2019-05-15 11:30:46.3994+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (710, 1, 1, '2019-05-15 12:11:02.9994+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (711, 1, 1, '2019-05-15 12:11:18.8054+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (712, 1, 1, '2019-05-15 12:37:45.6244+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (713, 1, 1, '2019-05-15 12:38:03.8754+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (714, 1, 1, '2019-05-15 12:39:31.1844+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (715, 1, 1, '2019-05-15 12:39:32.4254+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (716, 1, 1, '2019-05-15 12:39:49.7084+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (717, 1, 1, '2019-05-15 12:44:20.4484+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (718, 1, 1, '2019-05-15 12:47:56.8414+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (719, 1, 1, '2019-05-15 13:03:43.1734+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (720, 1, 1, '2019-05-15 13:06:18.3074+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (721, 1, 1, '2019-05-15 13:07:10.6014+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (722, 1, 1, '2019-05-15 13:18:27.0644+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (723, 1, 1, '2019-05-15 13:19:32.8124+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (724, 1, 1, '2019-05-15 13:20:55.0414+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (725, 1, 1, '2019-05-15 13:22:19.0994+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (726, 1, 1, '2019-05-15 13:25:05.6104+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (727, 1, 1, '2019-05-15 13:25:54.1904+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (728, 1, 1, '2019-05-15 13:28:15.0784+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (729, 1, 1, '2019-05-15 13:29:11.9754+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (761, 1, 1, '2019-05-15 13:44:24.9012+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (762, 1, 1, '2019-05-15 13:46:16.6772+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (763, 1, 1, '2019-05-15 13:46:55.2892+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (764, 1, 1, '2019-05-15 13:48:15.0702+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (765, 1, 1, '2019-05-15 13:49:01.4502+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (766, 1, 1, '2019-05-15 13:50:54.4142+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (767, 1, 1, '2019-05-15 13:51:31.6682+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (768, 1, 1, '2019-05-15 13:55:14.6022+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (769, 1, 1, '2019-05-15 16:36:22.9142+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (770, 1, 1, '2019-05-15 16:40:17.4002+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (771, 1, 1, '2019-05-15 16:43:04.8742+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (772, 1, 1, '2019-05-15 16:46:08.4062+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (773, 1, 1, '2019-05-15 16:47:28.8152+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (774, 1, 1, '2019-05-15 16:48:18.1012+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (775, 1, 1, '2019-05-15 16:52:33.6942+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (776, 1, 1, '2019-05-15 16:53:09.2852+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (777, 1, 1, '2019-05-15 16:54:21.4962+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (778, 1, 1, '2019-05-15 16:54:41.7622+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (779, 1, 1, '2019-05-15 16:56:26.4682+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (780, 1, 1, '2019-05-15 16:56:36.9712+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (781, 1, 1, '2019-05-15 16:57:30.9242+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (782, 1, 1, '2019-05-15 17:00:22.4512+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (783, 1, 1, '2019-05-15 17:01:23.0852+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (784, 1, 1, '2019-05-15 17:02:18.4642+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (785, 1, 1, '2019-05-15 17:05:00.1092+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (786, 1, 1, '2019-05-15 17:07:28.7622+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (787, 1, 1, '2019-05-15 17:07:58.3282+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (788, 1, 1, '2019-05-15 17:09:51.3712+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (789, 1, 1, '2019-05-15 17:17:15.7282+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (790, 1, 1, '2019-05-15 17:18:14.3042+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (791, 1, 1, '2019-05-15 17:21:45.2082+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (792, 1, 1, '2019-05-15 17:23:03.6712+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (793, 1, 1, '2019-05-15 18:28:57.2652+08', 6, NULL);
INSERT INTO "public"."na_cronjob_state" VALUES (794, 1, 1, '2019-05-15 18:32:01.4522+08', 6, NULL);

-- ----------------------------
-- Table structure for pub_data_dictionary
-- ----------------------------
DROP TABLE IF EXISTS "public"."pub_data_dictionary";
CREATE TABLE "public"."pub_data_dictionary" (
  "id" int4 NOT NULL DEFAULT nextval('pub_data_dictionary_id_seq'::regclass),
  "created_at" timestamptz(6) DEFAULT NULL,
  "updated_at" timestamptz(6) DEFAULT NULL,
  "is_enable" int4 DEFAULT NULL,
  "is_delete" int4 DEFAULT NULL,
  "title" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "code_main" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "code_sub" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "describe" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "platform" int4 DEFAULT NULL,
  "sort" int4 DEFAULT NULL,
  "type" int4 DEFAULT NULL,
  "status" int4 DEFAULT NULL,
  "is_custom" int4 DEFAULT NULL,
  "category_id" int4 DEFAULT NULL,
  "creator_id" int4 DEFAULT NULL,
  "updater_id" int4 DEFAULT NULL
)
;

-- ----------------------------
-- Table structure for pub_data_dictionary_category
-- ----------------------------
DROP TABLE IF EXISTS "public"."pub_data_dictionary_category";
CREATE TABLE "public"."pub_data_dictionary_category" (
  "id" int4 NOT NULL DEFAULT nextval('pub_data_dictionary_category_id_seq'::regclass),
  "created_at" timestamptz(6) DEFAULT NULL,
  "updated_at" timestamptz(6) DEFAULT NULL,
  "is_enable" int4 DEFAULT NULL,
  "is_delete" int4 DEFAULT NULL,
  "title" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "describe" text COLLATE "pg_catalog"."default" DEFAULT NULL,
  "platform" int4 DEFAULT NULL,
  "sort" int4 DEFAULT NULL,
  "status" int4 DEFAULT NULL,
  "creator_id" int4 DEFAULT NULL,
  "parent_id" int4 DEFAULT NULL,
  "updater_id" int4 DEFAULT NULL
)
;

-- ----------------------------
-- Table structure for pub_data_dictionary_value
-- ----------------------------
DROP TABLE IF EXISTS "public"."pub_data_dictionary_value";
CREATE TABLE "public"."pub_data_dictionary_value" (
  "id" int4 NOT NULL DEFAULT nextval('pub_data_dictionary_value_id_seq'::regclass),
  "created_at" timestamptz(6) DEFAULT NULL,
  "updated_at" timestamptz(6) DEFAULT NULL,
  "is_enable" int4 DEFAULT NULL,
  "is_delete" int4 DEFAULT NULL,
  "title" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "value" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "sort" int4 DEFAULT NULL,
  "type" int4 DEFAULT NULL,
  "status" int4 DEFAULT NULL,
  "is_default" int4 DEFAULT NULL,
  "is_custom" int4 DEFAULT NULL,
  "creator_id" int4 DEFAULT NULL,
  "dict_id" int4 DEFAULT NULL,
  "updater_id" int4 DEFAULT NULL
)
;

-- ----------------------------
-- Indexes structure for table auth_group_profile
-- ----------------------------
CREATE INDEX "auth_group_profile_creator_id_24cfa5fc" ON "public"."auth_group_profile" USING btree (
  "creator_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "auth_group_profile_parent_id_174f448a" ON "public"."auth_group_profile" USING btree (
  "parent_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "auth_group_profile_updater_id_b354ab52" ON "public"."auth_group_profile" USING btree (
  "updater_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_group_profile
-- ----------------------------
ALTER TABLE "public"."auth_group_profile" ADD CONSTRAINT "auth_group_profile_group_id_key" UNIQUE ("group_id");

-- ----------------------------
-- Primary Key structure for table auth_group_profile
-- ----------------------------
ALTER TABLE "public"."auth_group_profile" ADD CONSTRAINT "auth_group_profile_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table auth_permission
-- ----------------------------
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "public"."auth_permission" USING btree (
  "content_type_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_permission
-- ----------------------------
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename");

-- ----------------------------
-- Primary Key structure for table auth_permission
-- ----------------------------
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table auth_token
-- ----------------------------
CREATE INDEX "auth_token_key_c3ca0a8e_like" ON "public"."auth_token" USING btree (
  "key" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table auth_token
-- ----------------------------
ALTER TABLE "public"."auth_token" ADD CONSTRAINT "auth_token_user_id_key" UNIQUE ("user_id");

-- ----------------------------
-- Primary Key structure for table auth_token
-- ----------------------------
ALTER TABLE "public"."auth_token" ADD CONSTRAINT "auth_token_pkey" PRIMARY KEY ("key");

-- ----------------------------
-- Uniques structure for table auth_user_profile
-- ----------------------------
ALTER TABLE "public"."auth_user_profile" ADD CONSTRAINT "auth_user_profile_user_id_key" UNIQUE ("user_id");

-- ----------------------------
-- Primary Key structure for table auth_user_profile
-- ----------------------------
ALTER TABLE "public"."auth_user_profile" ADD CONSTRAINT "auth_user_profile_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table na_cronjob
-- ----------------------------
CREATE INDEX "na_cronjob_creator_id_b8d5de3c" ON "public"."na_cronjob" USING btree (
  "creator_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table na_cronjob
-- ----------------------------
ALTER TABLE "public"."na_cronjob" ADD CONSTRAINT "na_cronjob_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table na_cronjob_job_config
-- ----------------------------
CREATE INDEX "na_cronjob_job_config_creator_id_1cef711c" ON "public"."na_cronjob_job_config" USING btree (
  "creator_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table na_cronjob_job_config
-- ----------------------------
ALTER TABLE "public"."na_cronjob_job_config" ADD CONSTRAINT "na_cronjob_job_config_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table na_cronjob_job_store
-- ----------------------------
CREATE INDEX "na_cronjob_job_store_name_5eddd1ba_like" ON "public"."na_cronjob_job_store" USING btree (
  "name" COLLATE "pg_catalog"."default" "pg_catalog"."varchar_pattern_ops" ASC NULLS LAST
);
CREATE INDEX "na_cronjob_job_store_next_run_time_f2d8329a" ON "public"."na_cronjob_job_store" USING btree (
  "next_run_time" "pg_catalog"."timestamptz_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table na_cronjob_job_store
-- ----------------------------
ALTER TABLE "public"."na_cronjob_job_store" ADD CONSTRAINT "na_cronjob_job_store_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table na_cronjob_job_store
-- ----------------------------
ALTER TABLE "public"."na_cronjob_job_store" ADD CONSTRAINT "na_cronjob_job_store_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table na_cronjob_logs
-- ----------------------------
CREATE INDEX "na_cronjob_logs_cronjob_id_36436a44" ON "public"."na_cronjob_logs" USING btree (
  "cronjob_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table na_cronjob_logs
-- ----------------------------
ALTER TABLE "public"."na_cronjob_logs" ADD CONSTRAINT "na_cronjob_logs_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table na_cronjob_state
-- ----------------------------
CREATE INDEX "na_cronjob_state_cronjob_id_11989daa" ON "public"."na_cronjob_state" USING btree (
  "cronjob_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table na_cronjob_state
-- ----------------------------
ALTER TABLE "public"."na_cronjob_state" ADD CONSTRAINT "na_cronjob_state_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table pub_data_dictionary
-- ----------------------------
CREATE INDEX "pub_data_dictionary_category_id_609170f3" ON "public"."pub_data_dictionary" USING btree (
  "category_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "pub_data_dictionary_creator_id_078c2852" ON "public"."pub_data_dictionary" USING btree (
  "creator_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "pub_data_dictionary_updater_id_99d7a0b6" ON "public"."pub_data_dictionary" USING btree (
  "updater_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table pub_data_dictionary
-- ----------------------------
ALTER TABLE "public"."pub_data_dictionary" ADD CONSTRAINT "pub_data_dictionary_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table pub_data_dictionary_category
-- ----------------------------
CREATE INDEX "pub_data_dictionary_category_creator_id_c661c407" ON "public"."pub_data_dictionary_category" USING btree (
  "creator_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "pub_data_dictionary_category_parent_id_490502cb" ON "public"."pub_data_dictionary_category" USING btree (
  "parent_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "pub_data_dictionary_category_updater_id_5b66a129" ON "public"."pub_data_dictionary_category" USING btree (
  "updater_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table pub_data_dictionary_category
-- ----------------------------
ALTER TABLE "public"."pub_data_dictionary_category" ADD CONSTRAINT "pub_data_dictionary_category_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table pub_data_dictionary_value
-- ----------------------------
CREATE INDEX "pub_data_dictionary_value_creator_id_01d82f16" ON "public"."pub_data_dictionary_value" USING btree (
  "creator_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "pub_data_dictionary_value_dict_id_96fc7326" ON "public"."pub_data_dictionary_value" USING btree (
  "dict_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "pub_data_dictionary_value_updater_id_728417dd" ON "public"."pub_data_dictionary_value" USING btree (
  "updater_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table pub_data_dictionary_value
-- ----------------------------
ALTER TABLE "public"."pub_data_dictionary_value" ADD CONSTRAINT "pub_data_dictionary_value_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table auth_group_profile
-- ----------------------------
ALTER TABLE "public"."auth_group_profile" ADD CONSTRAINT "auth_group_profile_creator_id_24cfa5fc_fk_auth_user_id" FOREIGN KEY ("creator_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."auth_group_profile" ADD CONSTRAINT "auth_group_profile_group_id_d4690e5c_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."auth_group_profile" ADD CONSTRAINT "auth_group_profile_parent_id_174f448a_fk_auth_group_profile_id" FOREIGN KEY ("parent_id") REFERENCES "auth_group_profile" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."auth_group_profile" ADD CONSTRAINT "auth_group_profile_updater_id_b354ab52_fk_auth_user_id" FOREIGN KEY ("updater_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table auth_permission
-- ----------------------------
ALTER TABLE "public"."auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table auth_token
-- ----------------------------
ALTER TABLE "public"."auth_token" ADD CONSTRAINT "auth_token_user_id_d1863690_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table auth_user_profile
-- ----------------------------
ALTER TABLE "public"."auth_user_profile" ADD CONSTRAINT "auth_user_profile_user_id_f9aded29_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table na_cronjob
-- ----------------------------
ALTER TABLE "public"."na_cronjob" ADD CONSTRAINT "na_cronjob_creator_id_b8d5de3c_fk_auth_user_id" FOREIGN KEY ("creator_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table na_cronjob_job_config
-- ----------------------------
ALTER TABLE "public"."na_cronjob_job_config" ADD CONSTRAINT "na_cronjob_job_config_creator_id_1cef711c_fk_auth_user_id" FOREIGN KEY ("creator_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table na_cronjob_logs
-- ----------------------------
ALTER TABLE "public"."na_cronjob_logs" ADD CONSTRAINT "na_cronjob_logs_cronjob_id_36436a44_fk_na_cronjob_id" FOREIGN KEY ("cronjob_id") REFERENCES "na_cronjob" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table na_cronjob_state
-- ----------------------------
ALTER TABLE "public"."na_cronjob_state" ADD CONSTRAINT "na_cronjob_state_cronjob_id_11989daa_fk_na_cronjob_id" FOREIGN KEY ("cronjob_id") REFERENCES "na_cronjob" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table pub_data_dictionary
-- ----------------------------
ALTER TABLE "public"."pub_data_dictionary" ADD CONSTRAINT "pub_data_dictionary_category_id_609170f3_fk_pub_data_" FOREIGN KEY ("category_id") REFERENCES "pub_data_dictionary_category" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."pub_data_dictionary" ADD CONSTRAINT "pub_data_dictionary_creator_id_078c2852_fk_auth_user_id" FOREIGN KEY ("creator_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."pub_data_dictionary" ADD CONSTRAINT "pub_data_dictionary_updater_id_99d7a0b6_fk_auth_user_id" FOREIGN KEY ("updater_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table pub_data_dictionary_category
-- ----------------------------
ALTER TABLE "public"."pub_data_dictionary_category" ADD CONSTRAINT "pub_data_dictionary__creator_id_c661c407_fk_auth_user" FOREIGN KEY ("creator_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."pub_data_dictionary_category" ADD CONSTRAINT "pub_data_dictionary__parent_id_490502cb_fk_pub_data_" FOREIGN KEY ("parent_id") REFERENCES "pub_data_dictionary_category" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."pub_data_dictionary_category" ADD CONSTRAINT "pub_data_dictionary__updater_id_5b66a129_fk_auth_user" FOREIGN KEY ("updater_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;

-- ----------------------------
-- Foreign Keys structure for table pub_data_dictionary_value
-- ----------------------------
ALTER TABLE "public"."pub_data_dictionary_value" ADD CONSTRAINT "pub_data_dictionary__dict_id_96fc7326_fk_pub_data_" FOREIGN KEY ("dict_id") REFERENCES "pub_data_dictionary" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."pub_data_dictionary_value" ADD CONSTRAINT "pub_data_dictionary_value_creator_id_01d82f16_fk_auth_user_id" FOREIGN KEY ("creator_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."pub_data_dictionary_value" ADD CONSTRAINT "pub_data_dictionary_value_updater_id_728417dd_fk_auth_user_id" FOREIGN KEY ("updater_id") REFERENCES "auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
