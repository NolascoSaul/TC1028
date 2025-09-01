"""
    Desarrolla un programa que contenga las siguientes funciones:

    una función llamada area_cilindro, que reciba el radio y altura del cilindro y regrese el área calculada.
    una función llamada volumen_cilindro, que reciba el radio y altura del cilindro y regrese el volumen calculado.
    El programa debe leer el radio y la altura de un cilindro, luego llamar a las funciones y finalmente mostrar el área y volumen del cilindro.

    Entrada

    El radio del cilindro

    La altura del cilindro

    Salida

    En el primer renglón el área del cilindro utilizando el mensaje "area=" y después el valor del área formateado con 2 decimales.

    En el segundo renglón el volúmen del cilindro utilizando el mensaje "volumen=" y después el valor del volúmen formateado con 2 decimales.
"""

import math

def area_cilindro(radio: float, altura: float):
    area = 2 * math.pi * radio * (radio + altura)
    return area

def volumen_cilindro(radio: float, altura: float):
    volumen = math.pi * math.pow(radio, 2) * altura
    return volumen

def __main__():
    radio = float(input('Ingrese el radio del cilindro: '))
    altura = float(input('Ingrese la altura del cilindro: '))

    area = area_cilindro(radio, altura)
    volumen = volumen_cilindro(radio, altura)

    print(f'Área = {area:.2f}')
    print(f'Volumen = {volumen:.2f}')

__main__()