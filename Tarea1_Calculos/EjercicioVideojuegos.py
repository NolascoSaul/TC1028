PRECIO_JUEGO_USADO = 350
PRECIO_JUEGO_NUEVO = 1000

def __main__():
    print("Ingrese la cantidad de juegos nuevos para comprar")
    juegos_nuevos = int(input())
    print("Ingrese la cantidad de juegos usados para comprar")
    juegos_usados = int(input())
    
    total_nuevos = juegos_nuevos * PRECIO_JUEGO_NUEVO
    total_usados = juegos_usados * PRECIO_JUEGO_USADO

    precio_total = total_nuevos + total_usados

    print(f"El precio total de los juegos es {precio_total}")
    

__main__()