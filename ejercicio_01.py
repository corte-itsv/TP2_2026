def clasificar_nota(nota):
    if nota == 10:
        return "Perfecto"
    elif nota == 8 or nota == 9:
        return "Muy bueno"
    elif nota == 6 or nota == 7:
        return "Aprobado"
    elif nota == 4 or nota == 5:
        return "Desaprobado (cerca)"
    elif nota in [1, 2, 3]:
        return "Desaprobado (lejos)"
    else:
        return "Nota inválida"

notas = [10, 7, 4, 0, 11]

for nota in notas:
    print(f"{nota} → {clasificar_nota(nota)}")
