"""""
    Ejercicio 2
    Escribe una función llamada areaRect que reciba como parámetro el largo y ancho de un rectángulo y que regresa como valor de retorno el área del rectángulo.

    Escribe una función llamada perimetroRect que reciba como parámetro el largo y ancho de un rectángulo y que regresa como valor de retorno el perímetro del rectángulo.

    Observa que dentro de las funciones no mostrarás nada, solo regresarás el valor calculado usando return.

    Escribe ahora una función main que pregunte al usuario el largo y ancho del rectángulo y después pregunte si quiere calcular el área o el perímetro del rectángulo (pide una clave a para área y p para perímetro) y después muestre el valor correspondiente al cálculo que pidió el usuario.

    Entrada

    largo del rectángulo

    ancho del rectángulo

    clave que indica qué se quiere calcular a - área o p - perímetro

    Salida

    El área o el perímetro del rectángulo, de acuerdo con la clave que se haya tecleado
"""""

def area_rect(largo: float, ancho: float):
    return largo * ancho

def perimetro_rect(largo: float, ancho: float):
    return 2 * (largo + ancho) 

def __main__():
    largo = float(input('Ingrese el largo del rectángulo: '))
    ancho = float(input('Ingrese el ancho del rectángulo: '))

    print("MENÚ DE OPCIONES:")
    print("- Calcular el perímetro del rectángulo")
    print("- Calcular el área del rectángulo")
    opcion = input("Seleccione una opción (a/p): ")

    if opcion == "a":
        print(f"El área del rectángulo es: {area_rect(largo, ancho)}")
    elif opcion == "p":
        print(f"El perímetro del rectángulo es: {perimetro_rect(largo, ancho)}")
    else:
        print("Opción no válida")

__main__()