def clasificar_nota(nota):

    if nota < 0 or nota > 10:
        return "Nota Invalida"
    elif nota == 10:
        return "Perfecto"
    elif nota == 9 or nota == 8:
        return "Muy bueno"
    elif nota == 7 or nota == 6:
        return "Aprobado"
    elif nota == 5 or nota == 4:
        return "Desaprobado (cerca)"
    elif nota == 3 or nota == 2 or nota == 1:
        return "Desaprobado (lejos)"
    else:  # nota == 0
        return "Desaprobado (lejos)"


notas = [10, 7, 4, 0, 11]

for n in notas:
    resultado = clasificar_nota(n)
    print(f"{n} -> {resultado}")
    
