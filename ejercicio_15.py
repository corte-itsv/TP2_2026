def agrupar_por_inicial(nombres):
    agenda_iniciales = {}
    for nombre in nombres:
        inicial = nombre[0].upper()
        agenda_iniciales[inicial] = agenda_iniciales.get(inicial, []) + [nombre]
    return agenda_iniciales

# Pruebas
nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos",
           "Camila", "Ana Paula", "Diego", "Daniela"]

grupos = agrupar_por_inicial(nombres)
for inicial, lista_noms in sorted(grupos.items()):
    print(f"{inicial}: {lista_noms}")