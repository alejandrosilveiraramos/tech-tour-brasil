-- -----------------------------------------------------
-- Table tb_hotel
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS hotel (
    hotel_id SERIAL,
    hotel_name VARCHAR(64) NOT NULL,
    hotel_city VARCHAR(64) NOT NULL,
    hotel_coust DECIMAL(9,2) NOT NULL,
  PRIMARY KEY (id_hotel));


-- -----------------------------------------------------
-- Table tb_users
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL,
    user_lastName VARCHAR(64) NOT NULL,
    user_firstName VARCHAR(64) NOT NULL,
    user_gender BOOL NULL,
    user_cpf VARCHAR(11) NOT NULL,
    user_cep VARCHAR(8) NOT NULL,
    user_phone VARCHAR(10) NULL,
    user_cellphone VARCHAR(11) NOT NULL,
    user_email VARCHAR(128) NOT NULL,
    user_password VARCHAR(64) NOT NULL,
  PRIMARY KEY (id_user));

 
-- -----------------------------------------------------
-- Table tb_history
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS history (
    history_id SERIAL,
    history_fk_id_user INT NOT NULL,
    history_fk_id_hotel INT NOT NULL,
    history_check_in DATE NULL,
    history_check_out DATE NULL,
  PRIMARY KEY (history_id),
  FOREIGN KEY (history_fk_id_user)
    REFERENCES users (user_id),
  FOREIGN KEY (history_fk_id_hotel)
    REFERENCES hotel (hotel_id));