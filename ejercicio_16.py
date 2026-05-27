def promedio(notas):
    return round(sum(notas) / len(notas), 2)

def condicion(prom):
    if prom >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"

def reporte_curso(curso):
    lista_alumnos = []
    for nombre, notas in curso.items():
        prom = promedio(notas)
        cond = condicion(prom)
        lista_alumnos.append([nombre, prom, cond])
    
    lista_ordenada = sorted(lista_alumnos, key=lambda x: x[1], reverse=True)
    
    print("======================================")
    print("          REPORTE DEL CURSO")
    print("======================================")
    print("Alumno     | Promedio | Condición")
    print("--------------------------------------")
    for nombre, prom, cond in lista_ordenada:
        print(f"{nombre:<10} | {prom:>8.2f} | {cond}")
    print("======================================")
    
    return lista_ordenada

def resumen(curso):
    lista_ordenada = reporte_curso(curso)
    
    promedio_general = round(sum(a[1] for a in lista_ordenada) / len(lista_ordenada), 2)
    mejor = lista_ordenada[0]
    peor  = lista_ordenada[-1]
    
    print(f"Promedio general del curso: {promedio_general:.2f}")
    print(f"Mejor promedio: {mejor[0]} ({mejor[1]:.2f})")
    print(f"Peor promedio: {peor[0]} ({peor[1]:.2f})")

# --- Programa principal ---
curso = {
    "Ana":    [9, 10, 8, 9, 7],
    "Luis":   [6,  5, 7, 6, 4],
    "Sol":    [10, 9, 10, 8, 9],
    "Marcos": [4,  5, 3, 6, 2],
    "Julia":  [7,  8, 7, 9, 8],
    "Pedro":  [5,  4, 6, 5, 3],
}

resumen(curso)