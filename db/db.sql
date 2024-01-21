CREATE SCHEMA IF NOT EXISTS `smart-climate-controll` DEFAULT CHARACTER SET utf8 ;
USE `smart-climate-controll` ;

CREATE TABLE IF NOT EXISTS `alert` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `action` VARCHAR(45) NOT NULL,
  `cause` VARCHAR(45) NULL,
  `room_nr` INT NOT NULL,
  `date` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;