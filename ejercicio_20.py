def registrar_alumno(padron, nombre):
        padron.add(nombre)

def votar(votos, ya_votaron, nombre_votante, candidato, padron):
    if nombre_votante in padron:
        if nombre_votante not in ya_votaron:
            if candidato in votos:
                votos[candidato] = votos[candidato] + 1
                ya_votaron.add(nombre_votante)
            else:
                votos["Blanco"] = votos["Blanco"] + 1
                ya_votaron.add(nombre_votante)
                print(f"{nombre_votante} votó en blanco.")
        else:
            print(f"{nombre_votante} ya votó.")
    else:
        print(f"{nombre_votante} no está habilitado para votar.")

def listar_tuplas(votos):
    lista_de_tuplas = []
    for candidato, sus_votos in votos.items():
        lista_de_tuplas.append((candidato, sus_votos))
    return lista_de_tuplas

def ordenar_lista_de_tuplas(votos):
    lista_de_tuplas = listar_tuplas(votos)
    lista_de_tuplas_ordenada = sorted(lista_de_tuplas, key=lambda x: x[1], reverse=True)
    return lista_de_tuplas_ordenada

def nuevo_dict_ordenado(votos):
    lista_de_tuplas_ordenada = ordenar_lista_de_tuplas(votos)
    dict_nuevo = {}
    for (candidato, sus_votos) in lista_de_tuplas_ordenada:
        dict_nuevo[candidato] = sus_votos
    return dict_nuevo
            
def imprimir_votos_correctamente(votos):
    dict_nuevo = nuevo_dict_ordenado(votos)
    for candidato, sus_votos in dict_nuevo.items():
        if sus_votos != 1:
            print(f"{candidato:<7}: {sus_votos} votos")
        else:
            print(f"{candidato:<7}: {sus_votos} voto")

def ganador(votos):
    candidato_mas_votado = ""
    votos_del_candidato_mas_votado = 0
    dict_nuevo = nuevo_dict_ordenado(votos)
    for candidato, sus_votos in dict_nuevo.items():
        if sus_votos > votos_del_candidato_mas_votado:
            votos_del_candidato_mas_votado = sus_votos
            candidato_mas_votado = candidato
    return (candidato_mas_votado, votos_del_candidato_mas_votado)


def sistema():
    while True:
        
        print("")
        print("======= MENÚ DE OPCIONES =======")
        print("1) Empezar con la votación.")
        print("2) Mostrar resultados de la votación.")
        print("0) Salir.")
        print("")
        
        opcion_ingresada = int(input("Ingrese un numero de opción: "))

        if opcion_ingresada == 1:
            print("")
            print("==== CANDIDATOS ====")
            print("Ana")
            print("Luis")
            print("Sol")
            print("Voto en blanco")
            print("")
            
            nombre_ingresado_por_el_votante = input("Ingresa tu nombre para corroborar que podes votar: ")
            nombre_ingresado_por_el_votante = nombre_ingresado_por_el_votante.capitalize()
            
            if nombre_ingresado_por_el_votante in padron:
                candidato = input("Ingrese el NOMBRE de candidato que queres votar, con la primer letra en mayuscula: ")
                votar(votos, ya_votaron, nombre_ingresado_por_el_votante, candidato, padron)
        
            else:
                print(f"{nombre_ingresado_por_el_votante} no está habilitado para votar.")
                
        elif opcion_ingresada == 2:
            imprimir_votos_correctamente(votos)
            print("")
            candidato_mas_votado, votos_del_candidato_mas_votado = ganador(votos)
            print(f"🏆 Ganador/a: {candidato_mas_votado} con {votos_del_candidato_mas_votado} votos")
        elif opcion_ingresada == 0:
            print("¡Gracias por participar!")
            break
        else:
            print("Número de opción inválido. Por favor vuela a intentarlo.")







padron   = set()
ya_votaron = set()
votos    = {"Luis": 0, "Sol": 0, "Blanco": 0, "Ana": 0}




registrar_alumno(padron, "Valentina")
registrar_alumno(padron, "Tomas")
registrar_alumno(padron, "Camila")
registrar_alumno(padron, "Diego")
registrar_alumno(padron, "Lucia")

print("¡Bienvenido a la votación!")

sistema()