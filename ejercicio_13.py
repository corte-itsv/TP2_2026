curso = {
    "Ana": [9, 10, 8, 9],
    "Luis": [6, 5, 7, 6],
    "Sol": [10, 9, 10, 8],
    "Marcos": [4, 5, 3, 6],
    "Julia": [7, 8, 7, 9],
}

def calcular_promedios(curso):
  return {nombre: sum(notas) / len(notas) for nombre, notas in curso.items()}

def alumno_destacado(promedios):
  return max(promedios, key=promedios.get)

def alumnos_aprobados(promedios):
  return [nombre for nombre, promedio in promedios.items() if promedio >= 6]

promedios = calcular_promedios(curso)
mejor_alumno = alumno_destacado(promedios)
aprobados = alumnos_aprobados(promedios)

print(f"Promedios: {promedios}")
print(f"Alumno destacado: {mejor_alumno} ({promedios[mejor_alumno]})")
print(f"Aprobados: {aprobados}")
