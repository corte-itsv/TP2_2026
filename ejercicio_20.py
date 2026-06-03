def registrar_alumno(padron, nombre):
    """Agrega al alumno al set de habilitados."""
    padron.add(nombre)

def votar(votos, ya_votaron, nombre_votante, candidato, padron):
    """Registra el voto si el alumno está en el padrón y no ha votado."""
    if nombre_votante not in padron:
        print(f"{nombre_votante} no está habilitado para votar.")
        return
    
    if nombre_votante in ya_votaron:
        print(f"{nombre_votante} ya votó.")
        return
    
    if candidato not in ["Ana", "Luis", "Sol"]:
        candidato = "Blanco"
        print(f"{nombre_votante} votó en blanco.")
    votos[candidato] += 1
    ya_votaron.add(nombre_votante)

def resultado(votos):
    """Devuelve el diccionario de votos ordenado de mayor a menor."""
    votos_ordenados = sorted(votos.items(), key=lambda item: item[1], reverse=True)
    return dict(votos_ordenados)

def ganador(votos):
    """Devuelve el candidato con más votos."""
    return max(votos, key=votos.get)

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
votos_finales = resultado(votos)

for candidato, cantidad in votos_finales.items():
    print(f"{candidato} : {cantidad} votos")

ganador_final = ganador(votos_finales)
print(f"🏆 Ganador/a: {ganador_final} con {votos_finales[ganador_final]} votos")
