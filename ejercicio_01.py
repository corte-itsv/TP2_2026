def clasificar(nota):
    if nota > 10 or nota < 0:
        print(f"{nota}->Nota Invalida")
    elif nota == 10:
        print(f"{nota}->Perfecto")
    elif nota >= 8:
        print(f"{nota}->Muy Bueno")
    elif nota >= 6:
        print(f"{nota}->Aprobado")
    elif nota >= 4:
        print(f"{nota}->Desaprobado (cerca)")
    else:
        print(f"{nota}->Desaprobado (lejos)")

clasificar(10)
clasificar(7)
clasificar(4)
clasificar(0)
clasificar(11)