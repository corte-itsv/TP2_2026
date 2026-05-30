def promedio(notas):
    return round(sum(notas) / len(notas), 2)

def condicion(prom):
    return "Aprobado" if prom >= 6 else "Desaprobado"

def reporte_curso(curso):
    print("======================================")
    print("          REPORTE DEL CURSO")
    print("======================================")
    print(f"{'Alumno':<10} | {'Promedio':>8} | Condición")
    print("--------------------------------------")
    ranking = sorted(curso.items(), key=lambda x: promedio(x[1]), reverse=True)
    for nombre, notas in ranking:
        p = promedio(notas)
        print(f"{nombre:<10} | {p:>8.2f} | {condicion(p)}")
    print("======================================")

def resumen(curso):
    promedios = {nombre: promedio(notas) for nombre, notas in curso.items()}
    prom_general = round(sum(promedios.values()) / len(promedios), 2)
    mejor = max(promedios, key=promedios.get)
    peor  = min(promedios, key=promedios.get)
    print(f"Promedio general del curso: {prom_general}")
    print(f"Mejor promedio: {mejor} ({promedios[mejor]})")
    print(f"Peor promedio:  {peor} ({promedios[peor]})")


curso = {
    "Ana":    [9, 10, 8, 9, 7],
    "Luis":   [6,  5, 7, 6, 4],
    "Sol":    [10, 9, 10, 8, 9],
    "Marcos": [4,  5, 3, 6, 2],
    "Julia":  [7,  8, 7, 9, 8],
    "Pedro":  [5,  4, 6, 5, 3],
}

reporte_curso(curso)
resumen(curso)