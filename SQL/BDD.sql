-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: mariadb
-- Generation Time: Feb 11, 2026 at 08:26 PM
-- Server version: 11.8.5-MariaDB-ubu2404
-- PHP Version: 8.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
SET NAMES utf8mb4;

-- Désactivation temporaire pour accélérer les insertions
SET FOREIGN_KEY_CHECKS = 0;
SET UNIQUE_CHECKS = 0;
SET AUTOCOMMIT = 0;

START TRANSACTION;

-- --------------------------------------------------------
-- Table `class`
-- --------------------------------------------------------

CREATE TABLE `class` (
  `ID_CLASS` int(11) NOT NULL AUTO_INCREMENT,
  `CLASS_NAME` varchar(50) NOT NULL,
  PRIMARY KEY (`ID_CLASS`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `class` (`ID_CLASS`, `CLASS_NAME`) VALUES
  (1, 'chevalier'),
  (2, 'mage'),
  (3, 'berserker'),
  (4, 'archer'),
  (5, 'voleur');

-- --------------------------------------------------------
-- Table `race`
-- --------------------------------------------------------

CREATE TABLE `race` (
  `ID_RACE` int(11) NOT NULL AUTO_INCREMENT,
  `RACE_NAME` varchar(50) NOT NULL,
  PRIMARY KEY (`ID_RACE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `race` (`ID_RACE`, `RACE_NAME`) VALUES
  (1, 'orc'),
  (2, 'humain'),
  (3, 'elfe'),
  (4, 'nain'),
  (5, 'gobelin');

-- --------------------------------------------------------
-- Table `user_account`
-- --------------------------------------------------------

CREATE TABLE `user_account` (
  `ID`       int(11)      NOT NULL AUTO_INCREMENT,
  `username` varchar(50)  CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `PASSWORD` varchar(60)  NOT NULL,
  `last_time_username_modified` date DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `uq_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `user_account` (`ID`, `username`, `PASSWORD`) VALUES
  (3, 'Metaloul', '$2b$12$2S4xdxIx4/SrHLIDmKWgKOgl/ov478kfv9MjW8bZ1NNxUlABsoql6'),
  (4, 'Rémy',    '$2b$12$6t.D8pVoho0lXcdxuOFfMusN/jSfwXMPl6HlpzAcb9oBXKXbeUYru');

-- --------------------------------------------------------
-- Table `hero`  (après ses dépendances : class, race, user_account)
-- --------------------------------------------------------

CREATE TABLE `hero` (
  `ID`             int(11)     NOT NULL AUTO_INCREMENT,
  `CHARACTER_NAME` varchar(50) NOT NULL,
  `ID_RACE`        int(11)     NOT NULL,
  `ID_CLASS`       int(11)     NOT NULL,
  `USER_ID`        int(11)     NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `HERO_ID_RACE_FK`  (`ID_RACE`),
  KEY `HERO_ID_CLASS_FK` (`ID_CLASS`),
  CONSTRAINT `HERO_ID_CLASS_FK` FOREIGN KEY (`ID_CLASS`) REFERENCES `class` (`ID_CLASS`),
  CONSTRAINT `HERO_ID_RACE_FK`  FOREIGN KEY (`ID_RACE`)  REFERENCES `race`  (`ID_RACE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `hero` (`ID`, `CHARACTER_NAME`, `ID_RACE`, `ID_CLASS`, `USER_ID`) VALUES
  (1, 'Morice',  1, 1, 3),
  (2, 'Roger',   4, 2, 4),
  (3, 'Bernard', 2, 5, 4);

-- AUTO_INCREMENT finaux
ALTER TABLE `class`        MODIFY `ID_CLASS` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
ALTER TABLE `race`         MODIFY `ID_RACE`  int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
ALTER TABLE `hero`         MODIFY `ID`       int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
ALTER TABLE `user_account` MODIFY `ID`       int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

-- Réactivation
SET FOREIGN_KEY_CHECKS = 1;
SET UNIQUE_CHECKS = 1;

COMMIT;