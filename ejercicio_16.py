def promedio(notas):
    return round(sum(notas) / len(notas), 2)



def condicion(promedio_alumno):
    if promedio_alumno >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"


def reporte_curso(curso):
    datos_alumnos = []
    for alumno, notas in curso.items():
        prom = promedio(notas)
        cond = condicion(prom)
        datos_alumnos.append((alumno, prom, cond))

    datos_alumnos.sort(key=lambda x: x[1], reverse=True)

    print("======================================")
    print("          REPORTE DEL CURSO")
    print("======================================")
    print(f"{'Alumno':<10} | {'Promedio':<8} | Condición")
    print("--------------------------------------")
    for alumno, prom, cond in datos_alumnos:
        print(f"{alumno:<10} |     {prom:.2f} | {cond}")
    print("======================================")

def resumen(curso):
    promedios = {}
    for alumno, notas in curso.items():
        promedios[alumno] = promedio(notas)

    promedio_general = round(sum(promedios.values()) / len(promedios), 2)
    mejor_alumno = max(promedios, key=promedios.get)
    peor_alumno = min(promedios, key=promedios.get)

    print(f"Promedio general del curso: {promedio_general:.2f}")
    print(f"Mejor promedio: {mejor_alumno} ({promedios[mejor_alumno]:.2f})")
    print(f"Peor promedio: {peor_alumno} ({promedios[peor_alumno]:.2f})")

curso = {
    "Ana": [9, 10, 8, 9, 7],
    "Luis": [6, 5, 7, 6, 4],
    "Sol": [10, 9, 10, 8, 9],
    "Marcos": [4, 5, 3, 6, 2],
    "Julia": [7, 8, 7, 9, 8],
    "Pedro": [5, 4, 6, 5, 3],
}
reporte_curso(curso)
resumen(curso)