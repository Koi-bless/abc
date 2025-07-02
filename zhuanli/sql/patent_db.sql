/*
 Navicat Premium Dump SQL

 Source Server         : connect01
 Source Server Type    : MySQL
 Source Server Version : 80042 (8.0.42)
 Source Host           : localhost:3306
 Source Schema         : patent_db

 Target Server Type    : MySQL
 Target Server Version : 80042 (8.0.42)
 File Encoding         : 65001

 Date: 02/07/2025 12:01:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for patent
-- ----------------------------
DROP TABLE IF EXISTS province_patent;
CREATE TABLE `patent`  (
  `province` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `nums` int NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of patent
-- ----------------------------
INSERT INTO province_patent VALUES ('北京市', 3014173);
INSERT INTO province_patent VALUES ('天津市', 1007268);
INSERT INTO province_patent VALUES ('河北省', 1060139);
INSERT INTO province_patent VALUES ('山西省', 364725);
INSERT INTO province_patent VALUES ('内蒙古自治区', 239899);
INSERT INTO province_patent VALUES ('辽宁省', 953641);
INSERT INTO province_patent VALUES ('吉林省', 362593);
INSERT INTO province_patent VALUES ('黑龙江省', 506128);
INSERT INTO province_patent VALUES ('上海市', 157111);
INSERT INTO province_patent VALUES ('江苏省', 7097313);
INSERT INTO province_patent VALUES ('浙江省', 5474525);
INSERT INTO province_patent VALUES ('安徽省', 2029089);
INSERT INTO province_patent VALUES ('福建省', 1573334);
INSERT INTO province_patent VALUES ('江西省', 789983);
INSERT INTO province_patent VALUES ('山东省', 3352037);
INSERT INTO province_patent VALUES ('河南省', 1477330);
INSERT INTO province_patent VALUES ('湖北省', 1555257);
INSERT INTO province_patent VALUES ('湖南省', 1085998);
INSERT INTO province_patent VALUES ('广东省', 8686514);
INSERT INTO province_patent VALUES ('广西壮族自治区', 544270);
INSERT INTO province_patent VALUES ('海南省', 113590);
INSERT INTO province_patent VALUES ('重庆市', 891366);
INSERT INTO province_patent VALUES ('四川省', 1699457);
INSERT INTO province_patent VALUES ('贵州省', 388446);
INSERT INTO province_patent VALUES ('云南省', 406999);
INSERT INTO province_patent VALUES ('西藏自治区', 18691);
INSERT INTO province_patent VALUES ('陕西省', 1002587);
INSERT INTO province_patent VALUES ('甘肃省', 258984);
INSERT INTO province_patent VALUES ('青海省', 55456);
INSERT INTO province_patent VALUES ('宁夏回族自治区', 113458);
INSERT INTO province_patent VALUES ('新疆维吾尔自治区', 217361);
INSERT INTO province_patent VALUES ('台湾省', 482892);
INSERT INTO province_patent VALUES ('香港特别行政区', 76039);
INSERT INTO province_patent VALUES ('澳门特别行政区', 1434);

-- ----------------------------
-- Table structure for train
-- ----------------------------
DROP TABLE IF EXISTS `train`;
CREATE TABLE `train`  (
  `year` int NULL DEFAULT NULL,
  `nums` double NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of train
-- ----------------------------
INSERT INTO `train` VALUES (1985, 0.1);
INSERT INTO `train` VALUES (1986, 0.7);
INSERT INTO `train` VALUES (1987, 1.3);
INSERT INTO `train` VALUES (1988, 2.1);
INSERT INTO `train` VALUES (1989, 2.7);
INSERT INTO `train` VALUES (1990, 2.6);
INSERT INTO `train` VALUES (1991, 3.4);
INSERT INTO `train` VALUES (1992, 4.8);
INSERT INTO `train` VALUES (1993, 4);
INSERT INTO `train` VALUES (1994, 5.2);
INSERT INTO `train` VALUES (1995, 4.9);
INSERT INTO `train` VALUES (1996, 5);
INSERT INTO `train` VALUES (1997, 5.6);
INSERT INTO `train` VALUES (1998, 6.7);
INSERT INTO `train` VALUES (1999, 10);
INSERT INTO `train` VALUES (2000, 11);
INSERT INTO `train` VALUES (2001, 12.3);
INSERT INTO `train` VALUES (2002, 14.2);
INSERT INTO `train` VALUES (2003, 18.4);
INSERT INTO `train` VALUES (2004, 19.6);
INSERT INTO `train` VALUES (2005, 24.6);
INSERT INTO `train` VALUES (2006, 30.5);
INSERT INTO `train` VALUES (2007, 40.8);
INSERT INTO `train` VALUES (2008, 50.1);
INSERT INTO `train` VALUES (2009, 66.1);
INSERT INTO `train` VALUES (2010, 92.9);
INSERT INTO `train` VALUES (2011, 111.4);
INSERT INTO `train` VALUES (2012, 156.5);
INSERT INTO `train` VALUES (2013, 184.9);
INSERT INTO `train` VALUES (2014, 187.7);
INSERT INTO `train` VALUES (2015, 243.5);
INSERT INTO `train` VALUES (2016, 259.8);
INSERT INTO `train` VALUES (2017, 286);
INSERT INTO `train` VALUES (2018, 369.6);
INSERT INTO `train` VALUES (2019, 382.7);
INSERT INTO `train` VALUES (2020, 485.2);
INSERT INTO `train` VALUES (2021, 601.8);
INSERT INTO `train` VALUES (2022, 573.2);
INSERT INTO `train` VALUES (2023, 492);
INSERT INTO `train` VALUES (2024, 656.3);

SET FOREIGN_KEY_CHECKS = 1;
