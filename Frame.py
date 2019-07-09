# Nombre: Frame.py
# Ovjetivo:  Muestra el fincionamiento básico de un Frame 
# Autor: Rafael Ochoa
# Fecha: 05/07/2019

import tkinter as tk
from tkinter import *

# Función para sumar 
def trans():
    # Recuperamos los datos de los campos de texto
    txtC1.set("Holiiiiii")

# Función para borrar la caja de texto
def borrar():
    txtC1.set("")

# Funcion para salir de la app
def salir():
    wv.destroy()

# Programa principal 

# Creamos las ventana
wv = tk.Tk()
wv.config(bd=15)
# Modificamos el tamaño de la ventana
wv.geometry("500x400")
# Titulo de la ventana
wv.title("Aiudaaaaaaaaaa")

# Creamos la etiqueta
l1 = Label(None, text="Ingresa un texto: ")

# creamos los campos de texto
txtC1 = StringVar()

Entry(wv, justify="left",textvariable=txtC1,state="disabled").pack()

#Creamos los botones
be = Button(wv, text="Tranformar", command=trans).pack(side="left")
bb = Button(wv, text="Borrar", command=borrar).pack(side="left")
bs = Button(wv, text="Salir", command=salir).pack(side="left")

# Ciclo de espera de eventos
wv.mainloop()