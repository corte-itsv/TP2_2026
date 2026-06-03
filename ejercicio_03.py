def contar_aprobados(notas):
    nota = 0
    aprobados = 0
    cant = 0
    for nota in notas:
        cant += 1
        if nota >= 6:
            aprobados += 1
    return aprobados
    
def contar_desaprobados(notas):
    nota = 0
    desaprobados = 0
    for nota in notas:
        if nota < 6:
            desaprobados += 1
    return desaprobados
    

notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]

contar_desaprobados(notas)
contar_aprobados(notas)

print(f"Total: {contar_aprobados(notas)+contar_desaprobados(notas)}")
print(f"Aprobados: {contar_aprobados(notas)}")
print(f"Desaprobados: {contar_desaprobados(notas)}")
