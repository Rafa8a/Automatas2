# Nombre: circunferencia.py
# Ovjetivo: Calcular el área de una circunferencia e importar math
# Autor: Rafael Ochoa
# Fecha: 01/07/2019

import math as mat
import os

#----------------------------
# Función para calcular área
#----------------------------
def calcularArea(r):
    area = mat.pi * (mat.pow(r,2))
    return area

#----------------------------
# Función para calcular diámetro
#----------------------------
def calcularDiametro(d):
    diam = d * 2
    return diam

def main():
    ciclo = True
    while (ciclo == True):
        print(" *** Script para calcular el área de una circunferencia ***")
        radio = float(input(" Introduce el valor del radio "))
        # Invocar un método
        print("El área es: ", calcularArea(radio))
        print("El diámetro es: ", calcularDiametro(radio))
        
        resp = input("¿Desea otro cálculo? s/n")
        if resp == "s" or resp == "S":
            ciclo = True
            # Limpiar la pantalla 
            os.system("cls")
        else: 
            ciclo = False
            # Limpiar la pantalla 
            os.system("cls")

if __name__ == "__main__":
    main()