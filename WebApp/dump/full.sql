CREATE DATABASE  IF NOT EXISTS `wp3` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `wp3`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: wp3
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
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer` (
  `student_number` int NOT NULL,
  `statment_id` int NOT NULL,
  `choice_id` int NOT NULL,
  PRIMARY KEY (`student_number`,`statment_id`),
  KEY `answer_statement_number_id_fk` (`statment_id`),
  KEY `answer_statement_choices_id_fk` (`choice_id`),
  CONSTRAINT `answer_statement_choices_id_fk` FOREIGN KEY (`choice_id`) REFERENCES `statement_choices` (`id`),
  CONSTRAINT `answer_statement_number_id_fk` FOREIGN KEY (`statment_id`) REFERENCES `statement_number` (`id`),
  CONSTRAINT `answer_students_number_fk` FOREIGN KEY (`student_number`) REFERENCES `students` (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statement_choices`
--

DROP TABLE IF EXISTS `statement_choices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statement_choices` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text` varchar(200) NOT NULL,
  `result` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statement_choices`
--

LOCK TABLES `statement_choices` WRITE;
/*!40000 ALTER TABLE `statement_choices` DISABLE KEYS */;
INSERT INTO `statement_choices` VALUES (1,'U gedraagt zich energiek en houdt van drukte.','E'),(2,'U gedraagt zich ingetogen en houdt van rust.','I'),(3,'U vat dingen letterlijk op, u vertrouwt op uw gezonde verstand.','S'),(4,'U zoekt naar de betekenis van dingen, u vertrouwt op uw inzicht.','N'),(5,'U vertrouwt op logica en stelt vragen aan anderen voordat u een beslissing neemt.','T'),(6,'U gaat op uw gevoel af en laat alles op u inwerken voor u een beslissing neemt.','F'),(7,'U bent georganiseerd en netjes.','J'),(8,'U bent ongeorganiseerd en slordig','P'),(9,'U spreekt luid.','E'),(10,'U spreekt zacht.','I'),(11,'U bent praktisch ingesteld.','S'),(12,'U bent creatief ingesteld.','N'),(13,'U bent recht door zee en direct.','T'),(14,'U bent tactvol en bemoedigend.','F'),(15,'U doet alles stap voor stap.','J'),(16,'U doet alles tegelijk.','P'),(17,'U neigt naar actie.','E'),(18,'U neigt naar reflectie.','I'),(19,'U bent gewoon.','S'),(20,'U bent uniek.','N'),(21,'U bent kritisch en wilt argumenten winnen.','T'),(22,'U bent vriendelijk en wil partijen verenigen.','F'),(23,'U houdt van regels en systemen.','J'),(24,'U houdt van improviseren en opties open houden.','P'),(25,'U pakt van alles aan.','E'),(26,'U wilt er eerst over nadenken.','I'),(27,'U staat met beide benen op de grond.','S'),(28,'U bent fantasievol.','N'),(29,'U bent streng en rechtvaardig.','T'),(30,'U bent een gevoelsmens.','F'),(31,'U neemt de spanning weg door op tijd te beginnen.','J'),(32,'U creÃ«ert spanning door op het laatste moment te beginnen.','P'),(33,'U bent actief, u zet zaken in gang.','E'),(34,'U bent passief, u laat zaken over u heen komen.','I'),(35,'U bent vooral gericht op feiten en mensen.','S'),(36,'U bent vooral gericht op ideeÃ«n en fantasie.','N'),(37,'U bent zakelijk en blijft bij het onderwerp.','T'),(38,'U bent gevoelig en dwaalt af als dat zo uitkomt.','F'),(39,'U wilt controle en neemt graag initiatief.','J'),(40,'U wilt vrijheid en initiatief interesseert u niet zo.','P');
/*!40000 ALTER TABLE `statement_choices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statement_number`
--

DROP TABLE IF EXISTS `statement_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statement_number` (
  `id` int NOT NULL AUTO_INCREMENT,
  `choice_a_id` int NOT NULL,
  `choice_b_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `statement_number_statement_choices_id_fk` (`choice_b_id`),
  KEY `statement_number_statement_choices_id_fk_2` (`choice_a_id`),
  CONSTRAINT `statement_number_statement_choices_id_fk` FOREIGN KEY (`choice_b_id`) REFERENCES `statement_choices` (`id`),
  CONSTRAINT `statement_number_statement_choices_id_fk_2` FOREIGN KEY (`choice_a_id`) REFERENCES `statement_choices` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statement_number`
--

LOCK TABLES `statement_number` WRITE;
/*!40000 ALTER TABLE `statement_number` DISABLE KEYS */;
INSERT INTO `statement_number` VALUES (1,1,2),(2,3,4),(3,5,6),(4,7,8),(5,9,10),(6,11,12),(7,13,14),(8,15,16),(9,17,18),(10,19,20),(11,21,22),(12,23,24),(13,25,26),(14,27,28),(15,29,30),(16,31,32),(17,33,34),(18,35,36),(19,37,38),(20,39,40);
/*!40000 ALTER TABLE `statement_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `number` int NOT NULL,
  `class` varchar(2) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1122607,'1A','Imran van Gent-de Bock'),(1145590,'1C','Jenna de Reede-Unruoch Hunerik'),(1154367,'1B','Nynke Ehlert'),(1182671,'1B','Lucas Mansveld-de la Fleche'),(1205529,'1C','Nathan Oosterhout'),(1232429,'1D','Evy Goudriaan'),(1382725,'1B','Melissa van de Noordmark'),(1411164,'1B','Floor van der Horst-Timmermans'),(1772998,'1D','Oscar Wooning-Lathrope'),(1852720,'1C','Jelle Van Bragt'),(1964008,'1E','Bo Kloppert'),(2008557,'1B','Senna Vink-de Hoogh'),(2071260,'1E','Tobias Haengreve'),(2095137,'1D','Sylvie Spiker'),(2232772,'1A','Evi van de Ven'),(2237994,'1D','Fien Meijer'),(2317948,'1C','Bryan Kremer'),(2321500,'1E','Morris van Bovene-Verbeek'),(2338278,'1E','Nathan Olykan-van Wijland'),(2443681,'1D','Lara Jacobs-van Leeuwen'),(2464483,'1D','Aya Maaswinkel'),(2467615,'1A','Jelte West-Francië, van'),(2554236,'1E','Sam die Pelser-Steenbeek'),(2603543,'1C','Mette Ansems'),(2704622,'1D','Liz Ouwerkerk'),(2824197,'1D','Norah van der Kint'),(2891432,'1B','Livia Blaak'),(2926899,'1D','Jacob van der Loo'),(3307255,'1E','Jip Van Bragt'),(3324720,'1A','Ivy Hoogers'),(3351603,'1A','Ivy van Grondelle'),(3425925,'1D','Dylano Blom-Blewanus'),(3518243,'1C','Sophie Simonis-van Salm'),(3558792,'1E','Nina Mansveld'),(3675312,'1C','Rowan Everde'),(3876648,'1E','Zara Volcke'),(3903526,'1E','Dex Hulskes-van den Oever'),(3931563,'1A','Maaike van Asten'),(4168869,'1C','Ise van den Wittenboer'),(4219731,'1B','Mats Stettyn'),(4270903,'1E','Isabel Molen-Kriens'),(4619837,'1D','Lisanne Lucas-Wagenvoort'),(4737466,'1B','Wouter van Oostendorp'),(4965788,'1C','Alyssa Vial-Huijzing'),(4990264,'1E','Frederique van der Sloot-Blaak'),(5074078,'1A','Fien Phillipsen'),(5251171,'1D','Nina le Matelot-Jansdr'),(5481912,'1A','Kai Boeser'),(5499173,'1D','Fenne van Praagh-Bruggeman'),(5508372,'1B','Tyler Koster'),(5682228,'1D','Noud Ellis'),(5715118,'1A','Jinthe Langevoort'),(5758538,'1A','Kyan Guit'),(5973704,'1B','Rayan Dachgelt'),(6031351,'1E','Benjamin Rijn-van de Brink'),(6052614,'1A','Benjamin Strijker'),(6407271,'1D','Anna Winters'),(6409824,'1D','Mason Verkade-Bouhuizen'),(6421308,'1B','Rayan Pieters van der Maes'),(6541270,'1C','Dave de Pauw-Levesque'),(6541371,'1B','Jente Henric van den Nuwenhuse'),(6548779,'1B','Rosa Pauwels'),(6625414,'1D','Nadia Eerden'),(6657465,'1D','Puck Bökenkamp-Brouwer'),(6777308,'1E','Alex Muijs'),(6786988,'1D','Merel Simons'),(6838504,'1D','Riley Wright'),(6840850,'1B','Evie Bolkesteijn'),(7028399,'1D','Amira van Bergen-Texier'),(7123697,'1C','Colin van Goerle'),(7263063,'1A','Isabel van Breugel'),(7278713,'1D','Silke de Kok'),(7332019,'1B','Jill Perck'),(7357386,'1B','Jim Hanegraaff'),(7383264,'1B','Suze de Kale'),(7512863,'1B','Bas Ketting'),(7535802,'1A','Dylano Laffray'),(7549397,'1A','Rens van de Plas'),(7647427,'1A','Mare Mulder'),(7799523,'1A','Ecrin Doesburg'),(7804917,'1A','Evie Fortuyn'),(8124341,'1D','Danique Velderman'),(8167154,'1C','Quinty Chotzen'),(8179910,'1C','Michael van der Ven'),(8239435,'1A','Maartje Lansink-Otto'),(8475295,'1C','Sebastiaan de Vries'),(8488333,'1E','Ryan Westermann'),(8826007,'1B','Yara van Engelen'),(8831873,'1E','Stan Spies'),(8931645,'1C','Isabella Spreeuw-Slaetsdochter'),(9037811,'1B','Aiden Arnold'),(9103907,'1D','Nynke van Hamaland'),(9215154,'1D','Isis Dijkman-van den Velden'),(9284742,'1E','Jules van Verdun'),(9293310,'1A','Jan Rackham-van Mil'),(9433357,'1C','Lisanne Janssen'),(9688523,'1B','Danique de Bock'),(9782420,'1B','Philip Passchiers'),(9817946,'1B','Rowan Vignon');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-06 15:45:59
