def calcular_promedio(lista_de_notas):
    promedio_final = 0
    numero_gordo_creciente = 0
    for nota in lista_de_notas:
        numero_gordo_creciente = numero_gordo_creciente + nota
    promedio_final = numero_gordo_creciente / len(lista_de_notas)
    return promedio_final

def calcular_promedios_del_curso(curso):
    promedios_de_curso = {}
    for nombre, notas in curso.items():
        promedio_de_alumno = calcular_promedio(notas)
        promedios_de_curso[nombre] = promedio_de_alumno
    return promedios_de_curso

def alumno_destacado(dic_nombres_y_promedios):
    alumno_con_promedio_mas_alto = ""
    promedio_mas_alto = 0
    for nombre_del_alumno, promedio_de_alumno in dic_nombres_y_promedios.items():
        if promedio_de_alumno > promedio_mas_alto:
            promedio_mas_alto = promedio_de_alumno
            alumno_con_promedio_mas_alto = nombre_del_alumno
    return alumno_con_promedio_mas_alto

def alumnos_aprobados(dic_nombres_y_promedios):
    alumnos_aprobados = []
    for nombre_del_alumno, promedio_de_alumno in dic_nombres_y_promedios.items():
        if promedio_de_alumno >= 6:
            alumnos_aprobados.append(nombre_del_alumno)
    return alumnos_aprobados



array_de_notas = [8, 10, 5, 7, 9]

curso = {
    "Ana":     [9, 10, 8, 9],
    "Luis":    [6,  5, 7, 6],
    "Sol":     [10, 9, 10, 8],
    "Marcos":  [4,  5, 3, 6],
    "Julia":   [7,  8, 7, 9],
}


promedios_del_curso = calcular_promedios_del_curso(curso)
print("Promedios: ", promedios_del_curso)

mejor_alumno = alumno_destacado(promedios_del_curso)
print("Alumno destacado: ", mejor_alumno)

alumnos_aprobados = alumnos_aprobados(promedios_del_curso)
print("Aprobados: ", alumnos_aprobados)