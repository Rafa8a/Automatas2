# Nombre: BD.py
# Ovjetivo:  Script para realizar una BD 
# Autor: Rafael Ochoa
# Fecha: 15/07/2019

# Abrir la conexion a la base de datos
import pymysql
import tkinter as tk
from tkinter import Label
from reportlab.pdfgen import canvas
def main():
    try:
        global db
        db = pymysql.connect("localhost","root","","BasePrueba")
        print("Conexion establecida...")
    except:
        print("Error, no se establecio la conexion")
    #preparar el objeto cursor usando el metodo cursor()   

if __name__ == "__main__":
    main()
  
def insertar():
    # Insertar un valor
    cursor = db.cursor()
    cadsqlinsert = "insert into Usuario values(" + Txt1.get()+ ",'" + Txt2.get() + "');"
    # podemos utilizar las instrucciones sql
    cursor.execute(cadsqlinsert)
    db.commit()
    print("Datos insertados correctamente")

def reporte():   
    print("Generando reporte...")
    esp = ""
    a = 740

    c = canvas.Canvas("Reporte.pdf")
    c.drawString(18,830,"Reporte semanal")
    c.drawString(18,810,"Clave " + " Nombre")

    cursor = db.cursor()
    cadsqlbuscar = "select * from Usuario;"
    cursor.execute(cadsqlbuscar)
    result=cursor.fetchall()
    for row in result:  
        clave = row[0]
        nombre = row[1]
        c.drawString(18,a,"     {0}".format(clave,nombre) + esp + "    {1}".format(clave,nombre))
        a = a - 15

    c.save()
        

def consultar():
    # Buscar un valor
    cursor = db.cursor()
    cadsqlbuscar = "select * from Usuario where id =" + Txt1.get() + ";"
    cursor.execute(cadsqlbuscar)
    result=cursor.fetchall()
    for row in result:
        clave = row[0]
        nombre = row[1]
        print("Consultando...")
        print("clave = ", clave, "Nombre = ",nombre)

def eliminar():
    cursor = db.cursor()
    # Eliminar un valor
    cadsqldel = "delete from Usuario where id =" + Txt1.get() + ";"
    cursor.execute(cadsqldel)
    db.commit()
    print("Dato eliminado correctamente")

def actualizar():    
    # Actualizar un dato
    cursor = db.cursor()
    cadsqlupd = "UPDATE `Usuario` SET `Nombre`='" + Txt2.get() + "' WHERE id =" + Txt1.get() + ";"
    cursor.execute(cadsqlupd)
    db.commit()
    print("Dato actualizado correctamente")

#creamos la ventana
root = tk.Tk()
root.title("Base de datos con Python")
#creamos las etiquetas
eti1 = Label(None, text = 'Base de datos')

#agregamos la etiqueta a la ventana
eti1.pack()

root.geometry("500x250")
Txt1 = tk.Entry(root)
# Posicionarla en la ventana.
Txt1.place(x = 200, y = 50)

Txt2 = tk.Entry(root)
# Posicionarla en la ventana.
Txt2.place(x = 200, y = 100)

ins = tk.Button(root, text = "Insertar",
    command = insertar)
ins.place(x = 40, y = 150)

rep = tk.Button(root, text = "Reporte",
    command = reporte)
rep.place(x = 40, y = 200)

cons = tk.Button(root, text = "Consultar",
    command = consultar)
cons.place(x = 400, y = 150)

eli = tk.Button(root, text = "Eliminar",
    command = eliminar)
eli.place(x = 400, y = 200)

act = tk.Button(root, text = "Actualizar",
    command = actualizar)
act.place(x = 225, y = 150)

#ciclo de espera de eventos
root.mainloop()

