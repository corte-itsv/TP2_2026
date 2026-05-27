def min_max(numeros):
    minimo = numeros[0]
    maximo = numeros[0]

    for numero in numeros:
        if numero < minimo:
            minimo = numero

        if numero > maximo:
            maximo = numero

    return (minimo, maximo)


# Lista de prueba
numeros = [34, 7, 89, 12, 56, 3, 78, 45]

# Desempaquetado de la tupla
minimo, maximo = min_max(numeros)

# Mostrar resultados
print("Mínimo:", minimo)
print("Máximo:", maximo)