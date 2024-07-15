from modulos import *


def show_app(app_instance):
    app_instance.main_app.deiconify()  # Mostrar a janela principal do app
    app_instance.root.withdraw()  # Esconder a janela de login


def validarUser(self):
    user = self.inputLogin.get()
    pw = self.inputSenha.get()

    if(user and pw):
        show_app(self)
    else:
        messagebox.showwarning("Erro", "Campos em branco! Por favor, preencha todos!")

'''def chamarConexao(self):
        iniciar = None
        while(iniciar == None):
            iniciar = conectar_bd(self)'''


def novoUser(self):
    messagebox.showinfo("Info", "Botão Novo User")