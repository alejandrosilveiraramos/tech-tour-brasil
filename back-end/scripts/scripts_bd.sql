-- -----------------------------------------------------
-- Table tb_hoteis
-- -----------------------------------------------------

CREATE TABLE tb_hoteis (
  id_hotel SERIAL,
  name_hotel VARCHAR(45) NOT NULL,
  city VARCHAR(45) NOT NULL,
  coust DECIMAL(9,2) NOT NULL,
  PRIMARY KEY (id_hotel));


-- -----------------------------------------------------
-- Table tb_users
-- -----------------------------------------------------

CREATE TABLE tb_users (
  id_users SERIAL,
  name VARCHAR(45) NOT NULL,
  gender BOOL NOT NULL,
  cpf VARCHAR(11) NOT NULL,
  cep VARCHAR(8) NOT NULL,
  phone VARCHAR(45) NULL,
  cellphone VARCHAR(45) NOT NULL,
  email VARCHAR(45) NOT NULL,
  password VARCHAR(45) NOT NULL,
  PRIMARY KEY (id_users));

 
-- -----------------------------------------------------
-- Table tb_historic
-- -----------------------------------------------------

DROP TABLE IF EXISTS tb_historic;

CREATE TABLE IF NOT EXISTS tb_historic (
    id_history INT NOT NULL,
    fk_id_users INT NOT NULL,
    fk_id_hotel INT NOT NULL,
    check_in DATE NULL,
    check_out DATE NULL,
  PRIMARY KEY (id_history),
  FOREIGN KEY (fk_id_users)
    REFERENCES tb_users (id_users),
  FOREIGN KEY (fk_id_hotel)
    REFERENCES tb_hoteis (id_hotel));
