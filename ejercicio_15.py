def agrupar_por_inicial(nombres):
    iniciales = {}
    for nombre in nombres:
        inicial = nombre[0]
        if inicial not in iniciales:
            iniciales[inicial] = []
        iniciales[inicial].append(nombre)
    return iniciales
    

nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos",
"Camila", "Ana Paula", "Diego", "Daniela"]

resultado = agrupar_por_inicial(nombres) 
for inicial, lista_nombres in resultado.items():
    print(f"{inicial}: {lista_nombres}")