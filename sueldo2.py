# Nombre: sueldo2.py
# Ovjetivo:  Realice un programa en Python que dado como datos la categoría y el sueldo de un trabajor, 
# calcule el aumento correspondiente teniendo en cuenta la siguiente información e imprima el nuevo sueldo del trabajador:
# Autor: Rafael Ochoa
# Fecha: 04/07/2019

def main():
    print("Categoría 1")
    print("Categoría 2")
    print("Categoría 3")
    print("Categoría 4")
    cat = input("Itrodice la categoría que pertenece: ")
    suel = float(input("Introduce el sueldo que tiene :"))

    if (cat == "1"):
        suel = suel + (suel * .15)

    elif (cat == "2"):
        suel = suel + (suel * .10)

    elif (cat == "3"):
        suel = suel + (suel * .8)
    
    elif (cat == "4"):
        suel = suel + (suel * .7)

    else:
        print("Introduce una categoría válida")  

    print("Tu sueldo es: ",suel)  

if __name__ == "__main__":
    main()