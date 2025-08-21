import math

ancho = float(input("Ingrese el ancho del rectangulo:"))
largo = float(input("Ingrese el largo del rectangulo:"))

hipotenusa = math.sqrt(math.pow(ancho, 2) + math.pow(largo, 2))
print("La diagonal del rectángulo mide: ", hipotenusa)

