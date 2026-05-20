def clasificar_nota(nota):
    if nota==10:
        return "Perfecto"
    elif nota == 8 or nota == 9:
        return "Muy Bueno"
    elif nota == 7 or nota == 6:
        return "aprobado"
    elif nota == 5 or nota == 4:
        return "Desaprobado (Cerca)"
    elif nota == 3 or nota == 2 or nota == 1:
        return "Desaprobado (Lejos)"
    else:
        return "Nota invalida"
print("10 →" , clasificar_nota(10))
print("7 →" , clasificar_nota(7))
print("4 →" , clasificar_nota(4))
print("0 →" , clasificar_nota(0))
print("11 →" , clasificar_nota(11))