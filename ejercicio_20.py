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

    if candidato in ["Ana", "Luis", "Sol"]:
        votos[candidato] += 1
    else:
        votos["Blanco"] += 1
        print(f"{nombre_votante} votó en blanco.")

def resultado(votos):
    votos_ordenados = dict(sorted(votos.items(), key=lambda item: item[1], reverse=True))
    print("\n=== RESULTADOS ===")
    for candidato, cant in votos_ordenados.items():
        print(f"{candidato:<6} : {cant} votos")
    return votos_ordenados

def ganador(votos):
    ganador_actual = ""
    votos_ganador = -1
    for candidato, cantidad in votos.items():
        if candidato != "Blanco" and cantidad > votos_ganador:
            votos_ganador = cantidad
            ganador_actual = candidato
    return ganador_actual, votos_ganador

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
votar(votos, ya_votaron, "Lucía",     "Marta", padron)

resultado(votos)
nom_ganador, cant_votos = ganador(votos)
print(f"\n🏆 Ganador/a: {nom_ganador} con {cant_votos} votos.")