
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



notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]

total = len(notas)
print("Total:", total,"alumnos")

aprobados = contar_aprobados(notas)
desaprobados = contar_desaprobados(notas)

print("Aprobados:", aprobados)
print("Desaprobados:", desaprobados)
