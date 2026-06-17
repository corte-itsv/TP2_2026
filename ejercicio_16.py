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
    return "\n".join(f"  {alumno}: {prom} - {estado}" for alumno, (prom, estado) in reporte.items())


def resumen(curso):
    promedios = {alumno: promedio(notas) for alumno, notas in curso.items()}
    peor_alumno = min(promedios, key=promedios.get)
    alumno_destacado = max(promedios, key=promedios.get)
    promedio_destacado = round(promedios[alumno_destacado], 2)
    aprobados = [alumno for alumno, prom in promedios.items() if prom >= 6]
    promedio_general_del_curso = round(sum(promedios[a] for a in curso) / len(curso), 2)
    
    return {
        "peor_alumno": (peor_alumno, promedios[peor_alumno]),
        "alumno_destacado": (alumno_destacado, promedio_destacado),
        "aprobados": aprobados,
        "promedio_general_del_curso": promedio_general_del_curso
    }


curso = {
    "Ana":     [9, 10, 8, 9, 7],
    "Luis":    [6,  5, 7, 6, 4],
    "Sol":     [10, 9, 10, 8, 9],
    "Marcos":  [4,  5, 3, 6, 2],
    "Julia":   [7,  8, 7, 9, 8],
    "Pedro":   [5,  4, 6, 5, 3],
}

print("=" * 30)
print(f"REPORTE DEL CURSO")
reporte = reporte_curso(curso)
print(reporte)




resumen_data = resumen(curso)
print(f"Promedio general del curso: {resumen_data['promedio_general_del_curso']}")
print(f"Mejor promedio: {resumen_data['alumno_destacado'][0]} ({resumen_data['alumno_destacado'][1]})")
print(f"Peor promedio: {resumen_data['peor_alumno'][0]} ({resumen_data['peor_alumno'][1]})")