-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Фев 17 2022 г., 22:18
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
  `title` text,
  `description` longtext NOT NULL,
  `tags_ids` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `cells`
--

INSERT INTO `cells` (`id`, `date_time`, `date_time_edit`, `title`, `description`, `tags_ids`) VALUES
(152, '2022-02-17 23:23:14', '2022-02-17 23:23:14', NULL, 'Метохондрия\nВыделяет ATF, поглощает кислород, выделяет  угл. газ и воду', '144,145'),
(153, '2022-02-17 23:23:32', '2022-02-17 23:23:32', NULL, 'Глутамат - возбуждающий нейромедиатор в мозгу', '146,144'),
(154, '2022-02-17 23:24:01', '2022-02-17 23:24:01', NULL, 'Латеральное торможение - клетка тормозит расположенные рядом нейроны', '147,144'),
(155, '2022-02-17 23:24:38', '2022-02-17 23:24:38', NULL, 'Количество электронов равно количеству протонов', '148,149'),
(156, '2022-02-17 23:25:10', '2022-02-17 23:25:10', NULL, 'Что то такое для теста', '149,145'),
(157, '2022-02-17 23:25:25', '2022-02-17 23:25:25', NULL, 'Тестируем очередной раз', '150'),
(158, '2022-02-17 23:52:20', '2022-02-17 23:52:20', NULL, 'sada', ','),
(159, '2022-02-17 23:53:43', '2022-02-17 23:53:43', NULL, 'sada', '151,152'),
(160, '2022-02-17 23:54:12', '2022-02-17 23:54:12', NULL, 'sdas', ','),
(161, '2022-02-17 23:54:15', '2022-02-17 23:54:15', NULL, 'sdas', '153,154'),
(162, '2022-02-18 00:16:47', '2022-02-18 00:16:47', NULL, 'ыфвф', ',,');

-- --------------------------------------------------------

--
-- Структура таблицы `tags`
--

CREATE TABLE `tags` (
  `id` int(11) NOT NULL,
  `date_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` text NOT NULL,
  `cells_ids` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `tags`
--

INSERT INTO `tags` (`id`, `date_time`, `name`, `cells_ids`) VALUES
(144, '2022-02-17 23:23:14', 'Биология', '1,2'),
(145, '2022-02-17 23:23:14', 'клетка', '1'),
(146, '2022-02-17 23:23:32', 'гормон', '3,2'),
(147, '2022-02-17 23:24:01', 'мозг', '2,4'),
(148, '2022-02-17 23:24:38', 'наука', NULL),
(149, '2022-02-17 23:24:38', 'атомы', NULL),
(150, '2022-02-17 23:25:25', 'жесть', NULL),
(151, '2022-02-17 23:52:20', '1313', NULL),
(152, '2022-02-17 23:52:20', 'sda', NULL),
(153, '2022-02-17 23:54:12', 'sdas', NULL),
(154, '2022-02-17 23:54:12', 'asdcq', NULL),
(155, '2022-02-18 00:16:47', 'ыфв', NULL),
(156, '2022-02-18 00:16:47', 'ф', NULL),
(157, '2022-02-18 00:16:47', '11', NULL);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=163;

--
-- AUTO_INCREMENT для таблицы `tags`
--
ALTER TABLE `tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=158;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
