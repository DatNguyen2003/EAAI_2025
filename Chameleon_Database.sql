CREATE DATABASE `chameleon` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
CREATE TABLE `key` (
  `id` int NOT NULL AUTO_INCREMENT,
  `key_word_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `key_attributes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `attributes` varchar(255) NOT NULL,
  `key_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `key_id` (`key_id`),
  CONSTRAINT `key_attributes_ibfk_1` FOREIGN KEY (`key_id`) REFERENCES `key` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
