
curso = {
    "Ana":     [9, 10, 8, 9],
    "Luis":    [6,  5, 7, 6],
    "Sol":     [10, 9, 10, 8],
    "Marcos":  [4,  5, 3, 6],
    "Julia":   [7,  8, 7, 9],
}


def calcular_promedios(curso):
    return {nombre: sum(notas) / len(notas) for nombre, notas in curso.items()}

def alumno_destacado(promedios):
    return max(promedios, key=promedios.get)

def alumnos_aprobados(promedios):
    return [nombre for nombre, prom in promedios.items() if prom >= 6]

dicc_promedios = calcular_promedios(curso)
mejor = alumno_destacado(dicc_promedios)
aprobados = alumnos_aprobados(dicc_promedios)

print("Promedios:", dicc_promedios)
print("Alumno destacado:", mejor)
print("Alumnos Aprobados:", aprobados)


