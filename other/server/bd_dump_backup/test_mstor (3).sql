-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Мар 23 2022 г., 09:04
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
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `cells`
--

INSERT INTO `cells` (`id`, `date_time`, `date_time_edit`, `title`, `description`) VALUES
(326, '2022-03-23 00:54:45', '2022-03-23 00:54:45', NULL, 'Метохондрия\nВыделяет ATF, поглощает кислород, выделяет  угл. газ и воду'),
(327, '2022-03-23 00:55:09', '2022-03-23 00:55:09', NULL, 'Количество электронов равно количеству протонов'),
(328, '2022-03-23 00:55:33', '2022-03-23 00:55:33', NULL, 'Глутамат - возбуждающий нейромедиатор в мозгу'),
(329, '2022-03-23 00:56:06', '2022-03-23 00:56:06', NULL, 'Латеральное торможение - клетка тормозит расположенные рядом нейроны'),
(331, '2022-03-23 00:59:41', '2022-03-23 00:59:41', NULL, 'Mayukai Theme');

-- --------------------------------------------------------

--
-- Структура таблицы `ids_cells_tags`
--

CREATE TABLE `ids_cells_tags` (
  `id` int(11) NOT NULL,
  `cell_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `ids_cells_tags`
--

INSERT INTO `ids_cells_tags` (`id`, `cell_id`, `tag_id`) VALUES
(114, 326, 207),
(115, 326, 208),
(116, 327, 209),
(117, 327, 210),
(118, 328, 207),
(119, 328, 211),
(120, 329, 211),
(121, 329, 208),
(124, 331, 214),
(125, 331, 215);

-- --------------------------------------------------------

--
-- Структура таблицы `tags`
--

CREATE TABLE `tags` (
  `id` int(11) NOT NULL,
  `date_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `tags`
--

INSERT INTO `tags` (`id`, `date_time`, `name`) VALUES
(207, '2022-03-23 00:54:45', 'Биология'),
(208, '2022-03-23 00:54:45', 'Клетка'),
(209, '2022-03-23 00:55:09', 'Физика'),
(210, '2022-03-23 00:55:10', 'Наука'),
(211, '2022-03-23 00:55:33', 'Мозг'),
(214, '2022-03-23 00:59:41', 'VSCODE'),
(215, '2022-03-23 00:59:41', 'Темы');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `cells`
--
ALTER TABLE `cells`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `ids_cells_tags`
--
ALTER TABLE `ids_cells_tags`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=346;

--
-- AUTO_INCREMENT для таблицы `ids_cells_tags`
--
ALTER TABLE `ids_cells_tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=151;

--
-- AUTO_INCREMENT для таблицы `tags`
--
ALTER TABLE `tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=237;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
