CREATE DATABASE estoque_loja;
USE estoque_loja;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL UNIQUE,
    descricao VARCHAR(100),
    estoque INT NOT NULL,
    preco DECIMAL(8,2) NOT NULL
);

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    qtde_vendida TINYINT NOT NULL,
    data_venda DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status ENUM('ABERTA','FINALIZADA','CANCELADA') NOT NULL
);






    




