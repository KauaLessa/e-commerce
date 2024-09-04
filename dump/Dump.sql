CREATE DATABASE  IF NOT EXISTS `ec_users` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ec_users`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ec_users
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add locations',1,'add_locations'),(2,'Can change locations',1,'change_locations'),(3,'Can delete locations',1,'delete_locations'),(4,'Can view locations',1,'view_locations'),(5,'Can add logins',2,'add_logins'),(6,'Can change logins',2,'change_logins'),(7,'Can delete logins',2,'delete_logins'),(8,'Can view logins',2,'view_logins'),(9,'Can add custom user',3,'add_customuser'),(10,'Can change custom user',3,'change_customuser'),(11,'Can delete custom user',3,'delete_customuser'),(12,'Can view custom user',3,'view_customuser'),(13,'Can add products',4,'add_products'),(14,'Can change products',4,'change_products'),(15,'Can delete products',4,'delete_products'),(16,'Can view products',4,'view_products'),(17,'Can add log entry',5,'add_logentry'),(18,'Can change log entry',5,'change_logentry'),(19,'Can delete log entry',5,'delete_logentry'),(20,'Can view log entry',5,'view_logentry'),(21,'Can add permission',6,'add_permission'),(22,'Can change permission',6,'change_permission'),(23,'Can delete permission',6,'delete_permission'),(24,'Can view permission',6,'view_permission'),(25,'Can add group',7,'add_group'),(26,'Can change group',7,'change_group'),(27,'Can delete group',7,'delete_group'),(28,'Can view group',7,'view_group'),(29,'Can add user',8,'add_user'),(30,'Can change user',8,'change_user'),(31,'Can delete user',8,'delete_user'),(32,'Can view user',8,'view_user'),(33,'Can add content type',9,'add_contenttype'),(34,'Can change content type',9,'change_contenttype'),(35,'Can delete content type',9,'delete_contenttype'),(36,'Can view content type',9,'view_contenttype'),(37,'Can add session',10,'add_session'),(38,'Can change session',10,'change_session'),(39,'Can delete session',10,'delete_session'),(40,'Can view session',10,'view_session'),(41,'Can add cart item',11,'add_cartitem'),(42,'Can change cart item',11,'change_cartitem'),(43,'Can delete cart item',11,'delete_cartitem'),(44,'Can view cart item',11,'view_cartitem'),(45,'Can add product',12,'add_product'),(46,'Can change product',12,'change_product'),(47,'Can delete product',12,'delete_product'),(48,'Can view product',12,'view_product'),(49,'Can add cart',13,'add_cart'),(50,'Can change cart',13,'change_cart'),(51,'Can delete cart',13,'delete_cart'),(52,'Can view cart',13,'view_cart'),(53,'Can add product review',14,'add_productreview'),(54,'Can change product review',14,'change_productreview'),(55,'Can delete product review',14,'delete_productreview'),(56,'Can view product review',14,'view_productreview'),(57,'Can add product',15,'add_product'),(58,'Can change product',15,'change_product'),(59,'Can delete product',15,'delete_product'),(60,'Can view product',15,'view_product'),(61,'Can add cart item',16,'add_cartitem'),(62,'Can change cart item',16,'change_cartitem'),(63,'Can delete cart item',16,'delete_cartitem'),(64,'Can view cart item',16,'view_cartitem'),(65,'Can add cart',17,'add_cart'),(66,'Can change cart',17,'change_cart'),(67,'Can delete cart',17,'delete_cart'),(68,'Can view cart',17,'view_cart'),(69,'Can add department',18,'add_department'),(70,'Can change department',18,'change_department'),(71,'Can delete department',18,'delete_department'),(72,'Can view department',18,'view_department'),(73,'Can add product review',19,'add_productreview'),(74,'Can change product review',19,'change_productreview'),(75,'Can delete product review',19,'delete_productreview'),(76,'Can view product review',19,'view_productreview');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$ZxYFTQ67N7AxYpH8RjukHY$XC3H7fByG8F1t7MfGKWD5gsB66vMwiGFNwQTNDBxMqc=','2024-08-30 15:27:45.392432',0,'Pedro','','','pedro@gmail.com',0,1,'2024-08-09 21:31:38.533642'),(2,'pbkdf2_sha256$720000$aSQElIAii7gtJAzkLIbBWx$ncVttv9+SP33/8Ht5tH04u/9uolnaLlLeJLUBkcH1Sk=','2024-08-24 03:42:48.454924',0,'James','','','james@gmail.com',0,1,'2024-08-23 20:23:43.862417'),(3,'pbkdf2_sha256$720000$v0jV15UytnQla8WE3ZoXyS$TPwZGYntVMO4NtyuCBAHUWrzeHkOOQoznV29Lv648Jk=','2024-08-30 20:15:22.277965',0,'admin','','','admin@gmail.com',1,1,'2024-08-23 21:33:05.792168'),(4,'pbkdf2_sha256$720000$xI3n6qF3XOQrLFWWWze1tK$Yu1mWU/tkJEmrJPVKVnevMqPkz5hRSOlOB57ClR+yGc=',NULL,0,'Arthur','','','arthur@gmail.com',0,1,'2024-08-24 03:42:13.174063'),(5,'pbkdf2_sha256$720000$m94Cao3YmgFruOpkWFirFb$GpPC1EBY0pU8FYdsTBGpXheXVEbUjRK420VUXgIk1EM=',NULL,0,'Rodrigo','','','rodrigo@gmail.com',0,1,'2024-08-28 05:07:36.260364'),(6,'pbkdf2_sha256$720000$DS82HzCcuoKjun0tz54B0g$xa4bkE5Dk/3zW2NTImDuYpAo8lJyL6g25iJBx7G6IEk=','2024-08-28 12:32:23.348561',0,'matheus','','','matheus@gmail.com',0,1,'2024-08-28 05:12:56.594502'),(7,'pbkdf2_sha256$720000$e0qSxpb1VUxYGWrDxg6VI0$vWYsFrHiE9f/OMCUm/p/B0o9Z/YPRR3n2mfnwdWYHoY=','2024-08-28 05:51:10.780455',0,'junior','','','junior@gmail.com',0,1,'2024-08-28 05:51:00.600946'),(9,'pbkdf2_sha256$720000$S7ul7X0mVfomGfGBRYUIYN$BtUpjtJ1hk5jkV5RmVlxTHG6EA8Sv20KPxOyPnsHvOg=','2024-08-29 19:22:22.446240',0,'ana','','','ana@gmail.com',0,1,'2024-08-29 19:22:15.525279');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_customuser`
--

