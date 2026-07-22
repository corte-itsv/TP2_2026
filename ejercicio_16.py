def promedio(notas):
    promedio_del_alumno = 0
    suma_total = 0
    for nota in notas:
        suma_total = suma_total + nota
    promedio_del_alumno = suma_total / len(notas)
    promedio_final = round(promedio_del_alumno, 2)
    return promedio_final

def condicion(promedio):
    condicion_final = "Desaprobado"
    if promedio >= 6:
        condicion_final = "Aprobado"
    return condicion_final

def obtener_promedio_mas_alto(curso):
    promedio_mas_alto = 0
    alumno_con_promedio_mas_alto = ""
    lista_de_promedios = []
    for alumno, notas in curso.items():
        promedio_de_alumno = promedio(notas)
        lista_de_promedios.append((alumno, promedio_de_alumno))
    for (alumno, promedio_de_alumno) in lista_de_promedios:
        if promedio_de_alumno >= promedio_mas_alto:
            promedio_mas_alto = promedio_de_alumno
            alumno_con_promedio_mas_alto = alumno 
    return (alumno_con_promedio_mas_alto, promedio_mas_alto)

def reporte_curso(curso):
    copia_de_curso = curso.copy()
    promedios_de_mayor_a_menor = []
    while len(copia_de_curso) > 0:
        alumno, promedio_mas_alto = obtener_promedio_mas_alto(copia_de_curso)
        condicion_de_promedio = condicion(promedio_mas_alto)
        promedios_de_mayor_a_menor.append((alumno, promedio_mas_alto, condicion_de_promedio))
        del copia_de_curso[alumno]
    for (alumno, promedio_mas_alto, condicion_de_promedio) in promedios_de_mayor_a_menor:
            print(f"{alumno:<10} | {promedio_mas_alto:>8.2f} | {condicion_de_promedio}")
    return promedios_de_mayor_a_menor

def resumen(curso):
    promedio_general = 0
    promedio_del_mejor_alumno = 0
    alumno_con_mejor_promedio = ""
    promedio_del_peor_alumno = 0
    alumno_con_peor_promedio = ""
    curso_reportado = reporte_curso(curso)
    array_de_promedios = []
    tamaño_de_array = len(array_de_promedios)
    posicion_final = tamaño_de_array - 1
    suma_total = 0
    for (alumno, promedio_del_alumno, condicion_alumno) in curso_reportado:
        suma_total = suma_total + promedio_del_alumno
        array_de_promedios.append(promedio_del_alumno)
        if promedio_del_alumno == array_de_promedios[0]:
            promedio_del_mejor_alumno = promedio_del_alumno
            alumno_con_mejor_promedio = alumno
        elif promedio_del_alumno == array_de_promedios[posicion_final]:
            promedio_del_peor_alumno = promedio_del_alumno
            alumno_con_peor_promedio = alumno
    promedio_general = suma_total / len(curso_reportado)
    promedio_final = round(promedio_general, 2)
    return (promedio_final, alumno_con_mejor_promedio, promedio_del_mejor_alumno, promedio_del_peor_alumno, alumno_con_peor_promedio)
    


curso = {
    "Ana":     [9, 10, 8, 9, 7],
    "Luis":    [6,  5, 7, 6, 4],
    "Sol":     [10, 9, 10, 8, 9],
    "Marcos":  [4,  5, 3, 6, 2],
    "Julia":   [7,  8, 7, 9, 8],
    "Pedro":   [5,  4, 6, 5, 3],
}


print("======================================")
print("          REPORTE DEL CURSO")
print("======================================")
print(f"{'Alumno':<10} | {'Promedio':>8} | Condición")
print("--------------------------------------")
promedio_general, alumno_con_mejor_promedio, promedio_del_mejor_alumno, promedio_del_peor_alumno, alumno_con_peor_promedio = resumen(curso)
print("======================================")
print(f"Promedio general del curso: {promedio_general:.2f}")
print(f"Mejor promedio: {alumno_con_mejor_promedio} ({promedio_del_mejor_alumno:.2f})")
print(f"Peor promedio: {alumno_con_peor_promedio} ({promedio_del_peor_alumno:.2f})")