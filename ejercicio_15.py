def agrupar_por_inicial(nombres):
    agrupacion_por_letras = {}
    for nombre in nombres:
        primer_letra = nombre[0].upper()
        if agrupacion_por_letras.get(primer_letra) == None:
            agrupacion_por_letras[primer_letra] = [nombre]
        else:
            agrupacion_por_letras[primer_letra].append(nombre)
    return agrupacion_por_letras
    
nombres = ["Ana", "Alberto", "Belen", "Bruno", "Carlos", "Camila", "Ana Paula", "Diego", "Daniela"]


nombres_agrupados = agrupar_por_inicial(nombres)
print(nombres_agrupados)