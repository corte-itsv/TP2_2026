def agrupar_por_inicial(nombres):
    iniciales = {}
    for nombre in nombres:
        if nombre[0] not in iniciales:
            iniciales[nombre[0]] = []
            iniciales[nombre[0]].append(nombre)
        else: iniciales[nombre[0]].append(nombre)
    return iniciales

nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos",
           "Camila", "Ana Paula", "Diego", "Daniela"]
resultado_agenda = agrupar_por_inicial(nombres)
for inicial, lista_de_nombres in resultado_agenda.items():
    print(f"{inicial}: {lista_de_nombres}")