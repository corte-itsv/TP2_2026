def clasificar_nota(nota):
    if nota==10:
        return "Perfecto"
    elif nota == 8 or nota == 9:
        return "Muy bueno"
    elif nota == 7 or nota == 6:
        return "Aprobado"
    elif nota == 5 or nota == 4:
        return "Desaprobado (cerca)"
    elif nota == 3 or nota == 2 or nota == 1:
        return "Desaprobado (lejos)"
    else:
        return "Nota inválida"
print("10 →" , clasificar_nota(10))
print("7 →" , clasificar_nota(7))
print("4 →" , clasificar_nota(4))
print("0 →" , clasificar_nota(0))
print("11 →" , clasificar_nota(11))