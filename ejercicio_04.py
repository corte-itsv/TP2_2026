def min_max(numeros):
    numero_minimo = numeros[0] # Hipotesis nada mas
    numero_maximo = numeros[0] # Hipotesis nada mas
    for numero in numeros:
        if numero < numero_minimo:
            numero_minimo = numero
        if numero > numero_maximo:
            numero_maximo = numero
    return (numero_minimo, numero_maximo)

numeros_ejemplo = [34, 7, 89, 12, 56, 3, 78, 45]

numeros_finales = min_max(numeros_ejemplo)
numero_minimo, numero_maximo = numeros_finales
print("Mínimo: ", numero_minimo)
print("Mínimo: ", numero_maximo)