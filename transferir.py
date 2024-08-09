import pandas as pd
from modulos import *

def conectar_bd():
    senha = "cfeb6252a2;" #obterSenha()
    '''if senha is None:
        messagebox.showerror("Erro", "Nenhuma senha fornecida.")
        return None'''
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="admin",
            password= "admin1234",
            database="inventario"
        )
        #messagebox.showinfo("Conexão", "Conexão com o banco de dados estabelecida com sucesso!")
        return conexao
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
        return None

def tranferencia():
    # Carregar o arquivo Excel
    excel = pd.ExcelFile(r"C:\Users\Suporte\Downloads\Inventario Janeiro 2024 (1).xlsx")

    dados = []

    # Iterar sobre cada aba
    for sheet in excel.sheet_names:
        # Ler a aba atual sem cabeçalhos
        df = pd.read_excel(excel, sheet_name=sheet, header=None)
        
        # Verificar se a aba tem pelo menos 3 colunas
        if df.shape[1] >= 3:
            # Selecionar as colunas desejadas
            colunas_selecionadas = df.iloc[:, [0, 1, 2]].copy()

            # Usar .loc para adicionar uma nova coluna
            colunas_selecionadas.loc[:, 'Aba'] = sheet

            # Adicionar os dados desta aba à lista DADOS
            dados.append(colunas_selecionadas)

    # Combinar todos os DataFrames em um único DataFrame
    dadosFinais = pd.concat(dados, ignore_index=True)


    #-------------- MODIFICANDO DADOS --------------

    i = 0

    # Iterar sobre cada linha do DataFrame
    for index, row in dadosFinais.iterrows():
        if row[0] == "SEM TOMBO":  # Verifica se o valor da coluna A é "SEM TOMBO"
            # Substitui por "????????i", onde i é o contador
            dadosFinais.at[index, 0] = f"????????{i}" 
        i+=1 # Incrementa o contador


    #-------------- INSERINDO NO BANCO DE DADOS --------------
    conexao = conectar_bd()
    cursor = conexao.cursor()

    #cursor.execute("TRUNCATE TABLE item")
    #conexao.commit()

    def sala_existe(cursor, sala):
        cursor.execute("SELECT COUNT(*) FROM salas WHERE salaId = %s", (sala,))
        result = cursor.fetchone()
        return result[0] > 0


    def inserir_sala(cursor, sala):
        cursor.execute("INSERT INTO salas (salaId) VALUES (%s)", (sala,))
        conexao.commit()

    try:
        for index, row in dadosFinais.iterrows():
            tombo = row[0]  # Coluna A
            tipo = row[1].split()[0]  # 1ª palavra da coluna B
            descricao = row[1]  # Coluna B
            sala = row['Aba'][5:]  # Pegar o nome da aba e remover os primeiros 5 caracteres
            obs = row[2]  # Coluna C

            # Verificar se a sala já existe
            if not sala_existe(cursor, sala):
                inserir_sala(cursor, sala)

            print("%s, %s, %s, %s, %s" % (tombo, tipo, descricao, sala, obs))

            # Inserir o item
            cursor.execute("INSERT INTO item (tombo, tipo, descricao, salaId, obs) VALUES (%s, %s, %s, %s, %s)", 
                        (tombo, tipo, descricao, sala, obs))
            conexao.commit()

    except Exception as err:
        print(f"Erro ao executar comandos: {err}")
    finally:
        cursor.close()
        conexao.close()


tranferencia()