def promedio(notas):
    return round(sum(notas) / len(notas), 2)


def condicion(promedio):
    if promedio >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"

def reporte_curso(curso):
    reporte = {}
    for alumno, notas in curso.items():
        prom = promedio(notas)
        reporte[alumno] = (prom, condicion(prom))
    return reporte 


def resumen(curso):
    promedios = {alumno: promedio(notas) for alumno, notas in curso.items()}
    alumno_destacado = max(promedios, key=promedios.get)  # Remove trailing comma
    promedio_destacado = round(promedios[alumno_destacado], 2)
    aprobados = [alumno for alumno, prom in promedios.items() if prom >= 6]
    
    return {
        "alumno_destacado": (alumno_destacado, promedio_destacado),
        "aprobados": aprobados
    }


curso = {
    "Ana":     [9, 10, 8, 9, 7],
    "Luis":    [6,  5, 7, 6, 4],
    "Sol":     [10, 9, 10, 8, 9],
    "Marcos":  [4,  5, 3, 6, 2],
    "Julia":   [7,  8, 7, 9, 8],
    "Pedro":   [5,  4, 6, 5, 3],
}

print(f"Reporte del curso: {reporte_curso(curso)}")
print(f"Resumen del curso: {resumen(curso)}")
