def contar_aprobados(notas):
    contador = 0
    
    for nota in notas:
        if nota >= 6:
            contador += 1
    
    return contador


def contar_desaprobados(notas):
    contador = 0
    
    for nota in notas:
        if nota < 6:
            contador += 1
    
    return contador


# Lista de notas
notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]

# Pruebas
print("Aprobados:", contar_aprobados(notas))
print("Desaprobados:", contar_desaprobados(notas))