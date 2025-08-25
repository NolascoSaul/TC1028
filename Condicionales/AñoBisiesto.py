year = int(input("Ingrese un año: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} es un año bisiesto.")
else:
    print(f"{year} no es un año bisiesto.")