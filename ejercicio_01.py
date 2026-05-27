def clasificar_notas(nota):
    if nota == 10:
        return("Perfecto")
    elif nota == 9 or nota == 8:
        return("Muy bueno")
    elif nota == 7 or nota == 6:
        return("Aprobado")
    elif nota == 5 or nota == 4:
        return("Desaprobado (cerca)")
    elif nota == 1 or nota == 2 or nota == 3:
        return("Desaprobado (lejos)")
    else:
        return("Nota inválda")
clasificar_notas

for nota in [10, 7, 4, 0, 11]:
    print(f"{nota} = {clasificar_notas(nota)}")