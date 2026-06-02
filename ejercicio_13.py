curso = {
    "Ana":    [9, 10, 8, 9],
    "Luis":   [6,  5, 7, 6],
    "Sol":    [10, 9, 10, 8],
    "Marcos": [4,  5, 3, 6],
    "Julia":  [7,  8, 7, 9],
}
 
def calcular_promedios(curso):
    promedios = {}
    for nombre in curso:
        notas = curso[nombre]
        promedios[nombre] = sum(notas) / len(notas)
    return promedios
 
def alumno_destacado(promedios):
    mejor = ""
    mayor = 0
    for nombre in promedios:
        if promedios[nombre] > mayor:
            mayor = promedios[nombre]
            mejor = nombre
    return mejor
 
def alumnos_aprobados(promedios):
    aprobados = []
    for nombre in promedios:
        if promedios[nombre] >= 6:
            aprobados.append(nombre)
    return aprobados
 
promedios = calcular_promedios(curso)
destacado = alumno_destacado(promedios)
print("\nPromedios: " + str(promedios))
print("Alumno destacado: " + destacado + " (" + str(promedios[destacado]) + ")")
print("Aprobados: " + str(alumnos_aprobados(promedios)))