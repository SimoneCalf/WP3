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
-- Table structure for table `answers`
--

DROP TABLE IF EXISTS `answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answers` (
  `idanswers` int NOT NULL,
  `statement_numbre_1` varchar(1) DEFAULT NULL,
  `statement_numbre_2` varchar(1) DEFAULT NULL,
  `statement_numbre_3` varchar(1) DEFAULT NULL,
  `statement_numbre_4` varchar(1) DEFAULT NULL,
  `statement_numbre_5` varchar(1) DEFAULT NULL,
  `statement_numbre_6` varchar(1) DEFAULT NULL,
  `statement_numbre_7` varchar(1) DEFAULT NULL,
  `statement_numbre_8` varchar(1) DEFAULT NULL,
  `statement_numbre_9` varchar(1) DEFAULT NULL,
  `statement_numbre_10` varchar(1) DEFAULT NULL,
  `statement_numbre_11` varchar(1) DEFAULT NULL,
  `statement_numbre_12` varchar(1) DEFAULT NULL,
  `statement_numbre_13` varchar(1) DEFAULT NULL,
  `statement_numbre_14` varchar(1) DEFAULT NULL,
  `statement_numbre_15` varchar(1) DEFAULT NULL,
  `statement_numbre_16` varchar(1) DEFAULT NULL,
  `statement_numbre_17` varchar(1) DEFAULT NULL,
  `statement_numbre_18` varchar(1) DEFAULT NULL,
  `statement_numbre_19` varchar(1) DEFAULT NULL,
  `statement_numbre_20` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`idanswers`),
  CONSTRAINT `studentid` FOREIGN KEY (`idanswers`) REFERENCES `students` (`studentid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-03  9:24:21
