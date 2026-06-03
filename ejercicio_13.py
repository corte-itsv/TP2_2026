def calcular_promedios(curso):
    
    return {nombre: round(sum(notas) / len(notas), 2) for nombre, notas in curso.items()}

def alumno_destacado(promedios):
    
    mejor_alumno = None
    mejor_promedio = -1
    for alumno, promedio in promedios.items():
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_alumno = alumno
    return mejor_alumno

def alumnos_aprobados(promedios):

    return [alumno for alumno, promedio in promedios.items() if promedio >= 6]

print("--- Ejercicio 13 ---")
curso_dict = {
    "Ana":     [9, 10, 8, 9],
    "Luis":    [6,  5, 7, 6],
    "Sol":     [10, 9, 10, 8],
    "Marcos":  [4,  5, 3, 6],
    "Julia":   [7,  8, 7, 9],
}

promedios = calcular_promedios(curso_dict)
print(f"Promedios: {promedios}")
destacado = alumno_destacado(promedios)
prom_destacado = promedios[destacado]
print(f"Alumno destacado: {destacado} ({prom_destacado})")
print(f"Aprobados: {alumnos_aprobados(promedios)}")
print()