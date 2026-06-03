def calcular_promedios(curso):
    return {nombre: sum(notas)/len(notas) for nombre, notas in curso.items()}

def alumno_destacado(promedios):
    mejor_alumno = None
    mejor_promedio = -1
    for nombre, promedio in promedios.items():
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_alumno = nombre
    return mejor_alumno, mejor_promedio

def alumnos_aprobados(promedios):
    aprobados = []
    for nombre, promedio in promedios.items():
        if promedio >= 6:
            aprobados.append(nombre)
    return aprobados

datos_crudos = {
    "Ana": "9,10,8,9",
    "Luis": "6,5,7,6",
    "Sol": "10,9,10,8",
    "Marcos": "4,5,3,6",
    "Julia": "7,8,7,9"
}

curso = {nombre: [int(n) for n in notas.split(",")] for nombre, notas in datos_crudos.items()}

promedios_dict = calcular_promedios(curso)
print(f"Promedios: {promedios_dict}")
destacado, nota_destacado = alumno_destacado(promedios_dict)
print(f"Alumno destacado: {destacado} ({nota_destacado})")
print(f"Aprobados: {alumnos_aprobados(promedios_dict)}")
