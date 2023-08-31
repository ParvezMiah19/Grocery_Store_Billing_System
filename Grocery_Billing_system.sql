-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 17, 2022 at 04:15 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Grocery_Billing_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `Cosmetics_items`
--

CREATE TABLE `Cosmetics_items` (
  `Product_name` varchar(100) NOT NULL,
  `Price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Cosmetics_items`
--

INSERT INTO `Cosmetics_items` (`Product_name`, `Price`) VALUES
('Soap', 40),
('Face Cream', 300),
('Loation', 250),
('Hair Gel', 220),
('Hair Oil', 80),
('Shampoo', 400),
('Shaban', 80);

-- --------------------------------------------------------

--
-- Table structure for table `Dry_Food_Items`
--

CREATE TABLE `Dry_Food_Items` (
  `Product_Name` varchar(100) NOT NULL,
  `Price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Dry_Food_Items`
--

INSERT INTO `Dry_Food_Items` (`Product_Name`, `Price`) VALUES
('lays', 25),
('pringles', 180),
('kitkat', 30),
('weafers', 20),
('snikers', 50),
('Ferro Rochers', 300);

-- --------------------------------------------------------

--
-- Table structure for table `Grocery_items`
--

CREATE TABLE `Grocery_items` (
  `Product_Name` varchar(100) NOT NULL,
  `Price` int(11) NOT NULL COMMENT 'Per KG'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Grocery_items`
--

INSERT INTO `Grocery_items` (`Product_Name`, `Price`) VALUES
('Rice', 30),
('Chicken', 250),
('Beef', 550),
('onion', 50),
('Soyabean Oil', 280),
('Dal', 45);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
