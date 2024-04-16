from tkinter import *
from tkinter import Tk, StringVar, ttk

# import Pillow
from PIL import Image, ImageTk

# import Tkcalendar
from tkcalendar import Calendar, DateEntry

cor0 = '#4f4f4f'
cor1 = '#ffffff'
bgmid = '#4f4f4f'
bgdown = '#5f5f5f'

jan = Tk()

jan.title("Inventario DEART")
jan.geometry("900x600")
jan.configure(background = cor0)
jan.resizable(width=FALSE, height=FALSE) # bloqueia a alteração do tamanho da janela

style = ttk.Style(jan)
style.theme_use("clam")

# frames

# div superior
frameUp = Frame(jan, width=900, height=50, bg=cor1, relief=FLAT)
frameUp.grid(row=0, column=0)

# div mid
frameMid = Frame(jan, width=900, height=320, bg=bgmid, relief=FLAT)
frameMid.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# div inferior
frameDown = Frame(jan, width=900, height=430, bg=bgdown, relief=FLAT)
frameDown.grid(row=2, column=0, pady=1, padx=0, sticky=NSEW)

# modificando div superior

# abrindo imagem logo
app_img = Image.open('interface/icons/logoTop.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

logo = Label(frameUp, image=app_img, text=' STI', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=cor1, fg='black')
logo.place(x=0, y=0)



# modificando div mid

# criando inputs

# busca por tombo (input)
b_tombo = Label(frameMid, text="Tombo", height=1, anchor=NW, font=("Ivy 10 bold"), bg=bgmid, fg=cor1)
b_tombo.place(x=10, y=10)
in_nome = Entry(frameMid, width=30, justify='left', relief=SOLID)
in_nome.place(x=130, y = 11)

# busca por sala (input)
b_sala = Label(frameMid, text="Sala", height=1, anchor=NW, font=("Ivy 10 bold"), bg=bgmid, fg=cor1)
b_sala.place(x=10, y=40)
in_sala = Entry(frameMid, width=30, justify='left', relief=SOLID)
in_sala.place(x=130, y = 41)

# busca por tipo (input)
b_tipo = Label(frameMid, text="Tipo", height=1, anchor=NW, font=("Ivy 10 bold"), bg=bgmid, fg=cor1)
b_tipo.place(x=10, y=70)
in_tipo = Entry(frameMid, width=30, justify='left', relief=SOLID)
in_tipo.place(x=130, y = 71)

# busca por predio (input)
b_predio = Label(frameMid, text="Predio", height=1, anchor=NW, font=("Ivy 10 bold"), bg=bgmid, fg=cor1)
b_predio.place(x=10, y=100)
in_predio = Entry(frameMid, width=30, justify='left', relief=SOLID)
in_predio.place(x=130, y = 101)

# busca por data de movimentação (input)

b_data = Label(frameMid, text="Data de movimentação", height=1, anchor=NW, font=("Ivy 10 bold"), bg=bgmid, fg=cor1)
b_data.place(x=10, y=130)
in_data = DateEntry(frameMid, date_pattern='dd/mm/y', width=15, background='darkgray', borderwidth=2, year=2024)
in_data.place(x=203, y = 131)

jan.mainloop() # ultima linha do código