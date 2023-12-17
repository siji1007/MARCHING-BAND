-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.2.0 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for band
CREATE DATABASE IF NOT EXISTS `band` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `band`;

-- Dumping structure for table band.instruments
CREATE TABLE IF NOT EXISTS `instruments` (
  `MemberID` int NOT NULL,
  `Instrument` varchar(50) DEFAULT NULL,
  `BandPosition` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`MemberID`),
  CONSTRAINT `instruments_ibfk_1` FOREIGN KEY (`MemberID`) REFERENCES `members` (`MemberID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table band.instruments: ~50 rows (approximately)
INSERT INTO `instruments` (`MemberID`, `Instrument`, `BandPosition`) VALUES
	(1, 'Clarinet', 'Clarinet Member'),
	(2, 'Saxophone Soprano', 'Saxophone Soprano Member'),
	(3, 'Saxophone Soprano', 'Saxophone Soprano Lead'),
	(4, 'Baritone', 'Baritone Member'),
	(5, 'Piccolo', 'Piccolo Member'),
	(6, 'Bass Drum', 'Bass Drum Lead'),
	(7, 'Tuba', 'Tuba Lead'),
	(8, 'Trumpet', 'Trumpet Member'),
	(9, 'Bass Drum', 'Bass Drum Member'),
	(10, 'Quintom', 'Quintom Member'),
	(11, 'Bass Drum', 'Vice President'),
	(12, 'Saxophone Soprano', 'Saxophone Soprano Member'),
	(13, 'Flute', 'Flute Member'),
	(14, 'Quintom', 'Quintom Member'),
	(15, 'Cymbal', 'Cymbal Lead'),
	(16, 'Snare', 'Snare Member'),
	(17, 'Flute', 'Flute Member'),
	(18, 'Flute', 'Flute Member'),
	(19, 'Flute', 'Flute Member'),
	(20, 'French Horn', 'French Horn Member'),
	(21, 'Saxophone Soprano', 'Saxophone Soprano Member'),
	(22, 'Saxophone Soprano', 'Saxophone Soprano Member'),
	(23, 'Piccolo', 'Piccolo Member'),
	(24, 'Snare', 'Snare Member'),
	(25, 'Trumpet', 'Trumpet Lead'),
	(26, 'Piccolo', 'Piccolo Lead'),
	(27, 'Saxophone Soprano', 'Saxophone Soprano Member'),
	(28, 'Trumpet', 'Trumpet Member'),
	(29, 'Baritone', 'President'),
	(30, 'Bass Drum', 'Bass Drum Member'),
	(31, 'Saxophone Alto', 'Saxophone Alto Lead'),
	(32, 'Saxophone Soprano', 'Saxophone Soprano Member'),
	(33, 'Saxophone Soprano', 'Saxophone Soprano Member'),
	(34, 'French Horn', 'French Horn Lead'),
	(35, 'Bass Drum', 'Bass Drum Member'),
	(36, 'Trumpet', 'Trumpet Member'),
	(37, 'Flute', 'Flute Member'),
	(38, 'Snare', 'Snare Member'),
	(39, 'Clarinet', 'Clarinet Lead'),
	(40, 'Baritone', 'Baritone Member'),
	(41, 'Baritone', 'Baritone Member'),
	(42, 'Flute', 'Flute Member'),
	(43, 'French Horn', 'French Horn Member'),
	(44, 'Baritone', 'Baritone Lead'),
	(45, 'Snare', 'Snare Member'),
	(46, 'Snare', 'Snare Lead'),
	(47, 'Flute', 'Flute Lead'),
	(48, 'Snare', 'Snare Member'),
	(49, 'Quintom', 'Quintom Lead'),
	(50, 'Piccolo', 'Piccolo Member');

-- Dumping structure for table band.members
CREATE TABLE IF NOT EXISTS `members` (
  `MemberID` int NOT NULL,
  `MemberName` varchar(255) DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `UniformSize` varchar(20) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`MemberID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table band.members: ~50 rows (approximately)
INSERT INTO `members` (`MemberID`, `MemberName`, `Age`, `Gender`, `Department`, `UniformSize`, `Address`) VALUES
	(1, 'Patricia Ann Manalili', 21, 'Female', 'CBPA', 'extra large', 'Basud'),
	(2, 'Patrick Luis Morales', 20, 'Male', 'CBPA', 'small', 'Labo'),
	(3, 'Rafael Angelo Tan', 22, 'Male', 'COED', 'medium', 'Labo'),
	(4, 'Ella Marie Serrano', 18, 'Female', 'COED', 'medium', 'Paracale'),
	(5, 'Clarissa Mae Dizon', 22, 'Female', 'CBPA', 'extra large', 'Paracale'),
	(6, 'Marianne Grace Flores', 19, 'Female', 'ICS', 'large', 'Panganiban'),
	(7, 'Denise Nicole Ramos', 24, 'Female', 'COENG', 'large', 'Talisay'),
	(8, 'Jaime Rafael Dimaano', 23, 'Male', 'CAS', 'large', 'Labo'),
	(9, 'Isabella Sophia Tan', 24, 'Female', 'ICS', 'small', 'Mercedes'),
	(10, 'Alejandro Cruzat', 22, 'Male', 'COED', 'small', 'Labo'),
	(11, 'Juan Paolo Santos', 24, 'Male', 'COENG', 'extra large', 'Mercedes'),
	(12, 'Adrian Joseph Uy', 19, 'Male', 'CAS', 'large', 'Mercedes'),
	(13, 'Bianca Marie Lim', 20, 'Female', 'CBPA', 'extra large', 'Panganiban'),
	(14, 'Cassandra Anne Hernandez', 18, 'Female', 'COENG', 'large', 'Paracale'),
	(15, 'Jericho Paolo Magno', 20, 'Male', 'COED', 'extra large', 'Vinzons'),
	(16, 'Stephanie Joyce Villanueva', 19, 'Female', 'ICS', 'medium', 'Panganiban'),
	(17, 'Angelica Marie Gutierrez', 19, 'Female', 'COENG', 'medium', 'Paracale'),
	(18, 'Jonathan Daniel Enriquez', 24, 'Male', 'CAS', 'small', 'Basud'),
	(19, 'Carlos Antonio Rivera', 19, 'Male', 'CAS', 'medium', 'Basud'),
	(20, 'Adrian Gabriel Cruz', 19, 'Male', 'COENG', 'large', 'Labo'),
	(21, 'Carlo Angelo Cruz', 18, 'Male', 'COED', 'medium', 'Vinzons'),
	(22, 'Trisha Mae Magbanua', 20, 'Female', 'COED', 'large', 'Paracale'),
	(23, 'Samantha Louise Del Rosario', 24, 'Female', 'COENG', 'extra large', 'Mercedes'),
	(24, 'Paolo Andrei Cordero', 20, 'Male', 'COENG', 'extra large', 'Labo'),
	(25, 'Enrique Andres Cortez', 23, 'Male', 'COED', 'extra large', 'Talisay'),
	(26, 'Ysabel Grace Castillo', 20, 'Female', 'CBPA', 'large', 'Vinzons'),
	(27, 'Gabriel Angelo Sy', 22, 'Male', 'CBPA', 'medium', 'Basud'),
	(28, 'Danielle Beatriz Agustin', 19, 'Female', 'ICS', 'small', 'Mercedes'),
	(29, 'Maria Angelica Reyes', 21, 'Female', 'CBPA', 'extra large', 'Paracale'),
	(30, 'Natasha Denise Cabrera', 18, 'Female', 'COENG', 'medium', 'Panganiban'),
	(31, 'Krystel Anne Salazar', 18, 'Female', 'CAS', 'large', 'Paracale'),
	(32, 'Francis Xavier Ocampo', 22, 'Male', 'CBPA', 'medium', 'Mercedes'),
	(33, 'Camille Andrea Castro', 19, 'Female', 'COENG', 'small', 'Talisay'),
	(34, 'Sofia Isabel Gonzales', 22, 'Female', 'CBPA', 'medium', 'Paracale'),
	(35, 'Julius Caesar Alcaraz', 20, 'Male', 'CBPA', 'medium', 'Labo'),
	(36, 'Luis Miguel Santos', 23, 'Male', 'CBPA', 'extra large', 'Talisay'),
	(37, 'Danica Nicole Pascual', 24, 'Female', 'COED', 'medium', 'Daet'),
	(38, 'Joshua Matthew Espiritu', 24, 'Male', 'CAS', 'extra large', 'Labo'),
	(39, 'Katrina Joy Dimaculangan', 20, 'Female', 'COENG', 'small', 'Daet'),
	(40, 'Michael Vincent Galang', 22, 'Male', 'COENG', 'extra large', 'Talisay'),
	(41, 'Christopher Lloyd Ramos', 19, 'Male', 'COED', 'large', 'Daet'),
	(42, 'Lorenzo Miguel Velasco', 19, 'Male', 'COED', 'small', 'Daet'),
	(43, 'Martin Joseph Bautista', 20, 'Male', 'CAS', 'medium', 'Daet'),
	(44, 'Jose Miguel Alonzo', 22, 'Male', 'COENG', 'extra large', 'Panganiban'),
	(45, 'Maricar Isabel Reyes', 24, 'Female', 'CBPA', 'large', 'Panganiban'),
	(46, 'Giselle Anne Malabanan', 20, 'Female', 'CAS', 'large', 'Panganiban'),
	(47, 'Andrea Mae Dela Cruz', 23, 'Female', 'COED', 'medium', 'Paracale'),
	(48, 'Ferdinand Luis Lim', 19, 'Male', 'CBPA', 'extra large', 'Labo'),
	(49, 'Carla Jean Javier', 24, 'Female', 'CAS', 'small', 'Vinzons'),
	(50, 'Renato Miguel Paredes', 20, 'Male', 'COED', 'large', 'Basud');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
