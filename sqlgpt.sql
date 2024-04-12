-- Tabela de Salas
CREATE TABLE Salas (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    NomeSala VARCHAR(50),
    Descricao VARCHAR(255),
    Localizacao VARCHAR(100)
);

-- Tabela de Itens
CREATE TABLE Itens (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    NomeItem VARCHAR(100),
    Descricao VARCHAR(255),
    SalaID INT,
    FOREIGN KEY (SalaID) REFERENCES Salas(ID)
);

-- Tabela de Movimentação de Itens
CREATE TABLE MovimentacaoItens (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    ItemID INT,
    TipoMovimento VARCHAR(20),
    QuantidadeMovimentada INT,
    DataHoraMovimentacao DATETIME,
    SalaOrigemID INT,
    SalaDestinoID INT,
    FOREIGN KEY (ItemID) REFERENCES Itens(ID),
    FOREIGN KEY (SalaOrigemID) REFERENCES Salas(ID),
    FOREIGN KEY (SalaDestinoID) REFERENCES Salas(ID)
);
