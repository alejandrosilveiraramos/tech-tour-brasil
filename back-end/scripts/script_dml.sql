-- -----------------------------------------------------
-- DML - Hotel
-- -----------------------------------------------------

INSERT INTO hotel
	(hotel_id, hotel_name, hotel_city, totel_coust)
VALUES 
	(1, 'Glória', 'Blumenau', '220'),
	(2, 'Plaza Hering', 'Blumenau', '450'),
	(3, 'Himmelblau', 'Blumenau', '210'),
	(4, 'Ibis', 'Indaial', '190'),
	(5, 'Ibis', 'Timbó', '190'),
	(6, 'Ibis', 'Blumenau', '200'),
	(7, 'Quality', 'Blumenau', '215'),
	(8, 'Hotel 10', 'Gaspar', '170'),
	(9, 'Vila do Vale', 'Pomerode', '160'),
	(10, 'Quality', 'Indaial', '205'),
    (11, 'Plaza', 'Florianópolis', '500'),
    (12, 'Loft Vila', 'Timbó', '170'),
    (13, 'Europa', 'Pomerode', '150'),
    (14, 'Park House', 'Indaial', '185'),
    (15, 'Park House', 'Gaspar', '150'),
    (16, 'Bonatti', 'Itajaí', '140'),
    (17, 'Jardim', 'Ilhota', '160'),
    (18, 'Casa Branca', 'Gaspar', '155'),
    (19, 'Blu', 'Blumenau', '230'),
    (20, 'Austria', 'Pomerode', '195');


-- -----------------------------------------------------
-- DML - User
-- -----------------------------------------------------

INSERT INTO tb_user
	(id_users, last_name, first_name, gender, cpf, cep, phone, cellphone, email, password)
VALUES 
    ('1', 'Simas', 'David', '1', '11144477735', '89057060', '33390217', '999913988', 'david@gmail.com', '1234'),
    ('2', 'Indio', 'Alejandro', '1', '11144477735', '89057060', '33390217', '999913988', 'alejandro@gmail.com', '1234'),
    ('3', 'Saurro', 'Melissa', '0', '11144477735', '89057060', '33390217', '999913988', 'melissa@gmail.com', '1234');


-- -----------------------------------------------------
-- DML - History
-- -----------------------------------------------------

INSERT INTO tb_history
	(id_history, fk_id_user, fk_id_hotel, check_in, check_out)
values
	('1', '3', '11', '2022-01-21', '2022-01-30'),
	('2', '3', '7', '2022-01-25', '2022-02-15');