def calcular_mayor(a,b,c):
    if a >= b and a >= c:
        return a
    
    if b >= a and b >= c:
        return b
    
    if c >= a and c >= b:
        return c
    
def __main__():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    
    mayor = calcular_mayor(a,b,c)
    print(f"El mayor de los tres números es: {mayor}")

if __name__ == "__main__":
    __main__()