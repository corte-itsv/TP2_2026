def promedio(notas):
    return round(sum(notas) / len(notas), 2)

def condicion(prom):
    if prom >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"

def reporte_curso(curso):
    datos = []

    for nombre, notas in curso.items():
        prom = promedio(notas)
        datos.append((nombre, prom, condicion(prom)))

    datos.sort(key=lambda x: x[1], reverse=True)

    print("REPORTE DEL CURSO")
    print("-" * 35)
    print(f"{'Alumno':<10} {'Promedio':<10} {'Condición'}")
    print("-" * 35)

    for nombre, prom, cond in datos:
        print(f"{nombre:<10} {prom:<10} {cond}")

def resumen(curso):
    promedios = {nombre: promedio(notas) for nombre, notas in curso.items()}

    promedio_general = round(
        sum(promedios.values()) / len(promedios), 2
    )

    mejor_alumno = max(promedios, key=promedios.get)
    peor_alumno = min(promedios, key=promedios.get)

    print("\nRESUMEN")
    print("-" * 35)
    print("Promedio general:", promedio_general)
    print("Mejor alumno:", mejor_alumno, "-", promedios[mejor_alumno])
    print("Peor alumno:", peor_alumno, "-", promedios[peor_alumno])


# Datos
curso = {
    "Ana":     [9, 10, 8, 9, 7],
    "Luis":    [6, 5, 7, 6, 4],
    "Sol":     [10, 9, 10, 8, 9],
    "Marcos":  [4, 5, 3, 6, 2],
    "Julia":   [7, 8, 7, 9, 8],
    "Pedro":   [5, 4, 6, 5, 3],
}

# Prueba
reporte_curso(curso)
resumen(curso)