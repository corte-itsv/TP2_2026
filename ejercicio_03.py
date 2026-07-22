def contar_alumnos(notas):
    cantidad_de_alumnos = 0
    for nota in notas:
        cantidad_de_alumnos = cantidad_de_alumnos + 1
    return cantidad_de_alumnos

def contar_aprobados(notas):
    cantidad_de_notas_aprobadas = 0
    for nota in notas:
        if nota >= 6:
            cantidad_de_notas_aprobadas = cantidad_de_notas_aprobadas + 1
    return cantidad_de_notas_aprobadas

def contar_desaprobados(notas):
    cantidad_de_notas_desaprobadas = 0
    cantidad_de_numeros_que_no_son_notas = 0
    for nota in notas:
        if nota < 6 and nota >= 0:
            cantidad_de_notas_desaprobadas = cantidad_de_notas_desaprobadas + 1
    return cantidad_de_notas_desaprobadas


notas = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]


print("=== RESULTADOS ===")

cantidad_de_alumnos = contar_alumnos(notas)
print("Total", cantidad_de_alumnos, "alumnos.")

aprobados = contar_aprobados(notas)
print(f"Aprovados: {aprobados:>4}")

desaprobados = contar_desaprobados(notas)
print(f"Desaprobados: {desaprobados}")
