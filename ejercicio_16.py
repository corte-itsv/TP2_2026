def promedio(notas):
    if not notas:
        return 0
    return round(sum(notas) / len(notas), 2)

def condicion(promedio_alumno):
    return "Aprobado" if promedio_alumno >= 6 else "Desaprobado"

def reporte_curso(curso):
    print("======================================")
    print("          REPORTE DEL CURSO")
    print("======================================")
    print("Alumno     | Promedio | Condición")
    print("--------------------------------------")
    

    lista_alumnos = []
    for nombre, notas in curso.items():
        prom = promedio(notas)
        cond = condicion(prom)
        lista_alumnos.append((nombre, prom, cond))
        

    lista_alumnos.sort(key=lambda x: x[1], reverse=True)
    
    for nombre, prom, cond in lista_alumnos:
        
        print(f"{nombre:<10} | {prom:8.2f} | {cond}")
    print("======================================")

def resumen(curso):
    total_promedios = []
    mejor_alumno = None
    mejor_prom = -1
    peor_alumno = None
    peor_prom = 100
    
    for nombre, notas in curso.items():
        prom = promedio(notas)
        total_promedios.append(prom)
        
        if prom > mejor_prom:
            mejor_prom = prom
            mejor_alumno = nombre
        if prom < peor_prom:
            peor_prom = prom
            peor_alumno = nombre
            
    promedio_gral = sum(total_promedios) / len(total_promedios)
    print(f"Promedio general del curso: {promedio_gral:.2f}")
    print(f"Mejor promedio: {mejor_alumno} ({mejor_prom:.2f})")
    print(f"Peor promedio: {peor_alumno} ({peor_prom:.2f})")


cursox = {
    "Ana":     [9, 10, 8, 9, 7],
    "Luis":    [6,  5, 7, 6, 4],
    "Sol":     [10, 9, 10, 8, 9],
    "Marcos":  [4,  5, 3, 6, 2],
    "Julia":   [7,  8, 7, 9, 8],
    "Pedro":   [5,  4, 6, 5, 3],
}
reporte_curso(cursox)
resumen(cursox)