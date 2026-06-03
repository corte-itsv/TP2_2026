def promedio(notas):
    return round(sum(notas) / len(notas), 2)

def condicion(prom_alumno):
    if prom_alumno >= 6:
        return "Aprobado"
    return "Desaprobado"

def reporte_curso(curso):
    print("======================================")
    print("          REPORTE DEL CURSO")
    print("======================================")
    print(f"{'Alumno':<10} | {'Promedio':<8} | Condición")
    print("--------------------------------------")
    
    lista_reporte = []
    for nombre, notas in curso.items():
        p = promedio(notas)
        c = condicion(p)
        lista_reporte.append((nombre, p, c))
    
    lista_reporte.sort(key=lambda x: x[1], reverse=True)
    
    for nombre, p, c in lista_reporte:
        print(f"{nombre:<10} | {p:>8.2f} | {c}")
    print("======================================")

def resumen(curso):
    todos_promedios = []
    mejor_alumno = None
    peor_alumno = None
    max_p = -1
    min_p = 11
    
    for nombre, notas in curso.items():
        p = promedio(notas)
        todos_promedios.append(p)
        if p > max_p:
            max_p = p
            mejor_alumno = nombre
        if p < min_p:
            min_p = p
            peor_alumno = nombre
            
    promedio_general = round(sum(todos_promedios) / len(todos_promedios), 2)
    print(f"Promedio general del curso: {promedio_general:.2f}")
    print(f"Mejor promedio: {mejor_alumno} ({max_p:.2f})")
    print(f"Peor promedio: {peor_alumno} ({min_p:.2f})")

datos_crudos_16 = {
    "Ana": "9,10,8,9,7",
    "Luis": "6,5,7,6,4",
    "Sol": "10,9,10,8,9",
    "Marcos": "4,5,3,6,2",
    "Julia": "7,8,7,9,8",
    "Pedro": "5,4,6,5,3"
}

curso = {nombre: [int(n) for n in notas.split(",")] for nombre, notas in datos_crudos_16.items()}

reporte_curso(curso)
resumen(curso)
