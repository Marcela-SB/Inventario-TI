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


def responsa(nome):
    global nameUser
    config.nameUser = nome

def NivelUser(nivel):
    global acessNv
    config.acessNv = nivel

def alterarBt(ent):
    global bt
    config.bt = ent