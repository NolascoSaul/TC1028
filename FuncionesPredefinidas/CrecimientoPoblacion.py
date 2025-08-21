"""
    Entrada
    Tres números recibidos uno en cada renglón, correspondientes a: población inicial (entero positivo), tiempo en años (entero positivo) y tasa de crecimiento (flotante entre 0 y 1), en ese orden.

    Salida
    Un número entero, resultado del cálculo de la población final. IMPORTANTE: Trunca los decimales del número resultante, para que el resultado sea entero (¿Cuál es la función de la librería math de Python que te puede ayudar a truncar los decimales?).
"""
import math 
a = int(input("Ingresa la población incial: "))
tiempoAños =int(input("Ingresa el tiempo en años: "))
tasaCrecimineto = float(input("Ingresa la tasa de crecimiento (número entre 0 y 1): "))

poblacion = a * (math.pow(math.e, tasaCrecimineto * tiempoAños))

# print(round(poblacion))
print(math.trunc(poblacion))