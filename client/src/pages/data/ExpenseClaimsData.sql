CREATE DATABASE  IF NOT EXISTS `ExpenseClaimsData` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ExpenseClaimsData`;
-- MySQL dump 10.13  Distrib 8.0.21, for macos10.15 (x86_64)
--
-- Host: localhost    Database: ExpenseClaimsData
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `Currency`
--

DROP TABLE IF EXISTS `Currency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Currency` (
  `CurrencyID` varchar(3) NOT NULL,
  `ExchangeRate` float DEFAULT NULL,
  PRIMARY KEY (`CurrencyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Currency`
--

LOCK TABLES `Currency` WRITE;
/*!40000 ALTER TABLE `Currency` DISABLE KEYS */;
INSERT INTO `Currency` VALUES ('CNY',0.206),('HKD',0.17),('IDR',0.000093),('INR',0.018),('JPY',0.012),('KHR',0.00025),('KRW',0.0011),('SGD',1),('TWD',0.045),('VND',0.000044);
/*!40000 ALTER TABLE `Currency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Department`
--

DROP TABLE IF EXISTS `Department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Department` (
  `DepartmentCode` varchar(3) NOT NULL,
  `DepartmentName` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`DepartmentCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Department`
--

LOCK TABLES `Department` WRITE;
/*!40000 ALTER TABLE `Department` DISABLE KEYS */;
INSERT INTO `Department` VALUES ('101','Sales'),('102','Marketing'),('103','Human Resources'),('104','Finance'),('105','Information Technology'),('106','Customer Service'),('107','Engineering'),('108','Research and Development'),('109','Procurement'),('110','Insurance');
/*!40000 ALTER TABLE `Department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee` (
  `EmployeeID` int NOT NULL,
  `SupervisorID` int DEFAULT NULL,
  `DepartmentCode` varchar(3) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `FirstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `BankAccountNumber` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`),
  KEY `SupervisorID` (`SupervisorID`),
  KEY `DepartmentCode` (`DepartmentCode`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`SupervisorID`) REFERENCES `Employee` (`EmployeeID`),
  CONSTRAINT `employee_ibfk_2` FOREIGN KEY (`DepartmentCode`) REFERENCES `Department` (`DepartmentCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES (10001,NULL,'101','Singa@123','Aisha','Tan','1234567890'),(10002,10001,'101','LaKopi123!','Jia Hui','Lee','2345678901'),(10003,10001,'102','SedapNyumyum77','Nurul','Lim','3456789012'),(10004,NULL,'102','GulaMelaka#1','Siti','Baiduri','4567890123'),(10005,10002,'103','Majulah*Sg123','Shan','Chong','5678901234'),(10006,10002,'103','ShiokLah99!','Kai Ming','Tan','6789012345'),(10007,10003,'104','ChopeSeat_88','Rajesh','Kumar','7890123456'),(10008,10003,'104','SiaLah#123','Siti','Jamilah','8901234567'),(10009,NULL,'105','ShiokLah88#','Wei Ting','Tan','9012345678'),(10010,NULL,'105','Majulah_Sg99','Johnny','Ng','1123456789'),(10011,10006,'106','SedapNyumyum55','Siti','Zubaidah','2345678903'),(10012,10006,'106','KayaToast789#','Kok Wai','Lee','3456789014'),(10013,10007,'107','LaKopi_123','Deepa','Padukone','4567890125'),(10014,10007,'107','ShiokLah_77','Wei Jian','Chua','5678901235'),(10015,10008,'108','ChopeSeat99#','Saravanan','Kumar','6789012349'),(10016,10008,'108','GulaMelaka11#','Xiao Mei','Goh','7890123450'),(10017,NULL,'109','Majulah_Sg77','Rahman','Tan','8901234566'),(10018,NULL,'109','SedapNyumyum66','Ying Ying','Loh','9012345677'),(10019,10011,'110','LaKopi11#','Munirah','Yasin','0123456781'),(10020,10011,'110','SiaLah33#','Ganesan','Laksamana','1234567892');
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EmployeeProjects`
--

DROP TABLE IF EXISTS `EmployeeProjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EmployeeProjects` (
  `ProjectID` int NOT NULL,
  `EmployeeID` int DEFAULT NULL,
  `ProjectName` varchar(100) DEFAULT NULL,
  `ProjectStatus` varchar(50) DEFAULT NULL,
  `ProjectBudget` float DEFAULT NULL,
  `ProjectLeadID` int DEFAULT NULL,
  PRIMARY KEY (`ProjectID`),
  KEY `EmployeeID` (`EmployeeID`),
  KEY `ProjectLeadID` (`ProjectLeadID`),
  CONSTRAINT `employeeprojects_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `Employee` (`EmployeeID`),
  CONSTRAINT `employeeprojects_ibfk_2` FOREIGN KEY (`ProjectLeadID`) REFERENCES `Employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EmployeeProjects`
