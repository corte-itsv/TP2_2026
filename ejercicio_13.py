curso = {
    "Ana":     [9, 10, 8, 9],
    "Luis":    [6,  5, 7, 6],
    "Sol":     [10, 9, 10, 8],
    "Marcos":  [4,  5, 3, 6],
    "Julia":   [7,  8, 7, 9],
}
def calcular_promedios(curso):
    promedios_curso = []
    for alumno, promedio in curso.items():
        prom = sum(promedio) / len(promedio)
        promedios = {"nombre": alumno,
                 "promedio": prom}
        promedios_curso.append(promedios)
    return promedios_curso
print(calcular_promedios(curso))