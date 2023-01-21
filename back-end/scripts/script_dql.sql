-- -----------------------------------------------------
-- Select da tabela Hoteis
-- -----------------------------------------------------

-- Seleciona os Hoteis pela Cidade. --
SELECT
	id_hotel AS "Id Hotel",
    name_hotel AS "Hotel",
    city AS "Cidade",
    coust AS "Preço"
FROM tb_hoteis
WHERE city = 'Blumenau';


-- Seleciona os Hoteis em ordem cresente de preço por cidade. --
SELECT
	id_hotel AS "Id Hotel",
    name_hotel AS "Hotel",
    city AS "Cidade",
    coust AS "Preço"
FROM tb_hoteis
WHERE city = 'Blumenau'
ORDER BY coust ASC;


-- Seleciona todos os Hoteis em ordem cresente de preço e cidade. --
SELECT
	id_hotel AS "Id Hotel",
    name_hotel AS "Hotel",
    city AS "Cidade",
    coust AS "Preço"
FROM tb_hoteis
ORDER BY coust ASC, city ASC;


-- -----------------------------------------------------
-- Select da tabela Usuários
-- -----------------------------------------------------

SELECT 
	id_users AS "Id Usuário",
    name AS "Nome",
    gender AS "Sexo",
    cpf AS "CPF",
    cep AS "CEP",
    phone AS "Telefone",
    cellphone AS "Celular",
    email AS "Email",
    password AS "Senha"
FROM tb_users;


-- -----------------------------------------------------
-- Select da tabela Histórico
-- -----------------------------------------------------

SELECT
	id_history AS "Id Histórico",
    fk_id_users AS "ID do Usuário",
    fk_id_hotel AS "ID do Hotel",
    check_in AS "Entrada",
    check_out AS "Saída"
FROM tb_historic;

-- Select com as outras tabelas --

SELECT
	id_users AS "Número do Usuário",
    name AS "Nome",
    gender AS "Sexo",
    cpf AS "CPF",
    cep AS "CEP",
    phone AS "Telefone",
    cellphone AS "Celular",
    email AS "Email",
    password AS "Senha",
    id_history AS "Número do Histórico",
    fk_id_users AS "Id do Usuário",
    fk_id_hotel AS "Id do Hotel",
    check_in AS "Entrada",
    check_out AS "Saída",
    id_hotel AS "Número do Hotel",
    name_hotel AS "Hotel",
    city AS "Cidade",
    coust AS "Diária"
FROM tb_historic
INNER JOIN tb_users
    ON id_users = fk_id_users
INNER JOIN tb_hoteis
	ON id_hotel = fk_id_hotel;