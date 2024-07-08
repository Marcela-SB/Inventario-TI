from conexaoBD import *

def verificarItem(self, tb):
    #CONECTANDO O BD E INICIALIZANDO CURSOR
    conexao = conectar_bd(self)
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT tombo FROM item WHERE tombo = %s", (tb,))
        conexao.commit()

        # Verifica se o item foi encontrado
        if cursor.fetchone() is not None:
            return True
        else:
            return False

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Item não existe:  {err}")
        return False
    finally:
        cursor.close()
        conexao.close()