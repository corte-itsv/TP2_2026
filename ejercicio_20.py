def registrar_alumno(alumnos_dict, nombre):
    if nombre in alumnos_dict:  # Fixed variable name
        return "El alumno ya está registrado"
    else:
        alumnos_dict[nombre] = nombre
        return "Alumno registrado"



def votar(votos, ya_votaron, nombre_votante, candidato, padron):
    if padron not in alumnos:
        return "Padron no registrado"
    elif padron in ya_votaron:
        return "El alumno ya votó"
    else:
        ya_votaron.add(padron)
        votos[candidato] = votos.get(candidato, 0) + 1
        return "Voto registrado"


def resultado(votos):
    if not votos:
        return "No se han registrado votos"
    ganador = max(votos, key=votos.get)
    return f"El ganador es {ganador} con {votos[ganador]} votos"


def ganador(votos):
    if not votos:
        return "No se han registrado votos"
    ganador = max(votos, key=votos.get)
    return ganador

padron = {}
alumnos = {}
ya_votaron = set()
votos    = {"Ana": 0, "Luis": 0, "Sol": 0, "Blanco": 0}

registrar_alumno(alumnos, "Valentina")  # Pass alumnos, not padron
registrar_alumno(alumnos, "Tomás")
registrar_alumno(alumnos, "Camila")
registrar_alumno(alumnos, "Diego")
registrar_alumno(alumnos, "Lucía")


votar(votos, ya_votaron, "Valentina", "Ana",  padron)
votar(votos, ya_votaron, "Tomás",     "Sol",  padron)
votar(votos, ya_votaron, "Camila",    "Ana",  padron)
votar(votos, ya_votaron, "Diego",     "Luis", padron)
votar(votos, ya_votaron, "Valentina", "Sol",  padron)  
votar(votos, ya_votaron, "Pedro",     "Ana",  padron)  
votar(votos, ya_votaron, "Lucía",     "Marta",padron)


print(resultado(votos))
print(ganador(votos))







