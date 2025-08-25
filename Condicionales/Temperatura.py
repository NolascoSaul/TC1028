temperatura = float(input("Ingrese la temperatura en °C: "))

if temperatura < 10:
    print("Hace frío")
elif temperatura <= 20:
    print("Está templado.")
elif temperatura < 30:
    print("Está caliente.")
else:
    print("Está muy caliente.")