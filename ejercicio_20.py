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
        votos[candidato] = votos.get(candidato, 0) + 1
        print(f"{nombre_votante} votó en blanco.")


def resultado(votos):
    return dict(sorted(votos.items(), key=lambda item: item[1], reverse=True))


def ganador(votos):
    candidatos_reales = {k: v for k, v in votos.items() if k != "Blanco"}
    return max(candidatos_reales, key=candidatos_reales.get)


padron = set()
ya_votaron = set()
votos = {"Ana": 0, "Luis": 0, "Sol": 0, "Blanco": 0}

registrar_alumno(padron, "Valentina")
registrar_alumno(padron, "Tomás")
registrar_alumno(padron, "Camila")
registrar_alumno(padron, "Diego")
registrar_alumno(padron, "Lucía")

votar(votos, ya_votaron, "Valentina", "Ana", padron)
votar(votos, ya_votaron, "Tomás", "Sol", padron)
votar(votos, ya_votaron, "Camila", "Ana", padron)
votar(votos, ya_votaron, "Diego", "Luis", padron)
votar(votos, ya_votaron, "Valentina", "Sol", padron) 
votar(votos, ya_votaron, "Pedro", "Ana", padron)  
votar(votos, ya_votaron, "Lucía", "Marta", padron) 

print("\n=== RESULTADOS ===")
votos_ordenados = resultado(votos)
for cand, cant in votos_ordenados.items():
    texto_voto = "voto" if cant == 1 else "votos"
    print(f"{cand} : {cant} {texto_voto}")
print("")
candidato_ganador = ganador(votos)
print(f"🏆 Ganador/a: {candidato_ganador} con {votos[candidato_ganador]} votos")

