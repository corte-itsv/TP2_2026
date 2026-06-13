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
            


dicc_promedios = calcular_promedios(curso)
print(f"Promedios: {dicc_promedios}")

destacado = alumno_destacado(dicc_promedios)
nota_max = dicc_promedios[destacado]
print(f"Alumno destacado: {destacado} ({nota_max})")

lista_aprobados = alumnos_aprobados(dicc_promedios)
print(f"Aprobados: {lista_aprobados}")