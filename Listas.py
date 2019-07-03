# Nombre: Listas.py
# Ovjetivo: Muestra el funcuinamiento de las  listas en Python
# Autor: Rafael Ochoa
# Fecha: 02/07/2019

#----------------------------
# Crear la lista global
#----------------------------
lista = []

#----------------------------
# Función para agregar elementos a la lista
#----------------------------
def agegarItem(dato):
    lista.append(dato)
    print("*************")
    print("Dato agregado")

#----------------------------
# Función para imprimir los elementos de la lista
#----------------------------
def imprime():
    print("Imprimiendo datos...")
    print("********************")
    j = 0
    for i in lista:
        print("Item: ", j, ", ", i)
        j = j + 1

#----------------------------
# Función para eliminar items en la lista
#----------------------------
def eliminarItem(dato):
    # Buscar el item
    if (dato in lista):
        lista.remove(dato)
        print("**************")
        print("Item eliminado")
    else:
        print("*****************")
        print("Item no encitrado")

def main():
    ciclo = True
    while(ciclo == True):
        print("--- Menú para manejar una lista ---")
        print("1. Agregar un elemento a la lista: ")
        print("2. Eliminar un elemento de la lista: ")
        print("3. Desplegar los elementos de la lista: ")
        print("4. Modificar un elemento de la lista: ")
        print("5. Buscar un elemento de la list: ")
        print("6. Salir")
        opc = input("Elija una opción del 1 - 6: ")

        if (opc == "1"):
            dato = input("Introduce el dato a agregar: ")
            agegarItem(dato)
        elif (opc == "2"):
            dato = input("Introduce el dato que deseas eliminar: ")
            eliminarItem(dato)
        elif (opc == "3"):
            imprime()
        elif (opc == "4"):
            print("Se modificará algo")
        elif (opc == "5"):
            print("Se buscará algo")
        elif (opc == "6"): 
                ciclo = False
        else:
            print("Eliga una opción del 1 - 6")

if __name__ == "__main__":
    main()