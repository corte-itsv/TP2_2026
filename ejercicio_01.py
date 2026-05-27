def clasificar_nota(nota):
    if nota == 10:
        return "Perfecto"
    elif nota == 8 or nota == 9:
        return "Muy bueno"
    elif nota == 6 or nota == 7:
        return "Aprobado"
    elif nota == 4 or nota == 5:
        return "Desaprobado (cerca)"
    elif nota >= 1 and nota <= 3:
        return "Desaprobado (lejos)"
    else:
        return "Nota inválida"


# Llamadas a la función
notas = [10, 7, 4, 0, 11]

for n in notas:
    print(f"{n} → {clasificar_nota(n)}")