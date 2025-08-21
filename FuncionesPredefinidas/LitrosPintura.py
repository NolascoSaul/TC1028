import math

area = float(input("Ingrese el área a pintar: "))
pintura_por_metro = float(input("Ingrese la cantidad de pintura que se necesita por metro cuadrado: "))

litros = math.ceil(area / pintura_por_metro)


# Para cambiar formatear en terminal puedes buscar color.py
print(f"Necesitas comprar \033[34m{litros} litros\033[0m de pintura")