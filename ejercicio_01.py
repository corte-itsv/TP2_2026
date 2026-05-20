def clasificar_nota(nota):
    if nota == 10:
        print("Perfecto")
    elif nota in [9, 8]:
        print("Muy bueno")
    elif nota in [7, 6]:
        print("Aprobado")
    elif nota in [5, 4]:
        print("Desaprobado (cerca)")
    elif nota in [3, 2, 1]:
        print("Desaprobado (lejos)")
    else:
        print("nota invalida")
nota = int(input("Introduci tu nota"))
clasificar_nota(nota)
