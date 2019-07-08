# Nombre: DiccionarioITC.py
# Ovjetivo:  Realice un programa en python que permita almacenar en un diccionario los datos generales 
# de un alumno del ITC. Deberá poder imprimir cada uno de éstos datos a través de la clave del diccinario y modificar al menos uno de los datos (ej. número telefónico).
# Autor: Rafael Ochoa
# Fecha: 04/07/2019

lista = []

# Crear funciones para cada opción 

def main():
    ciclo = True
    while (ciclo == True):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido paterno: ")
        control = input("Ingrese el número de control: ")

        materias = {"Nombre": nombre, 
                    "Apellido paterno": apellido,
                    "Número de control": control}

        lista.append(materias)

        resp = input("Desea agregar otro alumno? s/n: ")
        if (resp == "s" or resp == "S"):
            ciclo = True
        else:
            ciclo = False

    print("*******************************************")
    for alum in lista:
        print(alum)

if __name__ == "__main__":
    main()
