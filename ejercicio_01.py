
def clasificar_nota(nota):
    if nota == 10:
        return "Perfecto"
    elif nota == 9 or nota == 8:
        return "Muy bueno"
    elif nota == 7 or nota == 6:
        return "Aprobado"
    elif nota == 5 or nota == 4:
        return "Desaprobado (cerca)"
    elif nota == 3 or nota == 2 or nota == 1:
        return "Desaprobado (lejos)"
    else:
        return "Nota inválida"

#10, 7, 4, 0 y 11

print(clasificar_nota(10))
print(clasificar_nota(7))
print(clasificar_nota(4))
print(clasificar_nota(0))
print(clasificar_nota(11))