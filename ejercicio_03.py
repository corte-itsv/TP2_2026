
def contar_aprobados(notas):
    Cantidad = 0
    for nota in notas:
        if nota >= 6:
            Cantidad += 1
    return Cantidad
    
def contar_desaprobados(notas):
    cantidad = 0
    for nota in notas:
        if nota < 6:
            cantidad += 1
    return cantidad

notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]

print("Total:", len(notas), "Alumnos")
print("Aprobados:", contar_aprobados(notas), "Alumnos Aprobados")
print("Desaprobados:", contar_desaprobados(notas), "Alumnos Desaprobados")