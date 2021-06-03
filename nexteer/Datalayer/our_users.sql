-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 03, 2021 at 11:51 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `our_users`
--

-- --------------------------------------------------------

--
-- Table structure for table `change_his`
--

CREATE TABLE `change_his` (
  `id` int(30) NOT NULL,
  `id_user` int(30) NOT NULL,
  `line` text NOT NULL,
  `old_ref_id` int(30) NOT NULL,
  `new_ref_id` int(30) NOT NULL,
  `date_changed` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `current_reff`
--

CREATE TABLE `current_reff` (
  `id` int(30) NOT NULL,
  `id_user` int(30) NOT NULL,
  `id_ref` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `eps_reff`
--

CREATE TABLE `eps_reff` (
  `id_eps_ref` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `eps_reff`
--

INSERT INTO `eps_reff` (`id_eps_ref`) VALUES
(38213710),
(38216130),
(38219816),
(38226329),
(38226332),
(38231410),
(38236683),
(38236684),
(38245523),
(38245524),
(38245525),
(38245526),
(38245533),
(38245534),
(38260746),
(38268195),
(38268196),
(38272195),
(38272202),
(38272203);

-- --------------------------------------------------------

--
-- Table structure for table `half_shift_ref`
--

CREATE TABLE `half_shift_ref` (
  `id_hs_ref` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `half_shift_ref`
--

INSERT INTO `half_shift_ref` (`id_hs_ref`) VALUES
(38241869),
(38241870),
(38246448),
(38246449),
(38246450),
(38246451),
(38246452),
(38246453),
(38246454),
(38246455),
(38255093),
(38255119),
(38260764),
(38261338),
(38261920),
(38261921),
(38264272),
(38266115),
(38266116),
(38266118),
(38266119),
(38266686),
(38273214),
(38273215),
(38273265),
(38273266),
(38273274),
(38277730),
(38278467),
(38278468),
(38286333),
(38286334),
(38288991),
(38292230),
(38292231),
(38292234);

-- --------------------------------------------------------

--
-- Table structure for table `logistic`
--

CREATE TABLE `logistic` (
  `id_logistic` int(30) NOT NULL,
  `name` text NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `logistic`
--

INSERT INTO `logistic` (`id_logistic`, `name`, `password`) VALUES
(1, 'Nabila Elkadiry', 'logistic');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id_user` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `password` varchar(30) NOT NULL,
  `line` int(11) NOT NULL,
  `zone` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id_user`, `name`, `password`, `line`, `zone`) VALUES
(1, 'Salaheddine Idrissi', 'salaheddine idrissi', 1, 'Machining'),
(2, 'Omar Chfik', 'omar chfik', 1, 'Assist MEC'),
(3, 'El Bassli Brahim', 'el bassli brahim', 2, 'FASS'),
(4, 'Houbari Youssef', 'houbari youssef', 2, 'HOT ZONE');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `change_his`
--
ALTER TABLE `change_his`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `current_reff`
--
ALTER TABLE `current_reff`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `eps_reff`
--
ALTER TABLE `eps_reff`
  ADD PRIMARY KEY (`id_eps_ref`);

--
-- Indexes for table `half_shift_ref`
--
ALTER TABLE `half_shift_ref`
  ADD PRIMARY KEY (`id_hs_ref`);

--
-- Indexes for table `logistic`
--
ALTER TABLE `logistic`
  ADD PRIMARY KEY (`id_logistic`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `change_his`
--
ALTER TABLE `change_his`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT for table `current_reff`
--
ALTER TABLE `current_reff`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=247;

--
-- AUTO_INCREMENT for table `eps_reff`
--
ALTER TABLE `eps_reff`
  MODIFY `id_eps_ref` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38272204;

--
-- AUTO_INCREMENT for table `half_shift_ref`
--
ALTER TABLE `half_shift_ref`
  MODIFY `id_hs_ref` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38292235;

--
-- AUTO_INCREMENT for table `logistic`
--
ALTER TABLE `logistic`
  MODIFY `id_logistic` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
