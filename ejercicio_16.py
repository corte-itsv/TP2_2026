curso16 = {
    "Ana":    [9.20, 10, 8, 9, 7],
    "Luis":   [6,  5, 7, 6, 4],
    "Sol":    [10, 9, 10, 8, 9],
    "Marcos": [4,  5, 3, 6, 2],
    "Julia":  [7,  8, 7, 9, 8],
    "Pedro":  [5,  4, 6, 5, 3],
}
 
def promedio(notas):
    return round(sum(notas) / len(notas), 2)
 
def condicion(prom):
    if prom >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"
 
def reporte_curso(curso):
    datos = []
    for nombre in curso:
        datos.append((nombre, promedio(curso[nombre])))
    datos.sort(key=lambda x: x[1], reverse=True)
 
    print("\n======================================")
    print("          REPORTE DEL CURSO")
    print("======================================")
    print("Alumno     | Promedio | Condición")
    print("--------------------------------------")
    for nombre, prom in datos:
        print(nombre.ljust(10) + " | " + str(prom).rjust(8) + " | " + condicion(prom))
    print("======================================")
 
def resumen(curso):
    mejor = ""
    peor  = ""
    mayor = 0
    menor = 100
    total = 0
    for nombre in curso:
        prom = promedio(curso[nombre])
        total += prom
        if prom > mayor:
            mayor = prom
            mejor = nombre
        if prom < menor:
            menor = prom
            peor  = nombre
    prom_general = round(total / len(curso), 2)
    print("Promedio general del curso: " + str(prom_general))
    print("Mejor promedio: " + mejor + " (" + str(mayor) + ")")
    print("Peor promedio: " + peor + " (" + str(menor) + ")")
 
reporte_curso(curso16)
resumen(curso16)
 