def promedio(notas):
    promedio_redondeado_dos_dcimales = 0
    suma_total = 0
    for nota in notas:
        suma_total = suma_total + nota
    promedio = suma_total / len(notas)
    promedio_redondeado_dos_dcimales = round(promedio, 2)
    return promedio_redondeado_dos_dcimales

def condicion(promedio):
    if promedio >= 6:
        return "Aprobado"
    return "Desaprobado"
        
def reporte_curso(curso):
    for nombre, notas in curso.items():
        promedio_del_alumno = promedio(notas)
        condicion_de_alumno = condicion(promedio_del_alumno)
        print(nombre, "     |     ", promedio_del_alumno, "     |     ", condicion_de_alumno)
    
def promedio_general_del_curso(curso):
    array_de_promedios = []
    for nombre, notas in curso.items():
        promedio_del_alumno = promedio(notas)
        array_de_promedios.append(promedio_del_alumno)
    promedio_general_del_curso = promedio(array_de_promedios)
    return promedio_general_del_curso

def mejor_promedio(curso):
    mejor_promedio = 0
    for nombre, notas in curso.items():
        promedio_del_alumno = promedio(notas)
        if promedio_del_alumno > mejor_promedio:
            mejor_promedio = promedio_del_alumno
    return mejor_promedio

def peor_promedio(curso):
    peor_promedio = 10
    for nombre, notas in curso.items():
        promedio_del_alumno = promedio(notas)
        if promedio_del_alumno < peor_promedio:
            peor_promedio = promedio_del_alumno
    return peor_promedio


curso = {
    "Ana":     [9, 10, 8, 9, 7],
    "Luis":    [6,  5, 7, 6, 4],
    "Sol":     [10, 9, 10, 8, 9],
    "Marcos":  [4,  5, 3, 6, 2],
    "Julia":   [7,  8, 7, 9, 8],
    "Pedro":   [5,  4, 6, 5, 3],
}


print("======================================")
print("          REPORTE DEL CURSO          ")
print("======================================")
print("Alumno     | Promedio | Condición")
print("--------------------------------------")
reporte_curso(curso)
print("======================================")
promedio_final_del_curso = promedio_general_del_curso(curso)
print("Promedio general del curso: ", promedio_final_del_curso)
mejor_promedio_del_curso = mejor_promedio(curso)
print("Mejor promedio: ", mejor_promedio_del_curso)
peor_promedio_del_curso = peor_promedio(curso)
print("Peor promedio: ", peor_promedio_del_curso)