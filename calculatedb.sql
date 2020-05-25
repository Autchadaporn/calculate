-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 25, 2020 at 09:08 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `calculatedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `gpa`
--

CREATE TABLE `gpa` (
  `Rows_id` int(11) NOT NULL,
  `Subject_ID` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `Name_TH` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `Unit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `gpa`
--

INSERT INTO `gpa` (`Rows_id`, `Subject_ID`, `Name_TH`, `Unit`) VALUES
(1, '225111', 'การเขียนโปรแกรมเชิงโครงสร้าง', 3),
(2, '225434', 'สถาปัตยกรรมคอมพิวเตอร์', 4),
(3, '225101', 'ตรรกะพื้นฐานและการแก้ปัญหา', 5),
(4, '241334', 'คณิตศาสตร์เต็มหน่วย', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gpa`
--
ALTER TABLE `gpa`
  ADD PRIMARY KEY (`Rows_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `gpa`
--
ALTER TABLE `gpa`
  MODIFY `Rows_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
