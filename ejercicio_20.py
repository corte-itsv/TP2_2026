def registrar_alumno(padron, nombre):
    # Agrega el nombre al set de alumnos habilitados
    padron.add(nombre)


def votar(votos, ya_votaron, nombre_votante, candidato, padron):
    # Controla que el alumno esté registrado
    if nombre_votante not in padron:
        print(f"{nombre_votante} no está habilitado para votar.")
        return

    # Controla que no haya votado antes
    if nombre_votante in ya_votaron:
        print(f"{nombre_votante} ya votó.")
        return

    # Registra que el alumno ya emitió su voto
    ya_votaron.add(nombre_votante)

    # Contabiliza el voto (si no es válido, va a Blanco)
    if candidato in ["Ana", "Luis", "Sol"]:
        votos[candidato] += 1
    else:
        votos[candidato] = votos.get(candidato, 0) + 1
        print(f"{nombre_votante} votó en blanco.")


def resultado(votos):
    # Devuelve el diccionario ordenado de mayor a menor según la cantidad de votos
    return dict(sorted(votos.items(), key=lambda item: item[1], reverse=True))


def ganador(votos):
    # Filtra los candidatos reales (excluye Blanco) para determinar el ganador
    candidatos_reales = {k: v for k, v in votos.items() if k != "Blanco"}
    return max(candidatos_reales, key=candidatos_reales.get)


# --- SIMULACIÓN DE LA VOTACIÓN ---

padron = set()
ya_votaron = set()
votos = {"Ana": 0, "Luis": 0, "Sol": 0, "Blanco": 0}

# Registro de alumnos
registrar_alumno(padron, "Valentina")
registrar_alumno(padron, "Tomás")
registrar_alumno(padron, "Camila")
registrar_alumno(padron, "Diego")
registrar_alumno(padron, "Lucía")

# Procesamiento de votos
votar(votos, ya_votaron, "Valentina", "Ana", padron)
votar(votos, ya_votaron, "Tomás", "Sol", padron)
votar(votos, ya_votaron, "Camila", "Ana", padron)
votar(votos, ya_votaron, "Diego", "Luis", padron)
votar(votos, ya_votaron, "Valentina", "Sol", padron)  # Ya votó
votar(votos, ya_votaron, "Pedro", "Ana", padron)  # No habilitado
votar(votos, ya_votaron, "Lucía", "Marta", padron)  # Candidato inválido -> Blanco

# Mostrar resultados
print("\n=== RESULTADOS ===")
votos_ordenados = resultado(votos)
for cand, cant in votos_ordenados.items():
    texto_voto = "voto" if cant == 1 else "votos"
    print(f"{cand} : {cant} {texto_voto}")
print("")
candidato_ganador = ganador(votos)
print(f"🏆 Ganador/a: {candidato_ganador} con {votos[candidato_ganador]} votos")





