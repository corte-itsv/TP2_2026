def contar_aprobados(notas):
    aprobados = 0
    for nota in notas: 
        if nota >= 6:
            aprobados = aprobados + 1
    return aprobados

def contar_desaprobados(notas):
    desaprobados = 0
    for nota in notas: 
        if nota < 6:
            desaprobados = desaprobados + 1
    return desaprobados
notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]
cant_aprobados = contar_aprobados(notas)
print(f"Total: {len(notas)} alumnos")
print(f"Aprobados: {cant_aprobados}")
cant_desaprobados = contar_desaprobados(notas)
print(f"Desaprobados: {cant_desaprobados}")

