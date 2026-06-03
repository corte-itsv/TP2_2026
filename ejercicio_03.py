def contar_aprobados(notas):
    """Cuenta cuántas notas son mayores o iguales a 6"""
    cantidad = 0
    for nota in notas:
        if nota >= 6:
            cantidad += 1
    return cantidad


def contar_desaprobados(notas):
    """Cuenta cuántas notas son menores a 6"""
    cantidad = 0
    for nota in notas:
        if nota < 6:
            cantidad += 1
    return cantidad


# Pruebas con la lista de notas
notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]

aprobados = contar_aprobados(notas)
desaprobados = contar_desaprobados(notas)

print(f"Total: {len(notas)} alumnos")
print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")