--

LOCK TABLES `EmployeeProjects` WRITE;
/*!40000 ALTER TABLE `EmployeeProjects` DISABLE KEYS */;
INSERT INTO `EmployeeProjects` VALUES (10001,10001,'Mobile Banking App','In Progress',15000,10002),(10002,10003,'Online Payment Gateway','Completed',25000,10004),(10003,10005,'ATM Upgrade','In Progress',18000,10006),(10004,10007,'Credit Scoring System','Terminated',30000,10008),(10005,10009,'Core Banking System Migration','In Progress',20000,10010),(10006,10011,'Digital Onboarding Platform','Yet To Commence',35000,10012),(10007,10013,'Trade Finance Automation','Completed',27000,10014),(10008,10015,'Customer Data Management System','In Progress',19000,10016),(10009,10017,'Risk Management Dashboard','Terminated',32000,10018),(10010,10019,'Loan Origination System','Yet To Commence',40000,10020);
/*!40000 ALTER TABLE `EmployeeProjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProjectExpenseClaims`
--

DROP TABLE IF EXISTS `ProjectExpenseClaims`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ProjectExpenseClaims` (
  `ClaimID` int NOT NULL,
  `ProjectID` int NOT NULL,
  `EmployeeID` int DEFAULT NULL,
  `CurrencyID` varchar(3) NOT NULL,
  `ExpenseDate` datetime NOT NULL,
  `Amount` decimal(10,2) NOT NULL,
  `Purpose` varchar(255) NOT NULL,
  `ChargeToDefaultDept` bit(1) NOT NULL,
  `AlternativeDeptCode` varchar(50) NOT NULL,
  `Status` varchar(20) NOT NULL,
  `LastEditedClaimDate` datetime NOT NULL,
  PRIMARY KEY (`ClaimID`),
  KEY `EmployeeID` (`EmployeeID`),
  KEY `ProjectID` (`ProjectID`),
  KEY `CurrencyID` (`CurrencyID`),
  CONSTRAINT `projectexpenseclaims_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `Employee` (`EmployeeID`),
  CONSTRAINT `projectexpenseclaims_ibfk_2` FOREIGN KEY (`ProjectID`) REFERENCES `EmployeeProjects` (`ProjectID`),
  CONSTRAINT `projectexpenseclaims_ibfk_3` FOREIGN KEY (`CurrencyID`) REFERENCES `Currency` (`CurrencyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProjectExpenseClaims`
--

LOCK TABLES `ProjectExpenseClaims` WRITE;
/*!40000 ALTER TABLE `ProjectExpenseClaims` DISABLE KEYS */;
INSERT INTO `ProjectExpenseClaims` VALUES (11147,10001,10011,'SGD','2023-04-29 08:30:00',100.50,'Banking tech',_binary '\0','','Pending','2023-04-30 10:00:00'),(11148,10002,10015,'IDR','2023-04-28 10:00:00',250.75,'Operations',_binary '\0','','Approved','2023-04-30 11:30:00'),(11149,10003,10014,'JPY','2023-04-27 13:45:00',500.00,'Banking operations',_binary '\0','','Rejected','2023-04-30 12:15:00'),(11150,10004,10018,'SGD','2023-04-26 15:30:00',175.25,'Banking tech',_binary '','105','Pending','2023-04-30 13:00:00'),(11151,10005,10020,'KRW','2023-04-25 17:15:00',350.00,'Banking operations',_binary '\0','','Pending','2023-04-30 14:30:00'),(11152,10006,10012,'IDR','2023-04-24 19:00:00',50.00,'Banking tech',_binary '\0','','Approved','2023-04-30 15:45:00'),(11156,10006,10018,'JPY','2023-04-29 09:12:00',5000.00,'Banking software upgrade',_binary '\0','','Approved','2023-04-30 13:28:00'),(11157,10007,10020,'IDR','2023-04-28 11:30:00',1000000.00,'Operations software license fee',_binary '\0','','Pending','2023-04-30 13:30:00'),(11158,10002,10016,'SGD','2023-04-27 15:45:00',250.00,'Banking conference registration fee',_binary '','104','Pending','2023-04-30 13:32:00'),(11159,10008,10010,'INR','2023-04-26 10:20:00',7500.00,'Operations training program fee',_binary '\0','','Approved','2023-04-30 13:34:00'),(11160,10009,10019,'KHR','2023-04-25 14:00:00',150.00,'Banking seminar fee',_binary '\0','','Rejected','2023-04-30 13:36:00'),(11161,10003,10015,'HKD','2023-04-24 12:30:00',2000.00,'Operations software upgrade',_binary '\0','','Pending','2023-04-30 13:38:00'),(11164,10004,10011,'SGD','2023-04-29 10:00:00',25.00,'IT support',_binary '\0','','Pending','2023-04-29 10:30:00'),(11165,10005,10012,'IDR','2023-04-28 14:30:00',2000000.00,'Hardware purchase',_binary '','105','Approved','2023-04-29 09:30:00'),(11166,10002,10011,'KRW','2023-04-28 16:45:00',15000.00,'Printing materials',_binary '\0','','Rejected','2023-04-29 11:00:00'),(11167,10007,10012,'VND','2023-04-27 13:15:00',750000.00,'Data entry software',_binary '\0','','Pending','2023-04-29 08:45:00'),(11168,10006,10016,'CNY','2023-04-26 11:30:00',500.00,'Office supplies',_binary '\0','','Approved','2023-04-29 10:15:00'),(11169,10010,10019,'TWD','2023-04-25 09:45:00',8000.00,'Telecommunications',_binary '\0','','Pending','2023-04-29 09:00:00'),(11170,10009,10019,'SGD','2023-04-27 10:12:45',232.50,'IT infrastructure upgrade',_binary '\0','105','Pending','2023-04-29 13:45:00'),(11171,10001,10016,'JPY','2023-04-28 08:30:15',15900.00,'Bank reconciliation software',_binary '\0','','Pending','2023-04-29 14:25:00'),(11172,10010,10010,'INR','2023-04-28 16:45:30',4500.00,'Teleconferencing equipment',_binary '\0','','Pending','2023-04-29 15:10:00'),(11173,10008,10012,'IDR','2023-04-29 09:15:00',2100000.00,'Core banking system upgrade',_binary '\0','','Pending','2023-04-30 09:20:00'),(11174,10005,10013,'TWD','2023-04-29 11:30:45',20000.00,'Mobile banking app development',_binary '\0','','Pending','2023-04-30 11:45:00'),(11175,10002,10010,'SGD','2023-04-29 13:20:00',750.00,'Travel expenses for IT training',_binary '\0','','Pending','2023-04-30 14:30:00'),(11176,10006,10018,'CNY','2023-04-30 08:45:00',8000.00,'Cloud storage subscription',_binary '\0','','Pending','2023-04-30 09:15:00'),(11177,10003,10015,'HKD','2023-04-30 11:30:00',5500.00,'Hardware maintenance contract renewal',_binary '\0','','Pending','2023-04-30 12:00:00'),(11178,10007,10011,'KHR','2023-04-30 14:15:30',600000.00,'Server upgrade',_binary '\0','','Pending','2023-04-30 14:45:00'),(11179,10004,10020,'VND','2023-04-30 16:00:00',1800000.00,'Data analytics software license',_binary '\0','','Pending','2023-04-30 16:00:00'),(11210,10007,10020,'SGD','2023-04-27 09:30:00',15.50,'IT Equipment Purchase',_binary '\0','','Approved','2023-04-28 10:15:00'),(11211,10005,10011,'KRW','2023-04-28 14:20:00',200000.00,'Training Course Fees',_binary '\0','','Pending','2023-04-28 16:35:00'),(11212,10003,10016,'HKD','2023-04-29 08:45:00',2500.00,'Business Lunch Meeting',_binary '','103','Pending','2023-04-29 12:20:00'),(11213,10004,10012,'CNY','2023-04-29 15:00:00',500.00,'Stationery and Supplies',_binary '\0','','Rejected','2023-04-30 09:45:00'),(11214,10010,10014,'IDR','2023-04-29 10:00:00',75000.00,'Marketing Materials',_binary '\0','','Pending','2023-04-30 11:30:00'),(11215,10002,10020,'INR','2023-04-30 13:45:00',8000.00,'Team Building Event',_binary '\0','','Approved','2023-04-30 16:20:00'),(11216,10005,10011,'SGD','2023-04-29 08:30:00',56.72,'Banking Operations Training',_binary '','105','Pending','2023-04-29 14:30:00'),(11217,10008,10012,'JPY','2023-04-28 10:45:00',3480.00,'IT Infrastructure Upgrade',_binary '\0','','Approved','2023-04-29 09:20:00'),(11218,10001,10013,'IDR','2023-04-26 15:15:00',900000.00,'Marketing Campaign Expenses',_binary '\0','','Rejected','2023-04-27 11:30:00'),(11219,10003,10014,'HKD','2023-04-24 12:30:00',1200.50,'Office Supplies Purchase',_binary '\0','','Pending','2023-04-26 16:45:00'),(11220,10006,10015,'KHR','2023-04-23 11:00:00',150000.00,'Client Meeting Expenses',_binary '\0','','Approved','2023-04-25 14:15:00'),(11221,10007,10016,'INR','2023-04-22 14:45:00',3000.00,'Travel Expenses',_binary '\0','','Pending','2023-04-24 16:30:00'),(11222,10008,10014,'VND','2023-04-22 13:30:00',450000.00,'Banking equipment repair',_binary '\0','103','Rejected','2023-04-23 14:00:00'),(11223,10006,10019,'HKD','2023-04-27 09:00:00',800.00,'Banking operations training course',_binary '\0','','Pending','2023-04-27 16:30:00'),(11224,10005,10017,'CNY','2023-04-25 15:00:00',600.00,'Banking software maintenance',_binary '\0','','Approved','2023-04-26 10:15:00'),(11225,10007,10016,'IDR','2023-04-28 14:30:00',300.00,'Banking Tech',_binary '\0','','Pending','2023-04-28 18:45:00'),(11226,10003,10018,'JPY','2023-04-27 10:00:00',1500.00,'Operations',_binary '\0','','Approved','2023-04-27 14:15:00'),(11227,10010,10012,'KRW','2023-04-26 13:00:00',800.00,'Banking Operations',_binary '\0','','Rejected','2023-04-26 17:30:00'),(11228,10002,10011,'SGD','2023-04-25 09:30:00',75.00,'Banking Tech',_binary '\0','','Pending','2023-04-25 13:45:00'),(11229,10005,10017,'INR','2023-04-24 16:00:00',900.00,'Banking Operations',_binary '\0','','Pending','2023-04-24 20:15:00'),(11231,10005,10017,'INR','2023-04-24 17:00:00',100.00,'Banking Operations',_binary '\0','','Pending','2023-04-24 20:17:00'),(12230,10004,10013,'SGD','2023-04-29 08:00:00',250.00,'Banking Operations',_binary '\0','','Pending','2023-04-29 12:30:00');
/*!40000 ALTER TABLE `ProjectExpenseClaims` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-02  9:47:30
