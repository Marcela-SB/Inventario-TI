from modulos import *

def realizarInventario(self):
    self.inventario = Toplevel()
    self.inventario.title("Inventário")
    self.inventario.configure(bg= "#D9D9D9")
    self.inventario.geometry("500x400")     # Largura x Altura
    self.inventario.resizable(False, False)     # RESPONSIVIDADE
    self.inventario.focus_force()
    self.inventario.grab_set()


# ----------- BOTÕES ----------- 


# ----------- LABELS E INPUTS ----------- 