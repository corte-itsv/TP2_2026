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

# Pruebas
notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]
print(f"Total: {len(notas)} alumnos")
print(f"Aprobados: {contar_aprobados(notas)}")
print(f"Desaprobados: {contar_desaprobados(notas)}")