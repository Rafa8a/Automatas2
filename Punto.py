# Nombre: Punto.py
# Ovjetivo:  Muestra el manejo de clases
# Autor: Rafael Ochoa
# Fecha: 05/07/2019

import math as mat

class Punto(object):
    # Constructor de la clase
    def __init__(self,valorX, valorY):
        self.x = valorX
        self.y = valorY

    # Métodos get
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # Métodos set
    def setX(self,valorX):
        self.x = valorX
    def setY(self,valorY):
        self.y = valorY

    def toString(self):
        return "El punto tiene las siguientes coordenadas: ",self.x, ", ",self.y

class Circunferenia (Punto):
    def __init__(self, valorRadio):
        self.radio = valorRadio

    def getRadio(self):
        return self.radio

    def setRadio(self, valorRadio):
        self.radio = valorRadio

    def getArea(self):
        return mat.pi * mat.pow(self.getRadio(), 2)

    def toString(self):
        return "La circunferencia tiene como centro. ", self.getX(), ", ",self.getY(), self.getRadio(), "el área es: ",self.getArea()

class Cilindro (Circunferenia):
    def __init__(self, valorAltura):
        self.altura = valorAltura

    def getAltura(self):
        return self.altura
    
    def setAltura(selt, valorAltura):
        self.altura = valorAltura

    def getVolumen(self):
        return self.altura * self.getArea()

    def toString(self):
        return " El cilindro: ", "X: ",self.getX(), " Y: ",self.getY(), " Radio: ", self.getRadio(), " Área: ",self.getArea(), " Volumen: ", self.getVolumen()

# Programa principal
def main():
    p1 = Punto(2,3)
    print(p1.toString())

    p2 = Punto(0,0)

    p2.setX(-2)
    p2.setY(-4)
    print(p2.toString())

    p3 = Circunferenia(12.34)
    p3.setX(10)
    p3.setY(12)
    print(p3.toString())

    p4 = Cilindro(9.81)
    p4.setX(2)
    p4.setY(2)
    p4.setRadio(3.12)
    print(p4.toString())


if __name__ == "__main__":
    main()