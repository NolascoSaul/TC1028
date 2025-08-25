while True:
    tiradaJuan = input("Turno de Juan, piedra (p), papel (a) o tijera (t): ")

    if len(tiradaJuan) > 1:
        print("Las tiradas deben ser un caracter.")
        continue

    if tiradaJuan not in ['p', 'a', 't']:
        print("Tirada incorrecta.")
        continue

    break

while True:
    tiradaAna = input("Turno de Ana, piedra (p), papel (a) o tijera (t): ")

    if len(tiradaAna) > 1:
        print("Las tiradas deben ser un caracter.")
        continue

    if tiradaAna not in ['p', 'a', 't']:
        print("Tirada incorrecta.")
        continue

    break

if tiradaJuan == tiradaAna:
    print("Empate.")
elif (tiradaJuan == 'p' and tiradaAna == 't') or (tiradaJuan == 't' and tiradaAna == 'a') or (tiradaJuan == 'a' and tiradaAna == 'p'):
    print("Juan gana.")
else:
    print("Ana gana.")