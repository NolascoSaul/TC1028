def binario_decimal(binario : str) -> int:
    if(not es_binario(binario)):
       return -1
    
    decimal = 0
    i = 0
    j = len(binario) - 1
    while i < len(binario):
        decimal += int(binario[i]) * (2 ** j)
        i += 1
        j -= 1

    return decimal

def es_binario(binario : str) -> bool:
    if(len(binario) == 0):
        return False
    
    for char in binario: 
        if char != '0' and char != '1':
            return False
        
    return True

def __main__():
    binario = input('Ingrese el número binario a convertir: ')
    decimal = binario_decimal(binario)

    if(decimal == -1):
        print('El número ingresado no es binario')
    else:
        print(f'El número en decimal es: {decimal}')

if __name__ == '__main__':
    __main__()