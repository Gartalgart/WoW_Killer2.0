-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: mariadb
-- Generation Time: Feb 11, 2026 at 08:26 PM
-- Server version: 11.8.5-MariaDB-ubu2404
-- PHP Version: 8.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `BDD`
--

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `ID_CLASS` int(11) NOT NULL,
  `CLASS_NAME` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`ID_CLASS`, `CLASS_NAME`) VALUES
(1, 'chevalier'),
(2, 'mage'),
(3, 'berserker'),
(4, 'archer'),
(5, 'voleur');

-- --------------------------------------------------------

--
-- Table structure for table `hero`
--

CREATE TABLE `hero` (
  `ID` int(11) NOT NULL,
  `CHARACTER_NAME` varchar(50) NOT NULL,
  `ID_RACE` int(11) NOT NULL,
  `ID_CLASS` int(11) NOT NULL,
  `USER_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `hero`
--

INSERT INTO `hero` (`ID`, `CHARACTER_NAME`, `ID_RACE`, `ID_CLASS`, `USER_ID`) VALUES
(1, 'Morice', 1, 1, 3),
(2, 'Roger', 4, 2, 4),
(3, 'Bernard', 2, 5, 4);

-- --------------------------------------------------------

--
-- Table structure for table `race`
--

CREATE TABLE `race` (
  `ID_RACE` int(11) NOT NULL,
  `RACE_NAME` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `race`
--

INSERT INTO `race` (`ID_RACE`, `RACE_NAME`) VALUES
(1, 'orc'),
(2, 'humain'),
(3, 'elfe'),
(4, 'nain'),
(5, 'gobelin');

-- --------------------------------------------------------

--
-- Table structure for table `user_account`
--

CREATE TABLE `user_account` (
  `ID` int(11) NOT NULL,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `PASSWORD` varchar(60) NOT NULL,
  `last_time_username_modified` date
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Dumping data for table `user_account`
--

INSERT INTO `user_account` (`ID`, `username`, `PASSWORD`) VALUES
(3, 'Metaloul', '$2b$12$2S4xdxIx4/SrHLIDmKWgKOgl/ov478kfv9MjW8bZ1NNxUlABsoql6'),
(4, 'Rémy', '$2b$12$6t.D8pVoho0lXcdxuOFfMusN/jSfwXMPl6HlpzAcb9oBXKXbeUYru');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`ID_CLASS`);



--
-- Indexes for table `hero`
--
ALTER TABLE `hero`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `HERO_ID_RACE_FK` (`ID_RACE`),
  ADD KEY `HERO_ID_CLASS_FK` (`ID_CLASS`);

--
-- Indexes for table `race`
--
ALTER TABLE `race`
  ADD PRIMARY KEY (`ID_RACE`);


--
-- Indexes for table `user_account`
--
ALTER TABLE `user_account`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `ID_CLASS` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `hero`
--
ALTER TABLE `hero`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `race`
--
ALTER TABLE `race`
  MODIFY `ID_RACE` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `service`
--
ALTER TABLE `service`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `user_account`
--
ALTER TABLE `user_account`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--


--
-- Constraints for table `hero`
--
ALTER TABLE `hero`
  ADD CONSTRAINT `HERO_ID_CLASS_FK` FOREIGN KEY (`ID_CLASS`) REFERENCES `class` (`ID_CLASS`),
  ADD CONSTRAINT `HERO_ID_RACE_FK` FOREIGN KEY (`ID_RACE`) REFERENCES `race` (`ID_RACE`);

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
