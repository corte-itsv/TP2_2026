def clasificar_nota(nota):
    if nota == 10:
        return "Perfecto"
    elif nota in [8, 9]:
        return "Muy bueno"
    elif nota in [6, 7]:
        return "Aprobado"
    elif nota in [5, 4]:
        return "Desaprobado (cerca)"
    elif nota in [3, 2, 1]:
        return "Desaprobado (lejos)"
    else:
        return "Nota Inválida"

notas_prueba  = [10, 7, 4, 0, 11]

for n in notas_prueba:
    resultado = clasificar_nota(n)
    print(f"{n} -> {resultado}")