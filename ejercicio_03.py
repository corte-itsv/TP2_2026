notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]

def contar_aprobados(notas):
    aprobados = 0
    for nota in notas:
        if round(nota) >= 6:
            aprobados = aprobados + 1
    return aprobados

    
def contar_desaprobados(notas):
    desaprobados = 0
    for nota in notas:
        if round(nota) <= 5:
            desaprobados = desaprobados + 1
    return desaprobados

cant_aprobados = contar_aprobados(notas)
cant_desaprobados = contar_desaprobados(notas)

print(f"Total: {len(notas)}")
print(f"Aprobados: {cant_aprobados}")
print(f"Desaprobados: {cant_desaprobados}")