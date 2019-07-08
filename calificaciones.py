# Nombre: sueldo3.py
# Ovjetivo:  Realice un programa en Python que permita capturar en una lista las calificaciones de N alumnos
# Autor: Rafael Ochoa
# Fecha: 04/07/2019

lista = []

def promedio():
    prom = 0.0
    for cali in lista:
        prom = prom + cali
    prom = prom / len(lista)
    return prom

def aproRepro():
    apro = 0
    repro = 0
    porApro = 0.0
    porRepro = 0.0
    almMay = 0
    for cali in lista:
        if(cali > 80):
            almMay = almMay + 1

        if (cali >= 70):
            apro = apro + 1
        else:
            repro = repro + 1

    porApro = (apro * 100) / len(lista)
    porRepro = (repro * 100) / len(lista)

    print("Número de alumnos aprobados: ", apro)
    print("Número de alumnos reprobados: ", repro)
    print("Porcentaje de alumnos aprobados: ", porApro)
    print("Porcentaje de alumnos reprobados: ", porRepro)
    print("Número de alumnos con calificación mayor a 80: ",almMay)
    


def main():
    ciclo = True
    while (ciclo == True):
        cal = float(input("Introduce la calificación: "))
        lista.append(cal)
        print("*************")
        print("Calificación guardada")
    
        resp = input("Desea calcular otra calificación? s/n: ")
        if (resp == "s" or resp == "S"):
            ciclo = True
        else:
            ciclo = False

    print("Promedio de calificaciones: ",promedio())
    aproRepro()
    



if __name__ == "__main__":
    main()

