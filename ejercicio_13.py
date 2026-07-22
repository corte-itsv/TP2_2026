def calcular_promedios(curso):
    promedios = {nombre: sum(ns) / len(ns) for nombre, ns in curso.items()}
    return promedios


def alumno_destacado(promedios):
    mejor_alumno = ""
    max_promedio = 0  
    
    for nombre, promedio in promedios.items():
        if promedio > max_promedio:
            max_promedio = promedio
            mejor_alumno = nombre
            
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

dicc_promedios = calcular_promedios(curso)
print(f"Promedios: {dicc_promedios}")

destacado = alumno_destacado(dicc_promedios)
nota_max = dicc_promedios[destacado]
print(f"Alumno destacado: {destacado} ({nota_max})")

lista_aprobados = alumnos_aprobados(dicc_promedios)
print(f"Aprobados: {lista_aprobados}")