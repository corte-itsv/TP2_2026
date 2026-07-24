def agrupar_por_inicial(nombres):
    iniciales = {}
    for nombre in nombres:
        inicial = nombre[0]
        if inicial not in iniciales:
            iniciales[inicial] = [nombre]
        else:
            iniciales[inicial].append(nombre)
    return iniciales

nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos",
           "Camila", "Ana Paula", "Diego", "Daniela"]

print(agrupar_por_inicial(nombres))