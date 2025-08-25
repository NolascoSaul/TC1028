year = int(input("Ingrese un año: ")) 
month = int(input("Ingrese un mes: ")) 
day = int(input("Ingrese un día: ")) 

def getNextDay(year, month, day):
    day += 1

    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                day = 1
                month += 1
        else:   
            if day > 28:
                day = 1
                month += 1

        return year, month, day

    if month in [1, 3, 5, 7, 8, 10]:
        if day > 31:
            day = 1
            month += 1

    if month in [4, 6, 9, 11]:
        if day > 30:
            day = 1
            month += 1
        return year, month, day

    if month == 12:
        if day > 31:
            day = 1
            month = 1
            year += 1
        return year, month, day
    
    print("Fecha inválida.")

year, month, day = getNextDay(year, month, day)
print(f"La fecha del día siguiente es: {day}/{month}/{year}")