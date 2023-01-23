-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Фев 20 2022 г., 16:58
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
(171, '2022-02-20 17:03:09', '2022-02-20 17:03:09', NULL, 'Глутамат - возбуждающий нейромедиатор в мозгу'),
(172, '2022-02-20 17:56:08', '2022-02-20 17:56:08', NULL, ''),
(173, '2022-02-20 17:56:56', '2022-02-20 17:56:56', NULL, 'sdassdasl'),
(174, '2022-02-20 18:05:23', '2022-02-20 18:05:23', NULL, 'Метохондрия\nВыделяет ATF, поглощает кислород, выделяет  угл. газ и воду'),
(175, '2022-02-20 18:11:04', '2022-02-20 18:11:04', NULL, 'Количество электронов равно количеству протонов'),
(176, '2022-02-20 18:12:00', '2022-02-20 18:12:00', NULL, 'Латеральное торможение - клетка тормозит расположенные рядом нейроны'),
(177, '2022-02-20 18:16:47', '2022-02-20 18:16:47', NULL, 'Парасимпатическая система - когда тело отдыхает (Выделяется ацетилхолин холин)\nСимпатическая система - бей или беги (нейромедиатор норэпинефрин)'),
(178, '2022-02-20 18:24:49', '2022-02-20 18:24:49', NULL, 'Domain: renault-test.lifestyle.uz\n| Ip: 205.251.155.226 (n)\n| HasCgi: y\n| UserName: renaulttestlifes\n| PassWord: N^Hjaz=8FBAO'),
(179, '2022-02-20 18:29:20', '2022-02-20 18:29:20', NULL, '12345789');

-- --------------------------------------------------------

--
-- Структура таблицы `ids_cells_tags`
--

CREATE TABLE `ids_cells_tags` (
  `cell_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `ids_cells_tags`
--

INSERT INTO `ids_cells_tags` (`cell_id`, `tag_id`) VALUES
(170, 164),
(170, 165),
(171, 166),
(171, 167),
(173, 166),
(174, 167),
(174, 166),
(175, 168),
(176, 169),
(176, 166),
(176, 168),
(177, 170),
(177, 166),
(178, 171),
(179, 172);

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
(166, '2022-02-20 17:03:09', 'Биология'),
(167, '2022-02-20 17:03:10', 'клетка'),
(168, '2022-02-20 18:11:04', 'наука'),
(169, '2022-02-20 18:12:00', 'нейроны'),
(170, '2022-02-20 18:16:47', 'мозг'),
(171, '2022-02-20 18:24:49', 'Доступы'),
(172, '2022-02-20 18:29:20', 'тест');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=180;

--
-- AUTO_INCREMENT для таблицы `tags`
--
ALTER TABLE `tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=173;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
