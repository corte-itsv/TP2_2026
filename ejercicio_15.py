def agrupar_por_inicial(nombres):
    grupos = {}

    for nombre in nombres:
        inicial = nombre[0]

        if inicial not in grupos:
            grupos[inicial] = []

        grupos[inicial].append(nombre)

    return grupos


# Prueba
nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos",
           "Camila", "Ana Paula", "Diego", "Daniela"]

resultado = agrupar_por_inicial(nombres)

for inicial, lista_nombres in resultado.items():
    print(inicial, "->", lista_nombres)