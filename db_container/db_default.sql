-- phpMyAdmin SQL Dump

CREATE DATABASE rating_database CHARACTER SET utf8 COLLATE utf8_general_ci;
USE rating_database;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+02:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

CREATE TABLE `ratings` (
  `ID` int(11) NOT NULL,
  `Name` text COLLATE utf8_bin NOT NULL,
  `Source` text COLLATE utf8_bin NOT NULL,
  `Rating` int(11) NOT NULL,
  `Comment` text COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

INSERT INTO `ratings` (`ID`, `Name`, `Source`, `Rating`, `Comment`) VALUES
(1, 'Half-Life', 'https://www.half-life.com/en/halflife', 4, 'One of the first FPS games I\'ve ever played.'),
(2, 'Half-Life 2', 'https://www.half-life.com/en/halflife2', 5, 'The game that made me enjoy half-life as series. The graphics stand the test of time and the addition of physics into gameplay makes it way more immersive.'),
(3, 'Warcraft 3', 'https://playwarcraft3.com/en-us/', 5, 'First game I\'ve ever played. Got me hooked into real-time strategy games and the whole Warcraft universe. Big fan to this day.'),
(4, 'World of Warcraft: Shadowlands', 'https://worldofwarcraft.com/en-us/', 4, 'A great MMO that I still play to this day. Current expansion has a great overhaul to levelling making it way more fun. New story content is also great, however, the endgame content feels a bit lackluster if playing solo.'),
(5, 'Mass Effect 2', 'https://www.ea.com/games/mass-effect/mass-effect-2', 5, 'One of the greatest single-player RPGs to date. Great replayability value and fun gameplay.'),
(6, 'The Elder Scrolls V: Skyrim', 'https://elderscrolls.bethesda.net/skyrim', 4, 'A great sandbox singleplayer RPG. Countless hours of fun gameplay and replayability and great mods. However, filled with many bugs and optimization issues.'),
(7, 'Call of Duty: Modern Warfare 2', 'https://store.steampowered.com/app/10180/Call_of_Duty_Modern_Warfare_2/', 3, 'Great singleplayer story and arguably the best multiplayer COD experience to date. However, the nerfed modding and lack of server support in comparison to previous installments in the series and also being prone to dangerous exploits such as RCE, it\'s hard to give this game a good score.'),
(8, 'Arma 3', 'https://arma3.com/', 4, 'The best military simulator. Has large scale warfare and great multiplayer experience. However, plagued by bad optimization.'),
(9, 'Battlefield 4', 'https://www.ea.com/games/battlefield/battlefield-4', 4, 'Great multiplayer experience. Amazing new features such as full environmental destruction. Pretty bad and exploitable networking code.'),
(10, 'Minecraft', 'https://www.minecraft.net', 5, 'Great sandbox game. Unlimited gameplay possibilities. Hours of endless fun. Great with friends. Regular massive updates.'),
(11, 'Escape from Tarkov', 'https://www.escapefromtarkov.com/', 4, 'Probably most hardcore and visceral close-quarter infantry combat experience to date. Exceptional focus on realism. Great graphical and sound design. Still lacking in basic features. Rare and slow updates. Currently subpar optimization. ');

ALTER TABLE `ratings`
  ADD PRIMARY KEY (`ID`);

ALTER TABLE `ratings`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

CREATE USER 'ratings_user'@'%' IDENTIFIED BY 'pw_ratings';
GRANT ALL PRIVILEGES ON rating_database.* TO 'ratings_user'@'%';
FLUSH PRIVILEGES;

