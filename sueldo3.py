# Nombre: sueldo3.py
# Ovjetivo:  Realice un programa en Python que dado como datos los sueldos de 10 trabajadores de una empresa, 
# obtenga el total de nómina de la misma. Puede utilizar un ciclo for o un ciclo while.
# Autor: Rafael Ochoa
# Fecha: 04/07/2019

def main():
    nomina = 0
    cont = 0
    while (cont != 10):
        cont = cont + 1
        print("Trabajador número ",cont,":")
        suel = float(input("Introduce el sueldo: "))
        nomina = nomina + suel
    print("La nómina es: ",nomina)


if __name__ == "__main__":
    main()