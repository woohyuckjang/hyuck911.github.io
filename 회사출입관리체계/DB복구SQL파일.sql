-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.4.24-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- phpdb 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `phpdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `phpdb`;

-- 테이블 phpdb.empid 구조 내보내기
CREATE TABLE IF NOT EXISTS `empid` (
  `num` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `birth` varchar(20) DEFAULT NULL,
  `tel` varchar(20) DEFAULT NULL,
  `regtime` varchar(20) DEFAULT NULL,
  `sign` varchar(50) DEFAULT '대기',
  PRIMARY KEY (`num`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 phpdb.guestid 구조 내보내기
CREATE TABLE IF NOT EXISTS `guestid` (
  `num` int(11) NOT NULL AUTO_INCREMENT,
  `g_name` varchar(20) DEFAULT NULL,
  `g_birth` varchar(20) DEFAULT NULL,
  `g_tel` varchar(20) DEFAULT NULL,
  `regtime` varchar(20) DEFAULT NULL,
  `g_sign` varchar(50) DEFAULT '대기',
  PRIMARY KEY (`num`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 phpdb.memberlog 구조 내보내기
CREATE TABLE IF NOT EXISTS `memberlog` (
  `id` varchar(20) NOT NULL,
  `pw` varchar(20) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `code` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 phpdb.signin_emp 구조 내보내기
CREATE TABLE IF NOT EXISTS `signin_emp` (
  `name` varchar(20) DEFAULT NULL,
  `birth` varchar(20) DEFAULT NULL,
  `tel` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 phpdb.signin_guest 구조 내보내기
CREATE TABLE IF NOT EXISTS `signin_guest` (
  `g_name` varchar(20) DEFAULT NULL,
  `g_birth` varchar(20) DEFAULT NULL,
  `g_tel` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 내보낼 데이터가 선택되어 있지 않습니다.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
