def contar_aprobados(notas):
    aprobados = 0
    for nota in notas:
        if nota >= 6:
            aprobados += 1
    return aprobados

def contar_desaprobados(notas):
    desaprobados = 0
    for nota in notas:
        if nota < 6:
            desaprobados += 1
    return desaprobados

notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]
print("Cantidad de aprobados:", contar_aprobados(notas))
print("Cantidad de desaprobados:", contar_desaprobados(notas))
