def promedio(notas):
    """Calcula y devuelve el promedio redondeado a 2 decimales."""
    prom = sum(notas) / len(notas)
    return round(prom, 2)

def condicion(prom):
    """Devuelve 'Aprobado' si el promedio es >= 6, si no 'Desaprobado'."""
    if prom >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"

def reporte_curso(curso):
    """Muestra la tabla ordenada de mayor a menor promedio."""

    lista_promedios = []
    
    for alumno, notas in curso.items():
        prom = promedio(notas)
        lista_promedios.append((alumno, prom))
        
    lista_promedios.sort(key=lambda x: x[1], reverse=True)
    
    print("======================================")
    print("          REPORTE DEL CURSO           ")
    print("======================================")
    print("Alumno | Promedio | Condición         ")
    print("--------------------------------------")
    
    for alumno, prom in lista_promedios:
        estado = condicion(prom)
        print(f"{alumno:<7} | {prom:<8.2f} | {estado}")
        
    print("======================================")
    return lista_promedios # Retornamos la lista para usarla en el resumen

def resumen(curso):
    """Calcula y muestra el promedio general, mejor y peor promedio."""
   
    reporte_ordenado = reporte_curso(curso)
    
    promedios_totales = [prom for _, prom in reporte_ordenado]
    
    promedio_general = sum(promedios_totales) / len(promedios_totales)
    
    mejor = reporte_ordenado[0]
    peor = reporte_ordenado[-1]
    
    print(f"Promedio general del curso: {promedio_general:.2f}")
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

resumen(curso)
