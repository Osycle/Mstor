-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Фев 13 2022 г., 12:48
-- Версия сервера: 5.6.51
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `test_mstor`
--

-- --------------------------------------------------------

--
-- Структура таблицы `cells`
--

CREATE TABLE `cells` (
  `id` int(11) NOT NULL,
  `date_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date_time_edit` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `title` text NOT NULL,
  `description` text NOT NULL,
  `tags` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `cells`
--

INSERT INTO `cells` (`id`, `date_time`, `date_time_edit`, `title`, `description`, `tags`) VALUES
(13, '2022-02-09 12:25:56', '0000-00-00 00:00:00', '', 'Латеральное торможение - клетка тормозит расположенные рядом нейроны', ''),
(50, '2022-02-11 12:21:56', '0000-00-00 00:00:00', '', '', ''),
(51, '2022-02-11 16:10:05', '0000-00-00 00:00:00', '', '', ''),
(52, '2022-02-11 16:10:46', '0000-00-00 00:00:00', '', '', ''),
(53, '2022-02-12 17:14:31', '0000-00-00 00:00:00', '', 'dasdasd', '12'),
(54, '2022-02-12 17:34:09', '0000-00-00 00:00:00', '', '111', '120|13'),
(55, '2022-02-12 17:38:26', '0000-00-00 00:00:00', '', '111', 'Array'),
(56, '2022-02-12 17:40:33', '0000-00-00 00:00:00', '', '222', '[{\"key\":\"\",\"value\":\"kok\"}]'),
(57, '2022-02-13 02:35:25', '0000-00-00 00:00:00', '', '', ''),
(58, '2022-02-13 02:37:22', '2022-02-13 02:37:22', '', 'asdas', 'Array'),
(59, '2022-02-13 03:21:37', '2022-02-13 03:21:37', '', 'asdasdca asc as ac a', 'asda|asd|sad|asd xcs'),
(60, '2022-02-13 03:42:02', '2022-02-13 03:42:02', '', 'asd', 'Array'),
(61, '2022-02-13 03:43:35', '2022-02-13 03:43:35', '', 'asd', 'Array'),
(62, '2022-02-13 03:44:00', '2022-02-13 03:44:00', '', 'asd', 'Array'),
(63, '2022-02-13 03:45:48', '2022-02-13 03:45:48', '', 'asd', 'Array'),
(64, '2022-02-13 03:49:05', '2022-02-13 03:49:05', '', 'asd', 'Array'),
(65, '2022-02-13 03:50:30', '2022-02-13 03:50:30', '', 'asd', 'Array'),
(66, '2022-02-13 04:17:02', '2022-02-13 04:17:02', '', '11111', 'Array'),
(67, '2022-02-13 13:54:12', '2022-02-13 13:54:12', '', 'desclsl', 'Array|Array'),
(68, '2022-02-13 13:55:06', '2022-02-13 13:55:06', '', 'desclsl', 'Array|Array'),
(69, '2022-02-13 14:05:13', '2022-02-13 14:05:13', '', 'sadas', 'Array'),
(70, '2022-02-13 14:05:33', '2022-02-13 14:05:33', '', '2333333333333333333333', 'Array'),
(71, '2022-02-13 14:06:04', '2022-02-13 14:06:04', '', '23124', '57|58');

-- --------------------------------------------------------

--
-- Структура таблицы `tags`
--

CREATE TABLE `tags` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `tags`
--

INSERT INTO `tags` (`id`, `name`) VALUES
(47, 'vas fsadfasdasds'),
(48, 'wqeq'),
(49, 'asdas'),
(50, '000'),
(51, '999'),
(52, '111'),
(53, '2'),
(54, '11122'),
(55, '334'),
(56, '4356'),
(57, 'sdsa'),
(58, '34523');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `cells`
--
ALTER TABLE `cells`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `tags`
--
ALTER TABLE `tags`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `cells`
--
ALTER TABLE `cells`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- AUTO_INCREMENT для таблицы `tags`
--
ALTER TABLE `tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
