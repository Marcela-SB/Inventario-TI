# Inventario STI DEART
Sistema de Inventário para o Setor TI do DEART.

Sistema contém como funções:
- Adicionar/Remover/Editar item
- Busca
- Impressão de informações (gerais e específicas) de
  - item
  - inventário
- Histórico de movimentação de cada item
  - e criação de novas movimentações

---
Linguagem: ![Python](https://img.shields.io/badge/-Python-0D1117?style=for-the-badge&logo=python&labelColor=0D1117)&nbsp;

Bibliotecas: 
- Tkinter
- Pillow (PIL):  ```pip install pillow```
- bcrypt: ```pip install bcrypt```
- mysql.connector: ```pip install mysql-connector-python```
- config: ```pip install python-decouple``` ou ```pip install configparser```

</br>

# BANCO DE DADOS:

**Tabela *salas*:**
- *salaId* CHAR(3) PRIMARY KEY,
- *funcao* VARCHAR(30),
- *predio* VARCHAR(10)
  
**Tabela *item*:**
- *tombo* CHAR(10) PRIMARY KEY,
- *tipo* VARCHAR(20),
- *descricao* VARCHAR(50),
- *salaId* CHAR(3), FOREIGN KEY (*salaId*) REFERENCES **salas**(*salaId*)

**Tabela *movimentacao*:**
- *id INT AUTO_INCREMENT PRIMARY KEY,
- *ItemID* CHAR(10), FOREIGN KEY (*ItemID*) REFERENCES **item**(*tombo*),
- *salaOrigemID* CHAR(3), FOREIGN KEY (*salaOrigemID*) REFERENCES **salas**(*salaId*),
- *salaDestinoID* CHAR(3), FOREIGN KEY (*salaDestinoID*) REFERENCES **salas**(*salaId*),
- *data* DATE,
- *responsavel* VARCHAR(50)
