

def invertir(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        elemento = lista[i]
        lista_invertida.append(elemento)
    return lista_invertida  
original = [1, 2, 3, 4, 5]
print(invertir(original)) 
letras = ["a", "b", "c", "d"]
print(invertir(letras))  