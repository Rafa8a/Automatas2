# Nombre: sueldo.py
# Ovjetivo:  Realice un programa en Python que dado como dato el sueldo de un trabajador
# le aplique un aumento del 15% si su sueldo es inferior a $1000.00 y del 12% en caso contrario. Imprima el nuevo sueldo del trabajador.
# Autor: Rafael Ochoa
# Fecha: 04/07/2019

def main():
    suel = float(input("Introduce tu sueldo: "))
    
    if (suel < 1000):
        suel = (suel * .15) + suel

    else:
        suel = (suel * .12) + suel
    
    print("El sueldo es: ", suel)
    
if __name__ == "__main__":
    main()