curso = {
    "Ana":     [9, 10, 8, 9, 7],
    "Luis":    [6,  5, 7, 6, 4],
    "Sol":     [10, 9, 10, 8, 9],
    "Marcos":  [4,  5, 3, 6, 2],
    "Julia":   [7,  8, 7, 9, 8],
    "Pedro":   [5,  4, 6, 5, 3],
}

def promedio(notas):
    return round(sum(notas) / len(notas), 2)

def condicion(promedio):
    if promedio >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"

def reporte_curso(curso):
    for alumno, notas in sorted(curso.items()):
        prom = promedio(notas)
        estado = condicion(prom)
        print(alumno, prom, estado)

def resumen(curso):
    promedios = {}

    for alumno, notas in curso.items():
        promedios[alumno] = promedio(notas)

    prom_general = round(sum(promedios.values()) / len(promedios), 2)

    mejor_alumno = max(promedios, key=promedios.get)
    peor_alumno = min(promedios, key=promedios.get)

    print("Promedio general:", prom_general)
    print("Mejor promedio:", mejor_alumno, "(", promedios[mejor_alumno], ")")
    print("Peor promedio:", peor_alumno, "(", promedios[peor_alumno], ")")

reporte_curso(curso)
print()
resumen(curso)