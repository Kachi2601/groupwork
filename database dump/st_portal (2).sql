-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2022 at 10:11 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `st_portal`
--

-- --------------------------------------------------------

--
-- Table structure for table `air`
--

CREATE TABLE `air` (
  `Booking_number` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Route` varchar(255) NOT NULL,
  `Payment_Method` varchar(255) NOT NULL,
  `Booking_date` varchar(255) NOT NULL,
  `Item` varchar(255) NOT NULL,
  `Total( £)` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `bus`
--

CREATE TABLE `bus` (
  `Booking_number` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Route` varchar(255) NOT NULL,
  `Payment_Method` varchar(255) NOT NULL,
  `Booking_date` varchar(255) NOT NULL,
  `Item` varchar(255) NOT NULL,
  `Total( £)` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bus`
--

INSERT INTO `bus` (`Booking_number`, `Name`, `Email`, `Route`, `Payment_Method`, `Booking_date`, `Item`, `Total( £)`) VALUES
('7359', 'Onyekachi Amugo', 'onyekachi670@gmail.com', 'Bristol to Cardiff', 'PayPal', '21-04-2022', '', ''),
('6438', 'Omite Amugo', 'ejiyk16@yahoo.com', 'Bristol to Cardiff', 'Visa', '21-04-2022', '', ''),
('5548', 'Omite Amugo', 'ejiyk16@yahoo.com', 'Bristol to Cardiff', 'Visa', '21-04-2022', '', ''),
('8917', 'Kap PACK', 'onyekachi670@gmail.com', 'NewCastle to Cardiff', 'Master card', '21-04-2022', '', ''),
('6772', 'Kap PACK', 'onyekachi670@gmail.com', 'NewCastle to Cardiff', 'Master card', '21-04-2022', '', ''),
('5126', 'Kap PACK', 'onyekachi670@gmail.com', 'NewCastle to Cardiff', 'Master card', '21-04-2022', '', ''),
('1113', 'kmsks', 'onyekachi670@gmail.com', 'Cardiff to Newcastle', 'Master card', '21-04-2022', '', ''),
('7327', 'Onyekachi Amugo', 'ejiyk16@yahoo.com', 'Bristol to London', 'PayPal', '21-04-2022', '3', ''),
('9593', 'w', 'onyekacwe670@gmail.com', 'Bristol to Newcastle', 'Visa', '21-04-2022', '3', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
