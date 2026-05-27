def contar_aprobados(Notas):
    aprobados = 0
    for nota in Notas:
        if nota >= 6:
            aprobados += 1
    return aprobados

def contar_desaprobados(Notas):
    desaprobados = 0
    for nota in Notas:
        if nota < 6:
            desaprobados += 1
    return desaprobados

Notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]

aprobados = contar_aprobados(Notas)
desaprobados = contar_desaprobados(Notas)

print(f"Total: {len(Notas)} alumnos")
print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")
