-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-05-2020 a las 01:46:55
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `appointmentapp`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appointments`
--

CREATE TABLE `appointments` (
  `id` int(11) NOT NULL,
  `firstName` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `lastName` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `ident` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `date` date NOT NULL,
  `city` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `neighborhood` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `mobile` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `dateAppointment` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `appointments`
--

INSERT INTO `appointments` (`id`, `firstName`, `lastName`, `ident`, `date`, `city`, `neighborhood`, `mobile`, `dateAppointment`) VALUES
(1, 'juan', 'campiño', '10461231123', '2020-05-05', 'medellin', 'bello', '311223323', '2020-05-16T02:05'),
(2, 'yohan', 'tobon', '3112321231', '2020-05-09', 'medellin', 'centro', '31112312312', '1111-02-02T02:02');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `appointments`
--
ALTER TABLE `appointments`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `appointments`
--
ALTER TABLE `appointments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
