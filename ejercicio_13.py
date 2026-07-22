def calcular_promedios(curso):
    promedios_por_alumno_del_curso = {}
    suma_total = 0
    for alumno, notas in curso.items():
        for nota in notas:
            suma_total = suma_total + nota
        promedio_del_alumno = suma_total / len(notas)
        promedios_por_alumno_del_curso[alumno] = promedio_del_alumno
        suma_total = 0
    return promedios_por_alumno_del_curso

def alumno_destacado(promedios):
    mejor_alumno = ""
    promedio_del_mejor_alumno = 0
    for alumno, promedio in promedios.items():
        if promedio >= promedio_del_mejor_alumno:
            promedio_del_mejor_alumno = promedio
            mejor_alumno = alumno
    return (mejor_alumno, promedio_del_mejor_alumno)
            
def alumnos_aprobados(promedios):
    lista_con_aprobados = []
    for alumno, promedio in promedios.items():
        if promedio >= 6:
            lista_con_aprobados.append(alumno)
    return lista_con_aprobados





curso = {
    "Ana":     [9, 10, 8, 9],
    "Luis":    [6,  5, 7, 6],
    "Sol":     [10, 9, 10, 8],
    "Marcos":  [4,  5, 3, 6],
    "Julia":   [7,  8, 7, 9],
}

print("===== RENDIMIENTO ESCOLAR =====")

promedios_calculados = calcular_promedios(curso)
print("Promedios:", promedios_calculados)
print("")

mejor_alumno, promedio_del_mejor_alumno = alumno_destacado(promedios_calculados)
print("Alumno destacado:", mejor_alumno, "(", promedio_del_mejor_alumno, ")")
print("")

aprobados = alumnos_aprobados(promedios_calculados)
print("Aprovados:", aprobados)