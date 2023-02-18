-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 12, 2023 at 07:02 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `news`
--

-- --------------------------------------------------------

--
-- Table structure for table `articles`
--

CREATE TABLE `articles` (
  `id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `body` varchar(300) NOT NULL,
  `published_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` tinyint(1) NOT NULL,
  `is_delete` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `articles`
--

INSERT INTO `articles` (`id`, `author_id`, `category_id`, `title`, `body`, `published_date`, `updated_date`, `status`, `is_delete`) VALUES
(1, 1, 1, 'Alan walker', ' the greatest risk of all time', '2023-02-12 13:23:18', '2023-02-12 13:23:18', 1, 0),
(2, 1, 5, 'Alan walker', ' the greatest risk of all time', '2023-02-12 13:24:26', '2023-02-12 13:24:26', 1, 0),
(3, 1, 5, 'Alan walker', ' the greatest risk of all time', '2023-02-12 13:25:32', '2023-02-12 13:25:32', 1, 0),
(4, 1, 5, 'Alan walker', ' the greatest risk of all time', '2023-02-12 13:38:40', '2023-02-12 13:38:40', 1, 0),
(5, 1, 5, 'Alan walker', ' the greatest risk of all time', '2023-02-12 13:48:27', '2023-02-12 13:48:27', 1, 0),
(6, 1, 5, 'Alan wfsdfalker', ' the greatest risk of all time', '2023-02-12 13:49:37', '2023-02-12 13:49:37', 1, 0),
(7, 20, 5, 'Alan wfsdfalker', ' the greatest risk of all time', '2023-02-12 13:55:53', '2023-02-12 13:55:53', 1, 0),
(8, 2, 5, 'Alan wfsdfalker', ' the greatest risk of all time', '2023-02-12 13:56:08', '2023-02-12 13:56:08', 1, 0),
(9, 3, 5, 'Alan wfsdfalker', ' the greatest risk of all time', '2023-02-12 13:56:27', '2023-02-12 13:56:27', 1, 0),
(10, 3, 5, 'Alan wfsdfalker', ' the greatest risk of all time', '2023-02-12 14:05:49', '2023-02-12 14:05:49', 1, 0),
(11, 1000, 5, 'Alan wfsdfalker', ' the greatest risk of all time', '2023-02-12 14:05:56', '2023-02-12 14:05:56', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `is_delete` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `name`, `created_at`, `updated_at`, `is_delete`) VALUES
(1, 'Technology', '2023-02-12 12:22:52', '2023-02-12 12:22:52', 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(300) NOT NULL,
  `password` varchar(200) NOT NULL,
  `role` varchar(200) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `is_delete` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `role`, `created_at`, `updated_at`, `is_delete`) VALUES
(1, 'ruth', 'ruthruthsan@gmail.com', 'ruthsan234', 'ADMIN', '2023-02-12 11:08:50', '2023-02-12 11:08:50', 0),
(3, 'ruth', 'ruthrusthsan@gmail.com', 'ruthsan234', 'ADMIN', '2023-02-12 11:10:38', '2023-02-12 11:10:38', 0),
(4, 'ruth', 'ruthrusathsan@gmail.com', 'ruthsan234', 'ADMIN', '2023-02-12 11:13:57', '2023-02-12 11:13:57', 0),
(5, 'ruth', 'ruthrusathssan@gmail.com', 'ruthsan234', 'ADMIN', '2023-02-12 11:15:58', '2023-02-12 11:15:58', 1),
(7, 'ruth', 'ruthrusathsdsdssan@gmail.com', 'ruthsan234', 'ADMIN', '2023-02-12 11:17:00', '2023-02-12 11:17:00', 1),
(8, 'ruth', 'ruthrusatsdssan@gmail.com', 'ruthsan234', 'ADMIN', '2023-02-12 11:19:06', '2023-02-12 11:19:06', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `articles`
--
ALTER TABLE `articles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
