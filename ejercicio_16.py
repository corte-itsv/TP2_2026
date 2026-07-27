curso = {
    "Ana": [9, 10, 8, 9, 7],
    "Luis": [6, 5, 7, 6, 4],
    "Sol": [10, 9, 10, 8, 9],
    "Marcos": [4, 5, 3, 6, 2],
    "Julia": [7, 8, 7, 9, 8],
    "Pedro": [5, 4, 6, 5, 3],
}


def promedio(notas):
    return round(sum(notas) / len(notas), 2)


def condicion(prom):
    if prom >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"


def reporte_curso(curso):
    datos = []

    for alumno, notas in curso.items():
        prom = promedio(notas)
        datos.append((alumno, prom, condicion(prom)))

    datos.sort(key=lambda x: x[1], reverse=True)

    print("=" * 38)
    print("       REPORTE DEL CURSO")
    print("=" * 38)
    print("Alumno     | Promedio | Condición")
    print("-" * 38)

    for alumno, prom, estado in datos:
        print(f"{alumno:10} | {prom:9.2f} | {estado}")

    print("=" * 38)


def resumen(curso):
    promedios = {}

    for alumno, notas in curso.items():
        promedios[alumno] = promedio(notas)

    promedio_general = round(sum(promedios.values()) / len(promedios), 2)

    mejor = max(promedios, key=promedios.get)
    peor = min(promedios, key=promedios.get)

    print(f"Promedio general del curso: {promedio_general}")
    print(f"Mejor promedio: {mejor} ({promedios[mejor]:.2f})")
    print(f"Peor promedio: {peor} ({promedios[peor]:.2f})")


reporte_curso(curso)
resumen(curso)