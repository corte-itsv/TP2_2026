def clasificar_nota(nota):   
    
    if nota == 10:
        return("Perfecto")
    elif nota == 9 or nota == 8:
        return("Muy bueno")
    elif nota == 7 or nota == 6:
        return("Aprobado")
    elif nota == 5 or nota == 4:
        return("Desaprobado (cerca)")
    elif nota == 3 or nota == 2 or nota == 1:
        return("Desaprobado (lejos)")
    elif nota == 0:
        return("Nota no Valida")
    else:
        return("Nota no válida")


notas=[10, 7, 4, 0, 11]
for n in notas:
    resultado = clasificar_nota(n)
    print(f"{n} -> {resultado}")
