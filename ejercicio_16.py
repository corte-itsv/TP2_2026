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
    alumno_destacado = max(promedios, key=promedios.get)
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

print(f"Reporte del curso:")
reporte = reporte_curso(curso)
for alumno, (prom, estado) in reporte.items():
    print(f"  {alumno}: {prom} - {estado}")

print(f"\nResumen del curso:")
resumen_data = resumen(curso)
print("Promedio general del curso:", round(sum(resumen_data['aprobados']) / len(curso), 2))
print(f"  Alumno destacado: {resumen_data['alumno_destacado'][0]} ({resumen_data['alumno_destacado'][1]})")
