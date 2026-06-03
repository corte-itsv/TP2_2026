def agrupar_por_inicial(nombres):
    agrupados = {}
    for nombre in nombres:
        
        inicial = nombre[0].upper()
        
        if inicial not in agrupados:
            agrupados[inicial] = []
        agrupados[inicial].append(nombre)
    return agrupados


nombr = ["Ana", "Alberto", "Belen", "Bruno", "Carlos",
                "Camila", "Ana Paula", "Diego", "Daniela"]

agrupados = agrupar_por_inicial(nombr)

for letra in sorted(agrupados.keys()):
    print(f"{letra}: {agrupados[letra]}")
