
CREATE SCHEMA IF NOT EXISTS `smart-climate-controll` DEFAULT CHARACTER SET utf8 ;
USE `smart-climate-controll` ;

CREATE TABLE IF NOT EXISTS `smart-climate-controll`.`room` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `preferred_temp` FLOAT NULL DEFAULT 18,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `smart-climate-controll`.`alert` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `action` VARCHAR(45) NOT NULL,
  `cause` VARCHAR(45) NOT NULL,
  `date` DATETIME NOT NULL,
  `room_id` INT NOT NULL,
  PRIMARY KEY (`id`, `room_id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_action_room_idx` (`room_id` ASC) VISIBLE,
  CONSTRAINT `fk_action_room`
    FOREIGN KEY (`room_id`)
    REFERENCES `smart-climate-controll`.`room` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `smart-climate-controll`.`measurement` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `time` DATETIME NOT NULL,
  `temperature` FLOAT NOT NULL,
  `humidity` FLOAT NOT NULL,
  `pressure` FLOAT NOT NULL,
  `room_id` INT NOT NULL,
  PRIMARY KEY (`id`, `room_id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_measurement_room1_idx` (`room_id` ASC) VISIBLE,
  CONSTRAINT `fk_measurement_room1`
    FOREIGN KEY (`room_id`)
    REFERENCES `smart-climate-controll`.`room` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;