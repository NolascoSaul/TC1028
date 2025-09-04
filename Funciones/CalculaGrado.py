def calcula_grado(score: float) -> str:
    if score > 0.9:
        return 'A'
    if score > 0.8:
        return 'B'
    if score > 0.7:
        return 'C'
    if score > 0.6:
        return 'D'
    
    return 'F'

def es_calificacion(score: float) -> bool: 
    if(score < 0 or score > 1):
        return False
    
    return True

def __main__():
    score = float(input('Ingrese el puntaje que obtuvo: '))
    nota = calcula_grado(score)
    
    if(not es_calificacion(score)):
        print("No es una calificación válida (0 - 1)")
        return

    print(f'Usted obtuvo una {nota}')

if __name__ == '__main__':
    __main__()
