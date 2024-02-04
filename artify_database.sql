-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 04, 2024 at 12:29 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `artify_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `sector`
--

CREATE TABLE `sector` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `parentid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sector`
--

INSERT INTO `sector` (`id`, `name`, `parentid`) VALUES
(1, 'Manufacturing', NULL),
(2, 'Other', NULL),
(3, 'Service', NULL),
(4, 'Construction materials', 1),
(5, 'Electronics and Optics', 1),
(6, 'Food and Beverage', 1),
(7, 'Furniture', 1),
(8, 'Plastic and Rubber', 1),
(9, 'Creative industries', 2),
(10, 'Energy technology', 2),
(11, 'Environment', 2),
(12, 'Business services', 3),
(13, 'Engineering', 3),
(14, 'Information Technology and Telecommunications', 3),
(15, 'Tourism', 3),
(16, 'Translation services', 3),
(17, 'Transport and Logistics', 3),
(18, 'Bakery & confectionery products', 6),
(19, 'Beverages', 6),
(20, 'Fish & fish products', 6),
(21, 'Meat & meat products', 6),
(22, 'Milk & dairy products', 6),
(23, 'Other', 6),
(24, 'Sweets & snack food', 6),
(25, 'Bathroom', 7),
(26, 'Bedroom', 7),
(27, 'Kitchen', 7),
(28, 'Living room', 7),
(29, 'Office', 7),
(30, 'Other (Furniture)', 7),
(31, 'Outdoor', 7),
(32, 'Packaging', 8),
(33, 'Plastic processing technology', 8),
(34, 'Plastic profiles', 8),
(35, 'Data processing, Web portals, E-marketing', 14),
(36, 'Programming Consultancy', 14),
(37, 'Software, Hardware', 14),
(38, 'Air', 17),
(39, 'Rail', 17),
(40, 'Road', 17),
(41, 'Water', 17),
(42, 'Blowing', 33),
(43, 'Moulding', 33),
(44, 'Plastics welding and processing', 33);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `UserID` int(11) NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `AgreeToTerms` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UserID`, `Name`, `AgreeToTerms`) VALUES
(3, 'Kevin Rosenberg', 1);

-- --------------------------------------------------------

--
-- Table structure for table `usersector`
--

CREATE TABLE `usersector` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `sector_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usersector`
--

INSERT INTO `usersector` (`id`, `user_id`, `sector_id`) VALUES
(9, 3, 37);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sector`
--
ALTER TABLE `sector`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UserID`);

--
-- Indexes for table `usersector`
--
ALTER TABLE `usersector`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `sector_id` (`sector_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sector`
--
ALTER TABLE `sector`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `usersector`
--
ALTER TABLE `usersector`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `usersector`
--
ALTER TABLE `usersector`
  ADD CONSTRAINT `usersector_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`UserID`),
  ADD CONSTRAINT `usersector_ibfk_2` FOREIGN KEY (`sector_id`) REFERENCES `sector` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
