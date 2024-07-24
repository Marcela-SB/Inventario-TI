# BIBLIOTECAS USADAS
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Label
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
#from tkinter import tix
import config


# VARIÁVEIS GLOBAIS
def responsa(nome):
    global nameUser
    config.nameUser = nome

def NivelUser(nivel):
    global acessNv
    config.acessNv = nivel

def alterarBt(ent):
    global bt
    config.bt = str(ent)


#VALIDAÇÃO NUMÉRICA DE TOMBO
def validarEntrada(action, value):
    if action != '1':  # Não é uma ação de inserção, permite todas as ações de deleção
        return True
    if value.isdigit() and len(value) <= 12:  # Verifica se o valor é dígito e tem no máximo 12 caracteres
        return True
    return False