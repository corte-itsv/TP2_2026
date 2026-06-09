def calcular_promedios(curso):
    return {alumno: sum(notas) / len(notas) for alumno, notas in curso.items()}


def alumno_destacado(promedios):
    alumno_destacado = max(promedios, key=promedios.get)
    return alumno_destacado 

def alumnos_aprobados(promedios):
    aprobados = [alumno for alumno, promedio in promedios.items() if promedio >= 6]
    return aprobados


curso = {
    "Ana":     [9, 10, 8, 9],
    "Luis":    [6,  5, 7, 6],
    "Sol":     [10, 9, 10, 8],
    "Marcos":  [4,  5, 3, 6],
    "Julia":   [7,  8, 7, 9],
}

print(f"Promedios: {calcular_promedios(curso)})")
print(f"Alumno destacado: {alumno_destacado(calcular_promedios(curso))}, ({calcular_promedios(curso)[alumno_destacado(calcular_promedios(curso))]})") 
print(f"Aprobados: {alumnos_aprobados(calcular_promedios(curso))}")

