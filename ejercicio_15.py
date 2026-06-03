def agrupar_por_inicial(nombres):
    diccionario_agrupado = {}
    for p in nombres:
        inicial = p[0].upper()
        lista_actual = diccionario_agrupado.get(inicial, [])
        lista_actual.append(p)
        diccionario_agrupado[inicial] = lista_actual
    return diccionario_agrupado

nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos", "Camila", "Ana Paula", "Diego", "Daniela"]
resultado = agrupar_por_inicial(nombres)

for letra, lista_nombres in resultado.items():
    print(f"{letra}: {lista_nombres}")
