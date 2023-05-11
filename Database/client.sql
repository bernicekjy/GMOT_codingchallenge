SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+08:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `client`
--

-- --------------------------------------------------------

--
-- Table structure for table `client`
--

CREATE DATABASE IF NOT EXISTS `client` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `client`;

DROP TABLE IF EXISTS `client`;

DROP TABLE IF EXISTS `client`;
CREATE TABLE IF NOT EXISTS `client` (
  `clientID` varchar(20) NOT NULL,
  `Commission` float NOT NULL,
  `GrossAmount` float NOT NULL,
  `lastUpdateTime` datetime NOT NULL,
  PRIMARY KEY (`clientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `client` (`clientID`, `Commission`, 'GrossAmount', 'lastUpdateTime') VALUES
('C001', '15', '300', '2023-03-18 21:43:02'),
('C002', '30', '400', '2023-03-19 20:43:02'),
('C003', '10', '500', '2023-03-20 22:43:02'),
('C004', '20', '600', '2023-03-28 16:43:02');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;