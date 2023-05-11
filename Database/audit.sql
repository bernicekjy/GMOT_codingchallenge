SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+08:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `audit`
--

-- --------------------------------------------------------

--
-- Table structure for table `audit`
--

CREATE DATABASE IF NOT EXISTS `audit` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `audit`;

DROP TABLE IF EXISTS `audit`;

DROP TABLE IF EXISTS `audit`;
CREATE TABLE IF NOT EXISTS `audit` (
  `changeID` varchar(20) NOT NULL,
  `clientID` varchar(20) NOT NULL,
  `newCommission` float NOT NULL,
  `newGrossAmount` float NOT NULL,
  `updateTime` datetime NOT NULL,
  `submitterID` varchar(20) NOT NULL,
  `approvalID` varchar(20) NOT NULL,
  `oldCommission` float NOT NULL,
  `oldGrossAmount` float NOT NULL,
  PRIMARY KEY (`changeID`),
  /*FOREIGN KEY clientID REFERENCES client(clientID),
  FOREIGN KEY submitterID REFERENCES pending(submitterID),
  FOREIGN KEY approvalID REFERENCES client(adminID),*/
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `audit` (`changeID`, `clientID`, `newCommission`, `newGrossAmount` , `updateTime` , `submitterID`, `approvalID`,`oldCommission`,`oldGrossAmount`) VALUES
(),

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;