
def clasificar_nota(nota):
    if nota == 10:
        print("Perfecto")
    elif nota == 9 or nota == 8:
        print("Muy bueno")
    elif nota == 7 or nota == 6:
        print("Aprobado")
    elif nota == 5 or nota == 4:
        print('desaprobado (cerca)')
    elif nota == 3 or nota == 2:
        print('Desaprobado (lejos)')
    elif nota == 1:
        print('Desaprobado (lejos)')
    else:
        print('Nota invalida')
    

#10, 7, 4, 0 y 11
    
clasificar_nota(10)
clasificar_nota(7)
clasificar_nota(4)
clasificar_nota(0)
clasificar_nota(11)