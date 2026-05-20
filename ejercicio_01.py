def clasificar_nota(nota):
    if nota == 10:
        return 'Perfecto'
    elif nota == 9 or nota == 8:
        return 'Muy Bueno'
    elif nota == 6 or nota == 7:
        return 'Aprobado'
    elif nota == [4, 5]:
        return 'Desaprobado (cerca)'
    elif nota == [1, 2, 3]:
        return 'Desaprobado (lejos)'
    else:
        return 'Nota Invalida'
    
notas = [10, 7, 4, 0, 11]
for nota in notas:
    print(f"{nota} = {clasificar_nota(nota)}")
