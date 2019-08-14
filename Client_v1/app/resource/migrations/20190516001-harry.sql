/*
 Navicat Premium Data Transfer

 Source Server         : data-testing
 Source Server Type    : SQLite
 Source Server Version : 3021000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3021000
 File Encoding         : 65001

 Date: 16/05/2019 08:33:54
*/

-- ----------------------------
-- Records of na_config
-- ----------------------------
INSERT OR REPLACE INTO "na_config"("fid", "name", "main_key", "minor_key", "value", "tip", "type", "sort")  VALUES (1, 'User Password', 'user', 'password', 'admin', '', 2, 2);
INSERT OR REPLACE INTO "na_config"("fid", "name", "main_key", "minor_key", "value", "tip", "type", "sort") VALUES (1, 'User Account', 'user', 'account', 'admin', '', 1, 1);
INSERT OR REPLACE INTO "na_config"("fid", "name", "main_key", "minor_key", "value", "tip", "type", "sort")  VALUES (1, 'User Language', 'user', 'language', '简体中文', NULL, 2, 3);
INSERT OR REPLACE INTO "na_config"("fid", "name", "main_key", "minor_key", "value", "tip", "type", "sort")  VALUES (0, 'Service URL', 'setting', 'leServiceUrl', 'http://127.0.0.1:8000', NULL, 1, 1);

