def clasificar_nota(nota):
    if nota == 10:
        print(f"{nota:<3}: ¡Perfecto!")
    elif nota >= 8 and nota <= 9:
        print(f"{nota:<}: Muy Bueno")
    elif nota >= 6 and nota <= 7:
        print(f"{nota:<3}: Aprobado")
    elif nota >= 4 and nota <= 5:
        print(f"{nota:<3}: Desaprobado (Cerca)")
    elif nota >= 1 and nota <= 3:
        print(f"{nota:<3}: Aprobado (Lejos)")
    else:
        print(f"{nota:<3}: Nota inválida. Ingrese una nota del 1 al 10")
    return

lista_de_notas = [10, 7, 4, 0, 11]


print("=== RENDIMIENTO ===")

for nota in lista_de_notas:
    condicion = clasificar_nota(nota)