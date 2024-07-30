-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: our_users
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `idteachers` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `e-mailadres` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `is_admin` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`idteachers`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (11,'John','Doe','1234567@hr.nl','password1',0),(12,'Jane','Smith','2345678@hr.nl','password2',0),(13,'Alice','Johnson','3456789@hr.nl','password3',0),(14,'Robert','Williams','4567890@hr.nl','password4',0),(15,'Michael','Brown','5678901@hr.nl','password5',0),(16,'Linda','Jones','6789012@hr.nl','password6',0),(17,'James','Garcia','7890123@hr.nl','password7',0),(18,'Mary','Miller','8901234@hr.nl','password8',0),(19,'William','Davis','9012345@hr.nl','password9',0),(20,'Patricia','Martinez','0123456@hr.nl','password10',0),(21,'Emily','Taylor','1122334@hr.nl','adminpass1',1),(22,'David','Wilson','2233445@hr.nl','adminpass2',1),(23,'Sophia','Moore','3344556@hr.nl','adminpass3',1),(24,'Oliver','Harris','4455667@hr.nl','adminpass4',1),(25,'Isabella','Clark','5566778@hr.nl','adminpass5',1),(26,'Liam','Lewis','6677889@hr.nl','adminpass6',1),(27,'Mia','Walker','7788990@hr.nl','adminpass7',1),(28,'Ethan','Roberts','8899001@hr.nl','adminpass8',1),(29,'Ava','Lee','9900112@hr.nl','adminpass9',1),(30,'Noah','Young','1011223@hr.nl','adminpass10',1);
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-25 17:30:47
