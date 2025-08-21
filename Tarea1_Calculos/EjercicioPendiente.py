def __main__():
    print("Ingrese la coordenada x del punto 1 (x1):")
    x1 = float(input())
    print("Ingrese la coordenada y del punto 1 (y1):")
    y1 = float(input())
    print("Ingrese la coordenada x del punto 2 (x2):")
    x2 = float(input())
    print("Ingrese la coordenada y del punto 2 (y2):")
    y2 = float(input())

    diferenciaX = x2 - x1
    diferenciaY = y2 - y1
    if diferenciaX == 0:
        print("No se puede calcular la pendiente.")
    else:
        pendiente = diferenciaY / diferenciaX
        print(f"La pendiente de la línea es: {pendiente}")

__main__()