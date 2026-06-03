def calcular_promedios(curso):
    promedios = {
        nombre: sum(notas) / len(notas)
        for nombre, notas in curso.items()
    }
    return promedios

def alumno_destacado(promedios):
    mejor_alumno = ""
    promedio_maximo = 0
    for nombre, promedio in promedios.items():
        if promedio > promedio_maximo:
            mejor_alumno = nombre
            promedio_maximo = promedio 
    return mejor_alumno

def alumnos_aprobados(promedios):
    aprobados = []
    for nombre, promedio in promedios.items():
        if promedio >= 6:
            aprobados.append(nombre)
    return aprobados


curso = {
    "Ana":     [9, 10, 8, 9],
    "Luis":    [6,  5, 7, 6],
    "Sol":     [10, 9, 10, 8],
    "Marcos":  [4,  5, 3, 6],
    "Julia":   [7,  8, 7, 9],
}

dicc_promedios =calcular_promedios(curso)
print(f"Promedios: {dicc_promedios}")
destacado = alumno_destacado(dicc_promedios)
nota_max = dicc_promedios[destacado]
print(f"Alumno destacado: {destacado} ({nota_max})")
print(f"Aprobados: {alumnos_aprobados(dicc_promedios)}")