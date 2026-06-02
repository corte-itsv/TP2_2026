def agrupar_por_inicial(nombres):
    agrupados = {}
    for nombre in nombres:
        inicial = nombre[0].upper()   # primera letra en mayúscula
        agrupados[inicial] = agrupados.get(inicial, []) + [nombre]
    return agrupados



nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos",
           "Camila", "Ana Paula", "Diego", "Daniela"]

resultado = agrupar_por_inicial(nombres)


for inicial in sorted(resultado.keys()):
    print(f"{inicial}: {resultado[inicial]}")
