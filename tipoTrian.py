# Nombre: tipoTrian.py
# Ovjetivo: Identificar que tipo de triángulo se introuce 
# Autor: Rafael Ochoa
# Fecha: 01/07/2019

import math as mat
import os

#----------------------------
# Función para identificar triángulos
#----------------------------
def trian(l1, l2, l3):
    if l1 == l2 and l1 == l3:
        return "El triángulo es Equilatero"
    elif l1 == l2 or l2 == l3 or l1 == l3:
        return "El triángulo es Isósceles"
    elif l1 != l2 or l2 != l3 or l1 != l3:
        return "El triángulo es Escaleno"
        

def main():
    ciclo = True
    while(ciclo == True):
        print("*** Script para identificar un tipo de triángulo ***")
        l1 = float(input(" Introduce el valor del primer lado: "))
        l2 = float(input(" Introduce el valor del segundo lado: "))
        l3 = float(input(" Introduce el valor del tercer lado: "))
        # Invocar un método
        print("El triándulo es: ", trian(l1, l2, l3))

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