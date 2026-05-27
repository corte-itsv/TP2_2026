def clasificar_nota(nota):
    if nota == 10:
        return "Perfecto"
    if 10 > nota >= 8:
        return "Muy bueno"
    if 8 > nota >= 6:
        return "Aprobado"
    if 6 > nota >= 4:
        return "Desaprobado (cerca)"
    if 4 > nota >= 1:
        return "Desaprobado (lejos)"
    else:
        return "Nota inválida"


print(clasificar_nota(10))
print(clasificar_nota(7))
print(clasificar_nota(4))
print(clasificar_nota(0))
print(clasificar_nota(11))