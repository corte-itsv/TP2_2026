def invertir(lista):
    lista_invertida = []
    for elemento in lista:
        lista_invertida.insert(0, elemento)
    return lista_invertida



original = [1, 2, 3, 4, 5]
letras   = ["a", "b", "c", "d"]

print("=== INVERTIDOS ===")

original_inverida = invertir(original)
print("Lista 'Original':", original_inverida)

letras_invertidas = invertir(letras)
print("Lista 'Letras':", letras_invertidas)