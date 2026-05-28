def clasificar_nota(nota):
    if nota == 10:
        print("Excelente")
    elif nota in [9, 8]:
        print("Muy bueno")
    elif nota in [7, 6]:
        print("aprobado")
    elif nota in [5, 4]:
        print("desaprobado (cerca)")
    elif nota in [3, 2, 1]:
        print("desaprobado (lejos)")
    else:
        print("nota invalida")
nota = int(input("Introducí tu nota: "))
clasificar_nota(nota)