-- Banco de Dados: Loja de Livros
-- TABELA: Clientes
CREATE TABLE Clientes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    nomeCliente VARCHAR(100) NOT NULL,
    emailCliente VARCHAR(100) NOT NULL UNIQUE,
    dataCadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- TABELA: Compras
-- =====================================================
CREATE TABLE Compras (
    CompraID INTEGER PRIMARY KEY AUTOINCREMENT,
    ClienteID INTEGER NOT NULL,
    NomeLivro VARCHAR(150) NOT NULL,
    DataCompra DATETIME DEFAULT CURRENT_TIMESTAMP,
    Valor DECIMAL(10, 2),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
);

-- =====================================================
-- ÍNDICES (Melhor performance)
-- =====================================================
CREATE INDEX idx_clientes_email ON Clientes(emailCliente);
CREATE INDEX idx_compras_clienteid ON Compras(ClienteID);
CREATE INDEX idx_compras_datacompra ON Compras(DataCompra);

-- =====================================================
-- DADOS DE EXEMPLO
-- =====================================================

-- Inserir clientes de exemplo
INSERT INTO Clientes (nomeCliente, emailCliente) VALUES
('João Silva', 'joao@email.com'),
('Maria Santos', 'maria@email.com'),
('Pedro Oliveira', 'pedro@email.com'),
('Ana Costa', 'ana@email.com');

-- Inserir compras de exemplo
INSERT INTO Compras (ClienteID, NomeLivro, Valor) VALUES
(1, 'O Senhor dos Anéis', 89.90),
(1, '1984 - George Orwell', 45.00),
(2, 'Dom Casmurro', 35.50),
(2, 'Cem Anos de Solidão', 52.00),
(3, 'O Código Da Vinci', 60.00),
(4, 'A Menina que Roubava Livros', 48.90);

-- Total gasto por cliente
-- SELECT c.nomeCliente, COUNT(co.CompraID) as TotalCompras, SUM(co.Valor) as TotalGasto
-- FROM Clientes c
-- LEFT JOIN Compras co ON c.ID = co.ClienteID
-- GROUP BY c.ID, c.nomeCliente;
SELECT * FROM Clientes; 
SELECT * FROM Compras; 
SELECT 
    c.nomeCliente AS "Nome do Cliente",
    co.NomeLivro AS "Nome do Livro",
    co.DataCompra AS "Data da Compra",
    co.Valor AS "Valor"
FROM Compras co
INNER JOIN Clientes c ON co.ClienteID = c.ID
ORDER BY co.DataCompra DESC;
