def registrar_alumno(padron, nombre):
    padron.add(nombre)

def votar(votos, ya_votaron, nombre_votante, candidato, padron):

    if nombre_votante not in padron:
        print(f"{nombre_votante} no está habilitado para votar.")
        return
        

    if nombre_votante in ya_votaron:
        print(f"{nombre_votante} ya votó.")
        return
        

    ya_votaron.add(nombre_votante)
    if candidato in votos:
        votos[candidato] += 1
    else:
        votos["Blanco"] += 1

def resultado(votos):

    return dict(sorted(votos.items(), key=lambda x: x[1], reverse=True))

def ganador(votos):

    max_votos = -1
    candidato_ganador = None
    for cand, cant in votos.items():
        if cand != "Blanco" and cant > max_votos:
            max_votos = cant
            candidato_ganador = cand
    return candidato_ganador, max_votos

print("--- Ejercicio 20 ---")
padron = set()
ya_votaron = set()
votos = {"Ana": 0, "Luis": 0, "Sol": 0, "Blanco": 0}

registrar_alumno(padron, "Valentina")
registrar_alumno(padron, "Tomás")
registrar_alumno(padron, "Camila")
registrar_alumno(padron, "Diego")
registrar_alumno(padron, "Lucía")


votar(votos, ya_votaron, "Valentina", "Ana",  padron)
votar(votos, ya_votaron, "Tomás",     "Sol",  padron)
votar(votos, ya_votaron, "Camila",    "Ana",  padron)
votar(votos, ya_votaron, "Diego",     "Luis", padron)
votar(votos, ya_votaron, "Valentina", "Sol",  padron)  
votar(votos, ya_votaron, "Pedro",     "Ana",  padron)  
votar(votos, ya_votaron, "Lucía",     "Marta",padron)  


print("=== RESULTADOS ===")
resultados_ordenados = resultado(votos)
for cand, cant in resultados_ordenados.items():
    sufijo = "votos" if cant != 1 else "voto"
    print(f"{cand:<7} : {cant} {sufijo}")
    
print()
quien_gano, votos_ganador = ganador(votos)
print(f"🏆 Ganador/a: {quien_gano} con {votos_ganador} votos")
print()