def calcular_promedios(curso):
    return {
        nombre: round(sum(notas) / len(notas), 2)
        for nombre, notas in curso.items()
    }

def alumno_destacado(promedios):
    return max(promedios, key=promedios.get)

def alumnos_aprobados(promedios):
    return [nombre for nombre, promedio in promedios.items() if promedio >= 6]


# Datos de prueba
curso = {
    "Ana":     [9, 10, 8, 9],
    "Luis":    [6, 5, 7, 6],
    "Sol":     [10, 9, 10, 8],
    "Marcos":  [4, 5, 3, 6],
    "Julia":   [7, 8, 7, 9],
}

# Uso de las funciones
promedios = calcular_promedios(curso)

print("Promedios:", promedios)
print("Alumno destacado:", alumno_destacado(promedios))
print("Alumnos aprobados:", alumnos_aprobados(promedios))