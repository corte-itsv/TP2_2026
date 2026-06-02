def agrupar_por_inicial(nombres):
    resultado = {}
    for nombre in nombres:
        inicial = nombre[0].upper()
        if inicial not in resultado:
            resultado[inicial] = []
        resultado[inicial].append(nombre)
    return resultado
 
nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos",
           "Camila", "Ana Paula", "Diego", "Daniela"]
 
grupos = agrupar_por_inicial(nombres)
print()
for letra in sorted(grupos):
    print(letra + ": " + str(grupos[letra]))