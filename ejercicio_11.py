#hacer una funcio "existe_elemento(array, elemento_a_buscar)"
# que busque un elemento y diga si existe
# (True) o si no existe (False)

def existe_elemento(array, elemento_a_buscar):
    for elemento in array:
        if elemento_a_buscar == elemento:
            return True
    return False

def sin_duplicados(lista_original): # 4 billones
    set_agregados = set()
    lista_sin_duplicados = []
    for elemento in lista_original:
        if elemento not in set_agregados:
            lista_sin_duplicados.append(elemento)
            set_agregados.add(elemento)
    return lista_sin_duplicados
    

lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nombres = ["Ana", "Luis", "Ana", "Sol", "Luis", "Marcos"]

respuesta = existe_elemento(lista, "Ana")


lista_final_n1 = sin_duplicados(lista)
print(lista_final_n1)
lista_final_n2 = sin_duplicados(nombres)
print(lista_final_n2)
