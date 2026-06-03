def agrupar_por_inicial(nombres):
    grupos = {}
    for nombre in nombres:
        inicial = nombre[0].upper()
        if inicial not in grupos:
            grupos[inicial] = []
        grupos[inicial].append(nombre)
    return grupos

nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos", "Camila", "Ana Paula", "Diego", "Daniela"]
resultado = agrupar_por_inicial(nombres)
for letra, lista_nombres in sorted(resultado.items()):
    print(f"{letra}: {lista_nombres}")