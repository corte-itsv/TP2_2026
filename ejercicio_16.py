def promedio(notas):
    return round(sum(notas) / len(notas), 2)

def condicion(prom):
    return "Aprobado" if prom >= 6 else "Desaprobado"

def reporte_curso(curso):
    print("======================================")
    print("          REPORTE DEL CURSO")
    print("======================================")
    print("Alumno     | Promedio | Condición")
    print("--------------------------------------")
    
    informe = []
    for nombre, notas in curso.items():
        prom_alum = promedio(notas)
        informe.append((nombre, prom_alum, condicion(prom_alum)))
    
    # Ordenar de mayor a menor promedio
    informe.sort(key=lambda x: x[1], reverse=True)
    
    for nombre, prom, cond in informe:
        print(f"{nombre:<10} | {prom:>8.2f} | {cond}")
    print("======================================")

def resumen(curso):
    promedios = [promedio(notas) for notas in curso.values()]
    prom_general = round(sum(promedios) / len(promedios), 2)
    
    mejor = max(curso.keys(), key=lambda k: promedio(curso[k]))
    peor = min(curso.keys(), key=lambda k: promedio(curso[k]))
    
    print(f"Promedio general del curso: {prom_general}")
    print(f"Mejor promedio: {mejor} ({promedio(curso[mejor]):.2f})")
    print(f"Peor promedio: {peor} ({promedio(curso[peor]):.2f})")

# Pruebas
curso = {
    "Ana":     [9, 10, 8, 9, 7],
    "Luis":    [6,  5, 7, 6, 4],
    "Sol":     [10, 9, 10, 8, 9],
    "Marcos":  [4,  5, 3, 6, 2],
    "Julia":   [7,  8, 7, 9, 8],
    "Pedro":   [5,  4, 6, 5, 3],
}

reporte_curso(curso)
resumen(curso)