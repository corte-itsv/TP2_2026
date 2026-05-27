
Eitanlan
2 days ago

Resuelve ejercicio 13
def calcular_promedios(curso):
    # ¡Esto estuvo impecable!
    promedios = {nombre: sum(ns) / len(ns) for nombre, ns in curso.items()}
    return promedios


def alumno_destacado(promedios):
    mejor_alumno = ""
    max_promedio = 0  # Empezamos en cero para comparar números reales
    
    # Usamos .items() para obtener el nombre y el promedio directo
    for nombre, promedio in promedios.items():
        if promedio > max_promedio:
            max_promedio = promedio
            mejor_alumno = nombre
            
    # Retornamos una tupla con el nombre y el número para armar el print pedido
    return mejor_alumno, max_promedio


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

destacado, nota_max = alumno_destacado(dicc_promedios)
print(f"Alumno destacado: {destacado} ({nota_max})")

lista_aprobados = alumnos_aprobados(dicc_promedios)
print(f"Aprobados: {lista_aprobados}")
