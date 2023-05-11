SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+08:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pending`
--

-- --------------------------------------------------------

--
-- Table structure for table `pending`
--

CREATE DATABASE IF NOT EXISTS `pending` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `pending`;

DROP TABLE IF EXISTS `pending`;

DROP TABLE IF EXISTS `pending`;
CREATE TABLE IF NOT EXISTS `pending` (
  `submissionID` varchar(20) NOT NULL,
  `clientID` varchar(20) NOT NULL,
  `newCommission` float NOT NULL,
  `newGrossAmount` float NOT NULL,
  `submitterID` varchar(20) NOT NULL,
  PRIMARY KEY (`submissionID`)
  FOREIGN KEY submitterID REFERENCES client(clientID),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;