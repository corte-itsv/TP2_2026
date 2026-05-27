def contar_aprobados(notas):
    notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]
    aprobados = 0
    for nota in notas:
        if nota >= 6:
            aprobados += 1
    return aprobados

def contar_desaprobados(notas):
    notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]
    desaprobados = 0
    for nota in notas:
        if nota < 6:
            desaprobados += 1
    return desaprobados
alumnos = 10


print("Alumnos", alumnos)
print("Aprobados:", contar_aprobados(alumnos))
print("Desaprobados:", contar_desaprobados(alumnos))



