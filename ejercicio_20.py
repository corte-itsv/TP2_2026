padron     = set()
ya_votaron = set()
votos      = {"Ana": 0, "Luis": 0, "Sol": 0, "Blanco": 0}
CANDIDATOS = {"Ana", "Luis", "Sol"}


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
    if candidato in CANDIDATOS:
        votos[candidato] += 1
    else:
        votos["Blanco"] += 1
        print(f"{nombre_votante} votó en blanco.")


def resultado(votos):
    return dict(sorted(votos.items(), key=lambda x: x[1], reverse=True))


def ganador(votos):
    return max(votos, key=votos.get)


# Simulación
for alumno in ["Valentina", "Tomás", "Camila", "Diego", "Lucía"]:
    registrar_alumno(padron, alumno)

votar(votos, ya_votaron, "Valentina", "Ana",  padron)
votar(votos, ya_votaron, "Tomás",     "Sol",  padron)
votar(votos, ya_votaron, "Camila",    "Ana",  padron)
votar(votos, ya_votaron, "Diego",     "Luis", padron)
votar(votos, ya_votaron, "Valentina", "Sol",  padron)  # ya votó
votar(votos, ya_votaron, "Pedro",     "Ana",  padron)  # no habilitado
votar(votos, ya_votaron, "Lucía",     "Marta",padron)  # voto blanco

print()
print("=== RESULTADOS ===")
sufijos = {1: "voto"}
for nombre, cant in resultado(votos).items():
    suf = sufijos.get(cant, "votos")
    print(f"{nombre:7}: {cant} {suf}")

g = ganador(votos)
print(f"\n🏆 Ganador/a: {g} con {votos[g]} votos")