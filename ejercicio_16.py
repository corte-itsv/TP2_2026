curso = {
    "Ana":   [9, 10, 8, 9, 7],
    "Luis":  [6, 5, 7, 6, 4],
    "Sol":   [10, 9, 10, 8, 9],
    "Marcos":[4, 5, 3, 6, 2],
    "Julia": [7, 8, 7, 9, 8],
    "Pedro": [5, 4, 6, 5, 3],
}

def promedio(notas):
    return round(sum(notas) / len(notas), 2)

def condicion(promedio):
    return "Aprobado" if promedio >= 6 else "Desaprobado"

def reporte_curso(curso):
    resultados = []
    for nombre, notas in curso.items():
        prom = promedio(notas)
        cond = condicion(prom)
        resultados.append((nombre, prom, cond))
    
    resultados.sort(key=lambda x: x[1], reverse=True)
    
    separador = "=" * 36
    print(separador)
    print(f"{'REPORTE DEL CURSO':^36}")
    print(separador)
    print(f"{'Alumno':<10} | {'Promedio':>8} | {'Condición'}")
    print("-" * 36)
    for nombre, prom, cond in resultados:
        print(f"{nombre:<10} | {prom:>8.2f} | {cond}")
    print(separador)
    
    return resultados

def resumen(curso):
    resultados = reporte_curso(curso)
    
    promedios = [(nombre, prom) for nombre, prom, _ in resultados]
    total = sum(p for _, p in promedios)
    prom_general = round(total / len(promedios), 2)
    
    mejor = max(promedios, key=lambda x: x[1])
    peor = min(promedios, key=lambda x: x[1])
    
    print(f"Promedio general del curso: {prom_general}")
    print(f"Mejor promedio: {mejor[0]} ({mejor[1]:.2f})")
    print(f"Peor promedio: {peor[0]} ({peor[1]:.2f})")

resumen(curso)