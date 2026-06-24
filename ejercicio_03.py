def contar_aprobados(notas):
    cantidad_num_mayor_o_igual_6 = 0
    for nota in notas:
        if nota >= 6:
            cantidad_num_mayor_o_igual_6 = cantidad_num_mayor_o_igual_6 + 1 
    return cantidad_num_mayor_o_igual_6

def contar_desaprobados(notas):
    cantidad_num_menores_6 = 0
    for nota in notas:
        if nota < 6:
            cantidad_num_menores_6 = cantidad_num_menores_6 + 1
    return cantidad_num_menores_6


notas_benja = [8, 3, 6, 10, 4, 7, 5, 9, 6, 2]

total_de_alumnos = len(notas_benja) 

print("Total: ", total_de_alumnos, "alumnos")
cant_notas_aprovadas_benja = contar_aprobados(notas_benja)
print("Aprobadas: ", cant_notas_aprovadas_benja)

cant_notas_desaprobadas_benja = contar_desaprobados(notas_benja)
print("Desaprobadas: ", cant_notas_desaprobadas_benja)




def saldo_creditos(personas):
    creditos_totales = 10
    for persona in personas:
        if persona == "Lucas":
            creditos_totales = creditos_totales - 1
    return creditos_totales

lista_de_nombre = ["Lucas", "Benja", "Tomi", "Lucas"]

saldo_final = saldo_creditos(lista_de_nombre)
print("Saldo actualizado: ", saldo_final)