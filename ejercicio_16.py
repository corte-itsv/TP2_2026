curso = {
    "Ana":     [9, 10, 8, 9, 7],
    "Luis":    [6,  5, 7, 6, 4],
    "Sol":     [10, 9, 10, 8, 9],
    "Marcos":  [4,  5, 3, 6, 2],
    "Julia":   [7,  8, 7, 9, 8],
    "Pedro":   [5,  4, 6, 5, 3],
}


def promedio(notas):
    return round(sum(notas) / len(notas), 2)


def condicion(prom):
    if prom >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"


def reporte_curso(curso):
   
    datos = [(nombre, promedio(notas)) for nombre, notas in curso.items()]
   
    datos.sort(key=lambda x: x[1], reverse=True)

    print("======================================")
    print("          REPORTE DEL CURSO")
    print("======================================")
    print("Alumno     | Promedio | Condición")
    print("--------------------------------------")
    for nombre, prom in datos:
        print(f"{nombre:<10} | {prom:8.2f} | {condicion(prom)}")
    print("======================================")

    return datos


def resumen(curso):
    datos = [(nombre, promedio(notas)) for nombre, notas in curso.items()]
    prom_general = round(sum(p for _, p in datos) / len(datos), 2)
    mejor = max(datos, key=lambda x: x[1])
    peor = min(datos, key=lambda x: x[1])

    print(f"Promedio general del curso: {prom_general}")
    print(f"Mejor promedio: {mejor[0]} ({mejor[1]:.2f})")
    print(f"Peor promedio: {peor[0]} ({peor[1]:.2f})")


datos = reporte_curso(curso)
resumen(curso)