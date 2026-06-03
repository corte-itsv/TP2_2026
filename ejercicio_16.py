def promedio(notas):
    return round(sum(notas) / len(notas), 2)

def condicion(promedio):    
    if promedio >= 6:
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
    print("           REPORTE DEL CURSO")
    print("======================================")
    print("Alumno     | Promedio | Condición")
    print("--------------------------------------")
    for nombre, prom, cond in lista_ordenada:
        print(f"{nombre:<10} | {prom:>8.2f} | {cond}")
    print("======================================")
    return lista_ordenada

def resumen(curso, lista_ordenada):
    suma_promedios = 0
    for alumno in lista_ordenada:
        suma_promedios += alumno[1]
    promedio_general = round(suma_promedios / len(lista_ordenada), 2) 
    mejor_alumno = lista_ordenada[0][0]    
    mejor_nota = lista_ordenada[0][1]
    peor_alumno = lista_ordenada[-1][0]
    peor_nota = lista_ordenada[-1][1]
    
    print(f"Promedio general del curso: {promedio_general:.2f}")
    print(f"Mejor promedio: {mejor_alumno} ({mejor_nota:.2f})")
    print(f"Peor promedio: {peor_alumno} ({peor_nota:.2f})")

curso = {
    "Ana":     [9, 10, 8, 9, 7],
    "Luis":    [6,  5, 7, 6, 4],
    "Sol":     [10, 9, 10, 8, 9],
    "Marcos":  [4,  5, 3, 6, 2],
    "Julia":   [7,  8, 7, 9, 8],
    "Pedro":   [5,  4, 6, 5, 3],
}

lista_ordenada = reporte_curso(curso)
resumen(curso, lista_ordenada)