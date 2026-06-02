def promedio(notas):
    return round(sum(notas) / len(notas), 2)

def condicion(prom):
    if prom >= 6:
        return "Aprobado"
    return "Desaprobado"

def reporte_curso(curso):
    datos = []

    for nombre, notas in curso.items():
        prom = promedio(notas)
        datos.append((nombre, prom))

    datos.sort(key=lambda x: x[1], reverse=True)

    print("=" * 38)
    print("         REPORTE DEL CURSO")
    print("=" * 38)
    print("Alumno     | Promedio | Condición")
    print("-" * 38)

    for nombre, prom in datos:
        print(f"{nombre:<10} | {prom:>8.2f} | {condicion(prom)}")

def resumen(curso):
    promedios = {
        nombre: promedio(notas)
        for nombre, notas in curso.items()
    }

    promedio_general = round(
        sum(promedios.values()) / len(promedios),
        2
    )

    mejor = max(promedios.items(), key=lambda x: x[1])
    peor = min(promedios.items(), key=lambda x: x[1])

    print("=" * 38)
    print(f"Promedio general del curso: {promedio_general}")
    print(f"Mejor promedio: {mejor[0]} ({mejor[1]:.2f})")
    print(f"Peor promedio: {peor[0]} ({peor[1]:.2f})")


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