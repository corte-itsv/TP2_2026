def agrupar_por_inicial(nombres):
    iniciales_nombres={}
    for nombre in nombres:
        lista_actual=iniciales_nombres.get(nombre[0],[])    
        lista_actual.append(nombre)
        iniciales_nombres[nombre[0]]=lista_actual
    return iniciales_nombres

nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos",
           "Camila", "Ana Paula", "Diego", "Daniela"]
resultado_agenda = agrupar_por_inicial(nombres)
for inicial, lista_de_nombres in resultado_agenda.items():
    print(f"{inicial}: {lista_de_nombres}")