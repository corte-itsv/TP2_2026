def registrar_alumno(padron, nombre):
    padron.add(nombre)


def votar(votos, ya_votaron, nombre_votante, candidato, padron):
    if nombre_votante not in padron:
        print(nombre_votante, "no está habilitado para votar.")
        return

    if nombre_votante in ya_votaron:
        print(nombre_votante, "ya votó.")
        return

    ya_votaron.add(nombre_votante)

    if candidato in votos and candidato != "Blanco":
        votos[candidato] += 1
    else:
        votos["Blanco"] += 1
        print(nombre_votante, "votó en blanco.")


def resultado(votos):
    return dict(sorted(votos.items(), key=lambda x: x[1], reverse=True))


def ganador(votos):
    max_votos = -1
    ganador = ""

    for candidato, cantidad in votos.items():
        if candidato != "Blanco" and cantidad > max_votos:
            max_votos = cantidad
            ganador = candidato

    return ganador

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

res = resultado(votos)

for candidato, cantidad in res.items():
    print(f"{candidato:<7}: {cantidad} votos")

gan = ganador(votos)
print(f"\n🏆 Ganador/a: {gan} con {votos[gan]} votos") 