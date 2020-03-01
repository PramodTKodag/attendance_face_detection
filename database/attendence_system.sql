-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 27, 2019 at 09:25 AM
-- Server version: 5.7.25
-- PHP Version: 5.6.40-6+ubuntu18.04.1+deb.sury.org+3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `attendence_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `sr_no` int(10) NOT NULL,
  `Name` varchar(200) NOT NULL,
  `USER_ID` int(11) NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `LATE_STATUS` int(11) NOT NULL,
  `date_today` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`sr_no`, `Name`, `USER_ID`, `datetime`, `LATE_STATUS`, `date_today`) VALUES
(1, 'pramod', 1, '2019-06-16 19:21:46', 0, '2019-06-17'),
(2, 'gayatri', 0, '2019-06-16 19:30:09', 0, '2019-06-17'),
(3, 'pramod', 1, '2019-08-26 12:07:20', 0, '2019-07-21'),
(4, 'gayatri', 0, '2019-08-01 19:09:56', 0, '2019-08-02'),
(5, 'gayatri', 2, '2019-09-08 18:22:21', 1, '2019-09-08'),
(18, 'pramod', 1, '2019-08-25 18:15:21', 1, '2019-08-25'),
(19, 'pramod', 1, '2019-08-25 19:06:47', 1, '2019-08-26'),
(20, 'pramod', 1, '2019-09-08 14:20:23', 1, '2019-09-08'),
(21, 'pramod', 1, '2019-09-08 19:48:09', 0, '2019-09-09'),
(22, 'pramod', 1, '2019-09-14 04:06:11', 0, '2019-09-14');

-- --------------------------------------------------------

--
-- Table structure for table `error_db`
--

CREATE TABLE `error_db` (
  `ID` int(11) NOT NULL,
  `FILE_NAME` varchar(400) NOT NULL,
  `LINE_NO` int(11) NOT NULL,
  `ERROR_MESSAGE` varchar(400) NOT NULL,
  `ERROR_DESCRIPTION` varchar(1000) NOT NULL,
  `ERROR_TYPE` varchar(100) NOT NULL,
  `CREATED_BY` int(11) NOT NULL,
  `CREATED_AT` datetime NOT NULL,
  `MODIFIED_BY` int(11) NOT NULL,
  `MODIFIED_AT` datetime NOT NULL,
  `MODIFIED_COUNT` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `office_timing`
--

CREATE TABLE `office_timing` (
  `ID` int(11) NOT NULL,
  `OFFICE_START_TIME` varchar(200) NOT NULL,
  `OFFICE_END_TIME` varchar(200) NOT NULL,
  `LATE_TIME` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `office_timing`
--

INSERT INTO `office_timing` (`ID`, `OFFICE_START_TIME`, `OFFICE_END_TIME`, `LATE_TIME`) VALUES
(1, '10:00 AM', '6:00 PM', '11:30:00');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `ID` int(11) NOT NULL,
  `USERNAME` varchar(200) NOT NULL DEFAULT '0',
  `FIRST_NAME` varchar(200) NOT NULL DEFAULT '0',
  `LAST_NAME` varchar(200) NOT NULL DEFAULT '0',
  `SHIFT` tinyint(4) NOT NULL DEFAULT '0',
  `MOBILE` varchar(20) NOT NULL DEFAULT '0',
  `EMAIL` varchar(100) NOT NULL DEFAULT '0',
  `ADDRESS` text NOT NULL,
  `SALARY` int(11) NOT NULL DEFAULT '0',
  `ADD_DATETIME` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`ID`, `USERNAME`, `FIRST_NAME`, `LAST_NAME`, `SHIFT`, `MOBILE`, `EMAIL`, `ADDRESS`, `SALARY`, `ADD_DATETIME`) VALUES
(1, 'pramod', 'Pramod', 'Kodag', 1, '9594262896', 'kodagpramod74@gmail.com', '795 Folsom Ave, Suite 600 San Francisco, CA 94107 Phone: (804) 123-5432', 20000, '2019-08-03 00:00:00'),
(2, 'BALAV', 'BALA', 'GANESHAN', 0, '1234567890', 'BALA@GMAIL.COM', '', 10000, '2019-08-03 00:00:00'),
(7, 'DJ3', 'DJ3', 'DJJ', 1, '9594262896', 'dj@gmail.com', 'sss', 10000, '2019-08-25 15:25:48');

-- --------------------------------------------------------

--
-- Table structure for table `user_login`
--

CREATE TABLE `user_login` (
  `ID` int(11) NOT NULL,
  `USERNAME` varchar(100) NOT NULL,
  `NAME` varchar(200) NOT NULL,
  `EMAIL` varchar(200) NOT NULL,
  `PASSWORD` varchar(100) NOT NULL,
  `AVATAR` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_login`
--

INSERT INTO `user_login` (`ID`, `USERNAME`, `NAME`, `EMAIL`, `PASSWORD`, `AVATAR`) VALUES
(1, 'admin', 'Admin', 'admin@gmail.com', 'cd73502828457d15655bbd7a63fb0bc8', 'assets/profile_image/admin.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`sr_no`);

--
-- Indexes for table `error_db`
--
ALTER TABLE `error_db`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `office_timing`
--
ALTER TABLE `office_timing`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `user_details`
--
ALTER TABLE `user_details`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `user_login`
--
ALTER TABLE `user_login`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `sr_no` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
--
-- AUTO_INCREMENT for table `error_db`
--
ALTER TABLE `error_db`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `office_timing`
--
ALTER TABLE `office_timing`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `user_details`
--
ALTER TABLE `user_details`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `user_login`
--
ALTER TABLE `user_login`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
