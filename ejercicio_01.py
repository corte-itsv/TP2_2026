def clasificar_nota(nota):
    if nota > 10 or nota <= 0:
        return "Nota inválida"
    elif nota == 10:
        return "Perfecto"
    elif nota >= 8:
        return "Muy bueno"
    elif nota >= 6:
        return "Aprobado"
    elif nota >= 4:
        return "Desaprobado (cerca)"
    else:
        return "Desaprobado (lejos)"
nota = 10
print(f"{nota} → {clasificar_nota(nota)}")
nota = 7
print(f"{nota} → {clasificar_nota(nota)}")
nota = 4
print(f"{nota} → {clasificar_nota(nota)}")
nota = 0
print(f"{nota} → {clasificar_nota(nota)}")
nota = 11
print(f"{nota} → {clasificar_nota(nota)}")