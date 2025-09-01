""" Escribe un programa que convierta pies, pulgadas y yardas a centímetros, para lo cual debes definir 3 funciones:

Función que reciba una cantidad de pies (entero positivo) y devuelva el equivalente a centímetros.
Función que reciba una cantidad de pulgadas (entero positivo) y devuelva el equivalente a centímetros.
Función que reciba una cantidad de yardas (entero positivo) y devuelva el equivalente en centímetros.
Entrada:

La opción a ejecutar (1 – pies a cm, 2 - pulgadas a cm, 3 – yardas a cm).

Un valor entero positivo que corresponde a la cantidad en la medida de acuerdo con la opción tecleada (sólo el número).

Salida

La cantidad equivalente en centímetros (sólo el número).

En caso de que el número de opción sea diferente a 1, 2, o 3 se desplegará el mensaje: Error.

En caso de que el valor a convertir sea 0 o menor se desplegará el mensaje: Error """

def ft_to_cm(ft: int):
    return ft * 30.48

def inch_to_cm(inch: int):
    return inch * 2.54

def yard_to_cm(yard: int):
    return yard * 91.44

def __main__():
    print("Menú de opciones (Ingrese el número de opción de lo que desea hacer):")
    print("1. Convertir pies a centímetros.")
    print("2. Convertir pulgadas a centímetros.")
    print("3. Convertir yardas a centímetros.")

    opcion = int(input("Ingrese su opción: "))
    valor = int(input("Ingrese el valor a convertir: "))

    if opcion == 1:
        resultado = ft_to_cm(valor)
    elif opcion == 2:
        resultado = inch_to_cm(valor)
    elif opcion == 3:
        resultado = yard_to_cm(valor)
    else:
        print("Error.")
        return

    if valor <= 0:
        print("Error.")
    else:
        print(f"Resultado: {resultado} cm")

__main__()