def contar_aprobados(notas):
    cantidad = 0
    for nota in notas:
        if nota >= 6:
            cantidad += 1
    return cantidad


def contar_desaprobados(notas):
    cantidad = 0
    for nota in notas:
        if nota < 6:
            cantidad += 1
    return cantidad

notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]

print("Total:", len(notas), "alumnos")
print("Aprobados:", contar_aprobados(notas), "alumnos ")
print("Desaprobados:", contar_desaprobados(notas), "alumnos")