def agrupar_por_inicial(nombres):
    resultado = {}
    for nombre in nombres:
        inicial = nombre[0].upper() 
        if inicial not in resultado:
            resultado[inicial] = []
        resultado[inicial].append(nombre)
    return resultado


nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos", "Camila", "Ana Paula", "Diego", "Daniela"]
salida = agrupar_por_inicial(nombres)

for letra, lista_nombres in salida.items():
    print(f"{letra}: {lista_nombres}")
