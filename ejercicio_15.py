def agrupar_por_inicial(nombres):
    inicial_nombre = {}
    for nombre in nombres:
        lista_actual = inicial_nombre.get(nombre[0],[])
        lista_actual.append(nombre)
        inicial_nombre[nombre[0]] = lista_actual
    return inicial_nombre

nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos",
           "Camila", "Ana Paula", "Diego", "Daniela"]

agenda_iniciales = agrupar_por_inicial(nombres)

for inicial, nombres in agenda_iniciales.items():
    print(f"{inicial}: {nombres}")