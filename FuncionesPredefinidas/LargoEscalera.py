""""
    Escribe un programa que determine el largo que debe tener una escalera, la cual se necesita para alcanzar una altura determinada, cuando se pone contra una casa. La altura que se desea alcanzar y el ángulo que deberá hacer la escalera contra la pared, son datos que te proporciona el usuario. Para calcular el largo de la escalera usa la siguiente ecuación:

    largo=altura/coseno(ángulo)

    Recuerda que las funciones de Python que calculan seno y coseno, reciben los ángulos en radianes, pero tu programa va a recibir los ángulos en grados.

    Entrada

    Un número que corresponde a la altura de la casa (flotante positivo) y el ángulo en grados (entero positivo), en ese orden.

    Salida

    Un número que representa el largo que debe tener la escalera. IMPORTANTE: Redondea el número para que el resultado sea entero. Utiliza la función adecuada que te provee Python para realizar un redondeo.
"""

import math

def grad_to_rad(grad):
    return grad * (math.pi / 180)

height = float(input("Ingrese la altura de la casa: "))
angle = int(input("Ingrese el ángulo en grados: "))

stair_length = height / math.cos(grad_to_rad(angle))
stair_length = round(stair_length)

print(f"El largo de la escalera debe ser: {stair_length}")