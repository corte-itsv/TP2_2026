def agrupar_por_inicial(nombres):
    resultado = {}
    for nombre in nombres:
        inicial = nombre[0]
        if inicial not in resultado:
            resultado[inicial] = []

        resultado[inicial].append(nombre)

    return resultado


nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos",
           "Camila", "Ana Paula", "Diego", "Daniela"]

resultado = agrupar_por_inicial(nombres)

for inicial, lista in resultado.items():
    print(f"{inicial}: {lista}")