-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Фев 12 2022 г., 18:23
-- Версия сервера: 5.6.41
-- Версия PHP: 7.1.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
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
  `date_time_edit` datetime NOT NULL,
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
(56, '2022-02-12 17:40:33', '0000-00-00 00:00:00', '', '222', '[{\"key\":\"\",\"value\":\"kok\"}]');

-- --------------------------------------------------------

--
-- Структура таблицы `tags`
--

CREATE TABLE `tags` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT для таблицы `tags`
--
ALTER TABLE `tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
