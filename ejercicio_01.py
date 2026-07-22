def clasificar_nota(nota):
        if nota == 10:
            return "Perfecto"
        elif nota in [9, 8]:
            return "Muy bueno"
        elif nota in [7, 6]:
            return "Aprobado"
        elif nota in [5, 4]:
            return "Desaprobado (cerca)"
        elif nota in [3, 2, 1]:
            return "Desaprobado (lejos)"
        else:
            return "Nota inválida"

notas = [10,7,4,0,11]
for nota in notas:
    print(f"{nota} → {clasificar_nota(nota)}")

    