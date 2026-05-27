print("Escribe la nota:")
nota = int(input())

def clasificar_nota(nota): 
    if nota == 10 :
        return "Perfecto"
    elif nota == 9 or nota == 8 :
        return "Muy bueno"
    elif nota == 7 or nota == 6:
        return "Aprobado"
    elif nota == 5 or nota == 4:
        return "Desaprobado (cerca)"
    elif nota == 3 or nota == 2 or nota == 1:
        return "Desaprobado (lejos)"
    else :
        return "nota invalida"

print(clasificar_nota(nota))