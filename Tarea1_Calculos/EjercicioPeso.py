def __main__():
    print("Ingrese su peso actual:")
    peso_inicial = float(input())

    print("Ingrese el peso al que quiere llegar:")
    peso_final = float(input())

    print("Ingrese el tiempo en meses que tiene para lograrlo:")
    meses = int(input())

    cambio_peso = abs(peso_final - peso_inicial)
    peso_mensual = cambio_peso / meses

    print(f"Para llegar a {peso_final} kg en {meses} meses, debe bajar {peso_mensual} kg por mes.")

__main__()