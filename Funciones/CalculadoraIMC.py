"""
    IMC = peso / altura^2
    Imprimir las siguientes etiquetas de acuerdo al IMC:
    - Bajo peso: menos de 18.5
    - Peso normal: más de 18.5 y hasta 25
    - Sobrepeso: más de 25 y hasta 30
    - Obesidad: 30 o más
"""


def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def __main__():
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")
    
    clasificacion = clasificar_imc(imc)
    print(f"Clasificación: {clasificacion}")

if __name__ == "__main__":
    __main__()