print("Nota:")
nota = int (input())
def clasificar_nota(nota):
    if nota == 10:
        return "Aprobado"
    elif nota >= 8 or nota == 9:
        return "Muy bueno"
    elif nota == 6 or nota == 7:
        return "Aprobado"
    elif nota == 4 or nota == 5:
        return "Desaprobado (cerca)"
    elif nota == 1 or nota == 2 or nota == 3:
        return "Desaprobado (lejos)"
    else :
        print("Nota inválida")

print(clasificar_nota(nota))