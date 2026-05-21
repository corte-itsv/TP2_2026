def clasificar_nota(nota):
    if nota == 10:
        return "Perfecto"
    elif nota in [9, 8]:
        return "Muy bueno"
    elif nota in [7, 6]:
        return "aprobado"
    elif nota in [5, 4]:
        return "desaprobado (cerca)"
    elif nota in [3, 2, 1]:
        return "desaprobado (lejos)"
    else:
        return("nota invalida")
nota = int(input("Introducí tu nota: "))
clasificar_nota(nota)
print(clasificar_nota(nota))

    