DROP TABLE IF EXISTS `client_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `client_customuser_user_id_f693055c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_customuser`
--

LOCK TABLES `client_customuser` WRITE;
/*!40000 ALTER TABLE `client_customuser` DISABLE KEYS */;
INSERT INTO `client_customuser` VALUES (1,1);
/*!40000 ALTER TABLE `client_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (5,'admin','logentry'),(7,'auth','group'),(6,'auth','permission'),(8,'auth','user'),(3,'client','customuser'),(1,'client','locations'),(2,'client','logins'),(9,'contenttypes','contenttype'),(17,'products','cart'),(16,'products','cartitem'),(18,'products','department'),(15,'products','product'),(19,'products','productreview'),(4,'products','products'),(13,'products2','cart'),(11,'products2','cartitem'),(12,'products2','product'),(14,'products2','productreview'),(10,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-08-09 21:11:42.473776'),(2,'auth','0001_initial','2024-08-09 21:12:29.225489'),(3,'admin','0001_initial','2024-08-09 21:12:38.901596'),(4,'admin','0002_logentry_remove_auto_add','2024-08-09 21:12:39.149732'),(5,'admin','0003_logentry_add_action_flag_choices','2024-08-09 21:12:39.375822'),(6,'contenttypes','0002_remove_content_type_name','2024-08-09 21:12:44.466770'),(7,'auth','0002_alter_permission_name_max_length','2024-08-09 21:12:48.773676'),(8,'auth','0003_alter_user_email_max_length','2024-08-09 21:12:49.385868'),(9,'auth','0004_alter_user_username_opts','2024-08-09 21:12:49.679618'),(10,'auth','0005_alter_user_last_login_null','2024-08-09 21:12:53.439349'),(11,'auth','0006_require_contenttypes_0002','2024-08-09 21:12:53.719773'),(12,'auth','0007_alter_validators_add_error_messages','2024-08-09 21:12:53.932005'),(13,'auth','0008_alter_user_username_max_length','2024-08-09 21:12:58.872839'),(14,'auth','0009_alter_user_last_name_max_length','2024-08-09 21:13:04.163590'),(15,'auth','0010_alter_group_name_max_length','2024-08-09 21:13:04.907386'),(16,'auth','0011_update_proxy_permissions','2024-08-09 21:13:05.132666'),(17,'auth','0012_alter_user_first_name_max_length','2024-08-09 21:13:10.060075'),(18,'client','0001_initial','2024-08-09 21:13:10.396031'),(19,'client','0002_delete_products','2024-08-09 21:13:10.757576'),(20,'client','0003_alter_logins_options','2024-08-09 21:13:11.069177'),(21,'client','0004_customuser','2024-08-09 21:13:18.268339'),(22,'products','0001_initial','2024-08-09 21:13:18.447894'),(23,'products','0002_alter_products_options','2024-08-09 21:13:18.693327'),(24,'products','0003_products_discount','2024-08-09 21:59:51.833192'),(25,'sessions','0001_initial','2024-08-09 21:59:56.560336'),(29,'products2','0001_initial','2024-08-27 14:49:24.783717'),(30,'products2','0002_alter_product_image','2024-08-27 14:49:25.656537'),(31,'products2','0003_alter_product_image','2024-08-27 14:49:26.357568'),(32,'products2','0004_remove_cartitem_user_cart_cartitem_cart','2024-08-27 14:55:23.846273'),(33,'products2','0005_alter_cartitem_cart','2024-08-27 15:18:15.929289'),(34,'products2','0006_productreview','2024-08-27 22:08:57.955804'),(35,'products2','0007_productreview_review','2024-08-27 22:26:49.197319'),(36,'products2','0008_alter_productreview_review','2024-08-27 22:27:33.191465'),(37,'products2','0009_alter_product_price','2024-08-28 03:38:41.587318'),(38,'products','0002_alter_product_image','2024-08-28 04:58:08.125644'),(39,'products','0003_alter_product_image','2024-08-28 04:58:08.574756'),(40,'products','0004_remove_cartitem_user_cart_cartitem_cart','2024-08-28 05:05:19.624118'),(41,'products','0005_alter_cartitem_cart','2024-08-28 05:05:20.105382'),(42,'products','0006_productreview','2024-08-28 05:05:20.727270'),(43,'products','0007_productreview_review','2024-08-28 05:05:21.021826'),(44,'products','0008_alter_productreview_review','2024-08-28 05:05:21.223180'),(45,'products','0009_alter_product_price','2024-08-28 05:05:21.493801'),(46,'products','0010_department_product_department','2024-08-29 19:47:52.297934'),(47,'products','0011_department_discount_percent_product_discount_percent_and_more','2024-08-30 03:18:27.352511');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('952rz8zhzp1iknc4wvms8m2h2pja829w','.eJxVjDsOwyAQBe9CHSHzMQsp0_sMaGEhOIlAMnYV5e6xJRdJOzPvvZnHbS1-62nxM7ErU-zyywLGZ6qHoAfWe-Ox1XWZAz8SftrOp0bpdTvbv4OCvexrsKQVOAITbCAJYYijixK0s6QE5pjBOY0ATsWcM447Q2NQEAyKpGCfL-WNOB4:1sjIZg:GcIKNl54Q-cbVNgMRDVhqmVK5ZBafyqw0q8xwp_UEyY','2024-09-11 13:19:00.358468'),('s28k4qi1ynpagvmkxvebwx23h3kncewt','.eJxVjEEOgjAURO_StWnaX8Di0j1nIL-dX0FNm1BYGe-uJCx0O--9eamRt3UatyrLOENdlFOn3y1wfEjeAe6cb0XHktdlDnpX9EGrHgrkeT3cv4OJ6_St22gMnw01REArCUngOpdgg-tjxxDvkRw1vSVuPVnuvJgQYcHMBur9AfoBONU:1shdhS:QP9VJEiwOAo38Bkg2z4b2qvlLdm84cAK_biTrwTRWlc','2024-09-06 23:28:10.497836'),('sqr620jgcvv43zakywzpwva4sqkgldfr','.eJxVjEsOAiEQBe_C2hBsPoJL956BNHQjowaSYWZlvLtOMgvdvqp6LxFxXWpcB89xInEWWhx-t4T5wW0DdMd26zL3tsxTkpsidzrktRM_L7v7d1Bx1G9dMHNOrBV6cEQhOLDeAilvTIDCAdCgMZZSKKCBcmGfyEFW5RSOQOL9Af6yOG4:1sj8rL:_o8Fo1pEEBnQBao4G6H8b7erdXbJ0k0jC_byETvBcxA','2024-09-11 02:56:35.113950'),('vyxed0og1x2ddg3e540jw619r0dlfeu8','.eJxVjDsOwjAQBe_iGlnY8ZeSPmewdr1rHECOFCcV4u4QKQW0b2beSyTY1pq2zkuaSFzEIE6_G0J-cNsB3aHdZpnnti4Tyl2RB-1ynImf18P9O6jQ67cGE63TfEaDhErr6G3xylJwEF3wxQ0IBDFkbQ0QMqqiiW0OqLzHYsT7A-TvOG4:1sk81j:pGvOCyM_JOuIGNdmFyymkR2uOw4zdHyXZcVfJVtGKlQ','2024-09-13 20:15:23.043565');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `location_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `country` varchar(15) DEFAULT NULL,
  `state` varchar(15) DEFAULT NULL,
  `city` varchar(15) DEFAULT NULL,
  `district` varchar(15) DEFAULT NULL,
  `street` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`location_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `locations_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `logins` (`user_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,1,'Brazil','Alagoas','Maceió','Ponta Verde','Sandoval Arroxelas');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logins`
--

DROP TABLE IF EXISTS `logins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logins` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT '0',
  `creation_date` date DEFAULT (curdate()),
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logins`
--

LOCK TABLES `logins` WRITE;
/*!40000 ALTER TABLE `logins` DISABLE KEYS */;
INSERT INTO `logins` VALUES (1,'ADMIN','admin@gmail.com','password',1,'2024-07-24'),(2,'caio','caio@gmail.com','password',0,'2024-07-24');
/*!40000 ALTER TABLE `logins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_cart`
--

DROP TABLE IF EXISTS `products_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_cart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `total_items` int NOT NULL,
  `total_cost` decimal(12,2) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products2_cart_user_id_cd4bb00c_fk_auth_user_id` (`user_id`),
  CONSTRAINT `products2_cart_user_id_cd4bb00c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_cart`
--

LOCK TABLES `products_cart` WRITE;
/*!40000 ALTER TABLE `products_cart` DISABLE KEYS */;
INSERT INTO `products_cart` VALUES (1,0,0.00,3),(2,0,0.00,6),(3,0,0.00,7),(4,0,0.00,9),(5,0,0.00,1);
/*!40000 ALTER TABLE `products_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_cartitem`
--

DROP TABLE IF EXISTS `products_cartitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_cartitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `date_added` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL,
  `cart_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products2_cartitem_product_id_e1939db2_fk_products2_product_id` (`product_id`),
  KEY `products2_cartitem_cart_id_75095ae1_fk_products2_cart_id` (`cart_id`),
  CONSTRAINT `products2_cartitem_cart_id_75095ae1_fk_products2_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `products_cart` (`id`),
  CONSTRAINT `products2_cartitem_product_id_e1939db2_fk_products2_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `products_cartitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_cartitem`
--

LOCK TABLES `products_cartitem` WRITE;
/*!40000 ALTER TABLE `products_cartitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_cartitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_department`
--

DROP TABLE IF EXISTS `products_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_department` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `dp` varchar(100) NOT NULL,
  `discount_percent` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_department`
--

LOCK TABLES `products_department` WRITE;
/*!40000 ALTER TABLE `products_department` DISABLE KEYS */;
INSERT INTO `products_department` VALUES (1,'electronics',10.00),(2,'home',0.00),(3,'books',0.00);
/*!40000 ALTER TABLE `products_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_product`
--

DROP TABLE IF EXISTS `products_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext,
  `price` decimal(10,2) NOT NULL,
  `image` varchar(100) NOT NULL,
  `date_added` datetime(6) NOT NULL,
  `department_id` bigint DEFAULT NULL,
  `discount_percent` decimal(5,2) NOT NULL,
  `sale_price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_product_department_id_bf781245_fk_products_` (`department_id`),
  CONSTRAINT `products_product_department_id_bf781245_fk_products_` FOREIGN KEY (`department_id`) REFERENCES `products_department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_product`
--

LOCK TABLES `products_product` WRITE;
/*!40000 ALTER TABLE `products_product` DISABLE KEYS */;
INSERT INTO `products_product` VALUES (1,'Iphone','This is an Iphone',3200.00,'media/iphone.jpg','2024-08-24 21:26:13.026133',1,0.00,2880.00),(2,'Iphone 15','Chip A16 Bionic com. GPU de 5 núcleos · Sistema avançado de câmera dupla. Câmera grande-angular de 48 MP Teleobjetiva de 2x. Câmera ultra-angular.',4000.00,'media/iphone_15.jpg','2024-08-25 21:53:31.344318',1,0.00,3600.00),(3,'Iphone 13','This is an iphone 13',3500.00,'media/iphone_13.jpg','2024-08-25 21:54:20.359419',1,0.00,3150.00),(5,'Iphone 11','This is an Iphone 11',2500.00,'media/iphone_11.jpg','2024-08-25 22:16:52.990652',1,0.00,2250.00),(7,'Phone','This is a smartphone',2500.00,'media/iphone_11_deDz80m.jpg','2024-08-28 04:30:22.384551',1,0.00,2250.00),(8,'Iphone smartphone','This is phone 2',3000.00,'media/iphone_15_LRflnKG.jpg','2024-08-28 06:05:51.303226',1,0.00,2700.00);
/*!40000 ALTER TABLE `products_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productreview`
--

DROP TABLE IF EXISTS `products_productreview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_productreview` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` int NOT NULL,
  `product_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `review` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products2_productrev_product_id_93cc101c_fk_products2` (`product_id`),
  KEY `products2_productreview_user_id_14de46c9_fk_auth_user_id` (`user_id`),
  CONSTRAINT `products2_productrev_product_id_93cc101c_fk_products2` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  CONSTRAINT `products2_productreview_user_id_14de46c9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productreview`
--

LOCK TABLES `products_productreview` WRITE;
/*!40000 ALTER TABLE `products_productreview` DISABLE KEYS */;
INSERT INTO `products_productreview` VALUES (4,5,2,3,'This smartphone is amazing'),(5,3,7,3,'Good phone'),(6,5,8,3,'This phone is great!'),(7,3,2,3,'Not the best Iphone'),(8,4,2,3,'Almost perfect.');
/*!40000 ALTER TABLE `products_productreview` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-04  0:46:12
